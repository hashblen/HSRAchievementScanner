import datetime
import os

import win32gui
from PIL import Image, ImageGrab


class Screenshot:
    """For taking screenshots of the game window"""

    def __init__(self, hwnd, debug: bool = False, debug_output_location: str = ""):
        """Constructor

        :param hwnd: The window handle of the game window
        :param debug: Whether to save screenshots, default False
        :param debug_output_location: Output location of saved screenshots
        """
        self._window_width, self._window_height = win32gui.GetClientRect(hwnd)[2:]
        self._window_x, self._window_y = win32gui.ClientToScreen(hwnd, (0, 0))

        self._x_scaling_factor = self._window_width / 1920
        self._y_scaling_factor = self._window_height / 1080

        self._debug = debug
        self._debug_output_location = debug_output_location

    def take_screenshot(self, x: float, y: float, width: float, height: float) -> Image:
        x = self._window_x + int(self._window_width * x)
        y = self._window_y + int(self._window_height * y)
        width = int(self._window_width * width)
        height = int(self._window_height * height)
        screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height), all_screens=True)
        screenshot = screenshot.resize((int(width / self._x_scaling_factor), int(height / self._y_scaling_factor)))

        if self._debug:
            self._save_image(screenshot)

        return screenshot

    def _save_image(self, img: Image) -> None:
        """Save the image on disk.

        :param img: The image to save.
        """
        file_name = f"{datetime.datetime.now().strftime('%H%M%S%f')}.png"
        output_location = os.path.join(self._debug_output_location, file_name)
        img.save(output_location)