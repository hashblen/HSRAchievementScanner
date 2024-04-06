import time

import win32gui
from PyQt6 import QtCore

from logic.game_data import GameData
from utils.ocr import get_completed_status
from utils.screenshot import Screenshot
from utils.navigation import Navigation

SUPPORTED_ASPECT_RATIOS = ["16:9"]


class HSRScanner(QtCore.QObject):
    update_signal = QtCore.pyqtSignal(int)
    log_signal = QtCore.pyqtSignal(str)
    complete_signal = QtCore.pyqtSignal()

    def __init__(self, config: dict, game_data: GameData):
        """Constructor

                :param config: The config dict
                :param game_data: The GameData class instance
                :raises Exception: Thrown if the game is not found
                :raises Exception: Thrown if no scan options are selected
                """
        super().__init__()
        for i, game_name in enumerate(
                [
                    "Honkai: Star Rail",
                    "崩坏：星穹铁道",
                    "崩壞：星穹鐵道",
                    "붕괴:\u00A0스타레일",
                    "崩壊：スターレイル",
                    "Honkai\u00A0: Star Rail",
                ]
        ):
            self._hwnd = win32gui.FindWindow("UnityWndClass", game_name)
            if self._hwnd:
                self._is_en = i == 0
                break
        if not self._hwnd:
            raise Exception(
                "Honkai: Star Rail not found. Please open the game and try again."
            )
        self._game_data = game_data
        self._config = config
        self._nav = Navigation(self._hwnd, self._config)

        self._aspect_ratio = self._nav.get_aspect_ratio()
        if self._aspect_ratio not in SUPPORTED_ASPECT_RATIOS:
            raise Exception(
                f"Aspect ratio {self._aspect_ratio} not supported. Supported aspect ratios: {SUPPORTED_ASPECT_RATIOS}"
            )

        self._screenshot = Screenshot(
            self._hwnd,
            config["debug"],
            config["debug_output_location"],
        )

        self._interrupt_event = False

    async def start_scan(self) -> dict:
        """Starts the scan

        :return: The scan results
        """
        if not self._is_en:
            self.log_signal.emit(
                "ERROR: Non-English game name detected. The scanner only works with English text."
            )
        self._nav.bring_window_to_foreground()
        self.log_signal.emit("Scanning starting...")
        startScanningTime = time.time()
        result = self.scan()
        self.log_signal.emit("Scanning complete!")
        endScanningTime = time.time()
        lengthScanningTime = endScanningTime - startScanningTime
        print(f"It took {lengthScanningTime} seconds!")
        return {"achievements": result}

    def stop_scan(self) -> None:
        """Stops the scan"""
        self._interrupt_event = True

    def scan(self) -> list[int]:
        self._nav.wake_up()
        if self._interrupt_event:
            return []

        completed_list: list[int] = []

        last_chive_id: int = -1
        current_tab: int = 1
        index: int = 0
        last_completed: int = 0
        completed_count: int = 0
        completed_scanned: int = 0
        isInterrupted: bool = False
        
        # reset Achievement index
        self._nav.change_tab()
        self._nav.change_tab_prev()

        while index < 700 and not isInterrupted:
            completed_scanned = 0
            for i in range(4):
                self._nav.go_down()
            for i in range(5):
                if win32gui.GetForegroundWindow() != win32gui.FindWindow("UnityWndClass", "Honkai: Star Rail"):
                    self.log_signal.emit("Scan interrupted")
                    isInterrupted = True
                    break
                is_chive_completed: bool = get_completed_status(i, self._screenshot)
                if not is_chive_completed:
                    self.log_signal.emit("Skipped uncompleted achievement")
                    completed_scanned += 1
                    continue
                if self._interrupt_event:
                    break
                chive_name, chive_id = self._game_data.get_closest_name_match(i, self._screenshot)
                if len(completed_list) > 4:
                    if last_chive_id == completed_list[-4]:
                        break
                if chive_id in completed_list:
                    continue
                elif is_chive_completed:
                    self.log_signal.emit(f"Achievement: {chive_name} | with id: {chive_id} is completed.")
                    completed_list.append(chive_id)
                    completed_count += 1
                    self.update_signal.emit(current_tab)
                    last_chive_id = chive_id
                    completed_scanned += 1
                    index += 1
                    continue
            if completed_scanned <= 0:
                # self.log_signal.emit(f"Debug: {chive_id} {chive_name}")
                self.log_signal.emit(f"{completed_count - last_completed} completed achievements in tab {current_tab}")
                last_completed = completed_count
                if current_tab == 9:
                    self.log_signal.emit("Scanned all achievements.")
                    break
                self.log_signal.emit("Hit the bottom of the page. Switching tabs.")
                index = 0
                self._nav.change_tab()
                current_tab += 1
                time.sleep(0.3)
                continue
        return completed_list
