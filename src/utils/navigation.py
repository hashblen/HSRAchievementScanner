import vgamepad as vg
import time

import win32gui


def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor of two numbers

    :param a: The first number
    :param b: The second number
    :return: The greatest common divisor of the two numbers
    """
    while b:
        a, b = b, a % b
    return a


class Navigation:
    """Navigation class for navigating the game window"""

    WAKE_WAIT = 0.5
    PRESSED_FOR = 0.05
    SCAN_TIME = 0.2
    NAV_TIME = 0.2

    def __init__(self, hwnd: int, config: dict) -> None:
        self._hwnd = hwnd
        self._width, self._height = win32gui.GetClientRect(self._hwnd)[2:]
        if self._width == 0 or self._height == 0:
            self.bring_window_to_foreground(9)
            self._width, self._height = win32gui.GetClientRect(self._hwnd)[2:]
        self._left, self._top = win32gui.ClientToScreen(self._hwnd, (0, 0))

        self.NAV_TIME += config["nav_delay"]
        self.SCAN_TIME += config["scan_delay"]

        self.gamepad = vg.VX360Gamepad()

    def bring_window_to_foreground(self, cmd_show: int = 5) -> None:
        """Bring the game window to the foreground

        :param cmd_show: The command to show the window, defaults to 5
        """
        win32gui.ShowWindow(self._hwnd, cmd_show)
        win32gui.SetForegroundWindow(self._hwnd)

    def wake_up(self) -> None:
        self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        self.gamepad.update()
        time.sleep(self.WAKE_WAIT)
        self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        self.gamepad.update()
        time.sleep(self.WAKE_WAIT)

    def go_down(self) -> None:
        if self.gamepad is None:
            raise ValueError('GamepadNotInitialized')
        self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        self.gamepad.update()
        time.sleep(self.PRESSED_FOR)
        self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        self.gamepad.update()
        time.sleep(self.SCAN_TIME)  # to wait to go down

    def change_tab(self) -> None:
        if self.gamepad is None:
            raise ValueError('GamepadNotInitialized')
        self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        self.gamepad.update()
        time.sleep(self.PRESSED_FOR)
        self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        self.gamepad.update()
        time.sleep(self.NAV_TIME)  # to wait for the tab to load

    def get_aspect_ratio(self) -> str:
        """Get the aspect ratio of the game window

        :return: The aspect ratio of the game window
        """
        x, y = self._width, self._height
        pgcd = gcd(x, y)
        return f"{x // pgcd}:{y // pgcd}"
