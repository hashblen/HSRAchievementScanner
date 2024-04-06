import asyncio
import datetime

import pytesseract
from pynput.keyboard import Key, Listener

from PyQt6 import QtCore, QtGui, QtWidgets

from logic.game_data import GameData
from logic.scanner import HSRScanner
from ui.form import Ui_MainWindow
from utils.data import create_debug_folder, executable_path, resource_path, save_to_json

pytesseract.pytesseract.tesseract_cmd = resource_path("assets/tesseract/tesseract.exe")


class ScannerUI(QtWidgets.QMainWindow, Ui_MainWindow):
    """Handler for the UI"""

    is_scanning = False

    def __init__(self) -> None:
        super().__init__()
        self._scanner_thread = None
        self._listener = InterruptListener()
        self.settings = QtCore.QSettings("hashblen", "HSRAchievementScanner")

        # fetch game data
        self._fetch_game_data_thread = FetchGameDataThread()
        self._fetch_game_data_thread.result_signal.connect(self.handle_game_data)
        self._fetch_game_data_thread.error_signal.connect(self.handle_game_data_error)
        self._fetch_game_data_thread.start()

    def handle_game_data(self, game_data: GameData) -> None:
        """Handle on game data loaded

        :param game_data: The game data
        """
        self.game_data = game_data
        self.log("Loaded database")  # version: " + self.game_data.version)
        self.pushButtonStartScan.clicked.connect(self.start_scan)
        self.pushButtonStartScan.setEnabled(True)
        self.pushButtonStartScan.setText("Start Scan")
        for label in [
            self.labelAchievementCount,
            self.labelAchievementCount_2,
            self.labelAchievementCount_3,
            self.labelAchievementCount_4,
            self.labelAchievementCount_5,
            self.labelAchievementCount_6,
            self.labelAchievementCount_7,
            self.labelAchievementCount_8,
            self.labelAchievementCount_9
        ]:
            label.setText("_")
        self._fetch_game_data_thread.deleteLater()

    def handle_game_data_error(self, e: Exception) -> None:
        """Handle on game data error

        :param e: The error
        """
        self.log(str(e))
        self.pushButtonStartScan.clicked.connect(self._fetch_game_data_thread.start)
        self.pushButtonStartScan.setEnabled(True)
        self.pushButtonStartScan.setText("Retry")

    def setup_ui(self, MainWindow: QtWidgets.QMainWindow) -> None:
        super().setupUi(MainWindow)
        self.pushButtonChangeLocation.clicked.connect(self.change_output_location)
        self.pushButtonOpenLocation.clicked.connect(self.open_output_location)
        self.pushButtonRestoreDefaults.clicked.connect(self.reset_settings)

        self.load_settings()

    def change_output_location(self) -> None:
        """Opens a dialog to change the output location of the scan"""
        new_output_location = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Select Output Location", self.lineEditOutputLocation.text()
        )
        if new_output_location:
            self.lineEditOutputLocation.setText(new_output_location)

    def open_output_location(self) -> None:
        """Opens the output location of the scan in the file explorer"""
        output_location = self.lineEditOutputLocation.text()
        if output_location:
            try:
                QtGui.QDesktopServices.openUrl(
                    QtCore.QUrl.fromLocalFile(output_location)
                )
            except Exception as e:
                self.log(f"Error opening output location: {e}")

    def load_settings(self) -> None:
        """Loads the settings for the scan"""
        self.lineEditOutputLocation.setText(
            self.settings.value("output_location", executable_path("StarRailData"))
        )
        self.checkBoxDebugMode.setChecked(
            self.settings.value("debug_mode", False) == "true"
        )
        self.spinBoxNavDelay.setValue(self.settings.value("nav_delay", 0))
        self.spinBoxScanDelay.setValue(self.settings.value("scan_delay", 0))
        self.comboBoxScanner.setCurrentIndex(self.settings.value("scanner", 0))
        self.comboBoxLanguage.setCurrentIndex(self.settings.value("language", 0))

    def save_settings(self) -> None:
        """Saves the settings for the scan"""
        self.settings.setValue("output_location", self.lineEditOutputLocation.text())
        self.settings.setValue("debug_mode", self.checkBoxDebugMode.isChecked())
        self.settings.setValue("nav_delay", self.spinBoxNavDelay.value())
        self.settings.setValue("scan_delay", self.spinBoxScanDelay.value())
        self.settings.setValue("scanner", self.comboBoxScanner.currentIndex())
        self.settings.setValue("language", self.comboBoxLanguage.currentIndex())

    def reset_settings(self) -> None:
        """Resets the settings for the scan"""
        self.settings.setValue("output_location", executable_path("StarRailData"))
        self.settings.setValue("nav_delay", 0)
        self.settings.setValue("scan_delay", 0)
        self.settings.setValue("debug_mode", False)
        self.settings.setValue("scanner", 0)
        self.settings.setValue("language", 0)
        self.load_settings()

    def start_scan(self) -> None:
        """Starts the scan"""
        self.disable_start_scan_button()
        self.save_settings()

        # reset fields
        for label in [
            self.labelAchievementCountProcessed,
            self.labelAchievementCountProcessed_2,
            self.labelAchievementCountProcessed_3,
            self.labelAchievementCountProcessed_4,
            self.labelAchievementCountProcessed_5,
            self.labelAchievementCountProcessed_6,
            self.labelAchievementCountProcessed_7,
            self.labelAchievementCountProcessed_8,
            self.labelAchievementCountProcessed_9
        ]:
            label.setText("0")
        self.textEditLog.clear()

        # get method string
        method = ["tesseract", "easyocr", "doctr"][self.comboBoxScanner.currentIndex()]

        # get language
        lang = ["en"][self.comboBoxLanguage.currentIndex()]

        # initialize scanner
        try:
            scanner = HSRScanner(self.get_config(), self.game_data, method=method, lang=lang)
            scanner.log_signal.connect(self.log)
            scanner.update_signal.connect(self.increment_progress)
            scanner.complete_signal.connect(self._listener.stop)
        except Exception as e:
            self.log(str(e))
            self.enable_start_scan_button()
            return

        # initialize thread
        self._scanner_thread = ScannerThread(scanner)
        self._scanner_thread.log_signal.connect(self.log)

        self._scanner_thread.result_signal.connect(self.handle_result)
        self._scanner_thread.result_signal.connect(self._scanner_thread.deleteLater)
        self._scanner_thread.result_signal.connect(self.enable_start_scan_button)

        self._scanner_thread.error_signal.connect(self.log)
        self._scanner_thread.error_signal.connect(self._scanner_thread.deleteLater)
        self._scanner_thread.error_signal.connect(self.enable_start_scan_button)
        self._scanner_thread.error_signal.connect(self._listener.stop)

        self._listener.interrupt_signal.connect(self._scanner_thread.interrupt_scan)

        # start thread
        self._scanner_thread.started.connect(self._listener.start)
        self._scanner_thread.start()

    def get_config(self) -> dict:
        """Gets the configuration for the scan

        :return: The configuration for the scan
        """
        config = {}

        # delays
        config["nav_delay"] = self.spinBoxNavDelay.value() / 1000
        config["scan_delay"] = self.spinBoxScanDelay.value() / 1000

        # debug mode
        config["debug"] = self.checkBoxDebugMode.isChecked()
        config["debug_output_location"] = ""

        if config["debug"]:
            config["debug_output_location"] = create_debug_folder(
                self.lineEditOutputLocation.text()
            )
            self.log(
                "[DEBUG] Debug mode enabled. Debug output will be saved to "
                + config["debug_output_location"]
            )

        return config

    def handle_result(self, data: dict) -> None:
        """Handles the result of the scan

        :param data: The data from the scan
        """
        output_location = self.lineEditOutputLocation.text()
        file_name = (
            f"HSRScanData_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )
        save_to_json(data, output_location, file_name)
        self.log("Scan complete. Data saved to " + output_location)

    def increment_progress(self, tab: int) -> None:
        """Increments the number on the UI based on the enum

        :param tab: The tab to increment the progress for
        """
        if tab < 1 or tab > 9:
            self.log("Error in increment_progress: tab not between 1 and 9.")
        tab_labels = [
            None,
            self.labelAchievementCountProcessed,
            self.labelAchievementCountProcessed_2,
            self.labelAchievementCountProcessed_3,
            self.labelAchievementCountProcessed_4,
            self.labelAchievementCountProcessed_5,
            self.labelAchievementCountProcessed_6,
            self.labelAchievementCountProcessed_7,
            self.labelAchievementCountProcessed_8,
            self.labelAchievementCountProcessed_9
        ]
        tab_labels[tab].setText(str(int(tab_labels[tab].text()) + 1))

    def disable_start_scan_button(self) -> None:
        """Disables the start scan button and sets the text to Processing"""
        self.is_scanning = True
        self.pushButtonStartScan.setText("Processing...")
        self.pushButtonStartScan.setEnabled(False)

    def enable_start_scan_button(self) -> None:
        """Enables the start scan button and sets the text to Start Scan"""
        self.is_scanning = False
        self.pushButtonStartScan.setText("Start Scan")
        self.pushButtonStartScan.setEnabled(True)

    def log(self, message: str) -> None:
        """Logs a message to the log box

        :param message: The message to log
        """
        self.textEditLog.appendPlainText(
            f"[{datetime.datetime.now().strftime('%H:%M:%S')}] > {str(message)}"
        )
        self.textEditLog.verticalScrollBar().setValue(self.textEditLog.verticalScrollBar().maximum())


class FetchGameDataThread(QtCore.QThread):
    """FetchGameDataThread class handles fetching the game data in a separate thread"""

    result_signal = QtCore.pyqtSignal(object)
    error_signal = QtCore.pyqtSignal(object)

    def __init__(self) -> None:
        """Constructor"""
        super().__init__()

    def run(self) -> None:
        """Runs the fetch game data"""
        try:
            self.result_signal.emit(GameData())
            self.quit()
        except Exception as e:
            self.error_signal.emit(e)


class InterruptListener(QtCore.QThread):
    """InterruptListener class listens for the enter key to interrupt the scan"""

    interrupt_signal = QtCore.pyqtSignal()

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.listener = None

    def run(self):
        """Runs the listener"""
        with Listener(on_press=self.on_press) as listener:
            self.listener = listener
            listener.join()

    def stop(self):
        """Stops the listener"""
        if self.listener:
            self.listener.stop()

    def on_press(self, key: Key) -> None:
        """Handles the key press. If the key is enter, emit the interrupt signal

        :param key: The key that was pressed
        """

        if key == Key.enter:
            self.interrupt_signal.emit()


class ScannerThread(QtCore.QThread):
    """ScannerThread class handles the scanning in a separate thread"""

    result_signal = QtCore.pyqtSignal(object)
    error_signal = QtCore.pyqtSignal(object)
    log_signal = QtCore.pyqtSignal(str)

    def __init__(self, scanner: HSRScanner) -> None:
        """Constructor

        :param scanner: The HSRScanner class instance
        """
        super().__init__()
        self._scanner = scanner
        self._interrupt_requested = False

    def run(self) -> None:
        """Runs the scan"""
        try:
            self.log_signal.emit("Starting scan...")
            res = asyncio.run(self._scanner.start_scan())
            if self._interrupt_requested:
                self.error_signal.emit("Scan interrupted")
            else:
                self.result_signal.emit(res)
        except Exception as e:
            self.error_signal.emit(
                f"Scan aborted with error {e.__class__.__name__}: {e} (Try scanning with a different window "
                f"resolution, or fullscreen/windowed mode, or increasing nav/scan delay in scanner configuration.)"
            )

    def interrupt_scan(self) -> None:
        """Interrupts the scan"""
        self._interrupt_requested = True
        self._scanner.stop_scan()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(resource_path("assets/images/app.ico")))
    MainWindow = QtWidgets.QMainWindow()
    ui = ScannerUI()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
