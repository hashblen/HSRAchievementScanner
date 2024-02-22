import Levenshtein
from PIL import Image
import pytesseract
from config.screenshot import *

from utils.screenshot import Screenshot


def image_to_string(img: Image, psm=7, whitelist=None) -> str:
    if whitelist:
        config = f'-c tessedit_char_whitelist="{whitelist}" --psm {psm} -l DIN-Alternate'
    else:
        config = f'--psm {psm} -l DIN-Alternate'
    return pytesseract.image_to_string(img, config=config).replace("\n", " ").strip()


def get_achievement_name(index: int, screenshotter: Screenshot) -> str:  # index starts at 0
    index = min(index, 4)
    img = screenshotter.take_screenshot(NAME_X, NAME_Y[index], NAME_X_END - NAME_X, FONT_HEIGHT)
    return image_to_string(img)


def get_achievement_desc(index: int, screenshotter: Screenshot) -> str:
    index = min(index, 4)
    img = screenshotter.take_screenshot(NAME_X, NAME_Y[index] + DESC_SHIFT_Y, NAME_X_END - NAME_X, FONT_HEIGHT)
    return image_to_string(img)


def get_completed_status(index: int, screenshotter: Screenshot) -> bool:
    index = min(index, 4)
    img = screenshotter.take_screenshot(COMPLETED_X, COMPLETED_Y[index], COMPLETED_X_END - COMPLETED_X, FONT_HEIGHT)
    return Levenshtein.ratio(image_to_string(img, whitelist='Completed'), 'Completed') >= 0.8
