import Levenshtein
import numpy as np
from PIL import Image
import pytesseract
from config.screenshot import *

from utils.screenshot import Screenshot


def image_to_string(img: Image, psm=7, whitelist=None) -> str:
    if whitelist:
        config = f'-c tessedit_char_whitelist="{whitelist}" --psm {psm} -l DIN-Alternate'
    else:
        config = f'--psm {psm} -l DIN-Alternate --user-words eng'
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
    # Check if unclaimed
    x, y = CLAIM_BOX_SHIFT_AFTER_RESIZE[0], CLAIM_BOX_SHIFT_AFTER_RESIZE[1]
    z, t = CLAIM_BOX_SHIFT_AFTER_RESIZE[2], CLAIM_BOX_SHIFT_AFTER_RESIZE[3]
    arr = np.array(img)
    area = arr[y:t, x:z, :]
    average_color = np.mean(area, axis=(0, 1))
    color_distance = np.sqrt(np.sum((average_color - np.array([0xFF, 0xC7, 0x59])) ** 2))
    if color_distance < 5:  # Arbitrary value, can induce bugs ?
        return True
    # Check if "Completed"
    return Levenshtein.ratio(image_to_string(img, whitelist='Completed'), 'Completed') >= 0.8


def ratio(s1, s2, wLev=1, wHam=1):
    ham_ratio = (1 - Levenshtein.hamming(s1, s2) / (len(s1) + len(s2)))
    return (wLev * Levenshtein.ratio(s1, s2) + wHam * ham_ratio) / (wLev + wHam)
