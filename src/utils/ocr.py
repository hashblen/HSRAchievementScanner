import Levenshtein
import numpy as np
from PIL import Image
import pytesseract
from config.screenshot import *

from utils.screenshot import Screenshot


def image_to_string(img: Image, whitelist=None, method="tesseract", lang="en", psm=7) -> str:
    if method == "tesseract":
        return image_to_string_tesseract(img, psm=psm, whitelist=whitelist, lang=lang)
    else:
        raise ValueError("Not using a valid OCR model!")


def image_to_string_tesseract(img: Image, psm=7, whitelist=None, lang="en") -> str:
    if whitelist:
        config = f'-c tessedit_char_whitelist="{whitelist}" --psm {psm} -l hsr3-{lang}'
    else:
        config = f'--psm {psm} -l hsr3-{lang}'
    return pytesseract.image_to_string(img, config=config).replace("\n", " ").strip()


def get_achievement_name(index: int, screenshotter: Screenshot, method="tesseract", lang="en") -> str:  # index starts at 0
    index = min(index, 4)
    img = screenshotter.take_screenshot(NAME_X, NAME_Y[index], NAME_X_END - NAME_X, FONT_HEIGHT)
    return image_to_string(img, method=method, lang=lang)


def get_achievement_desc(index: int, screenshotter: Screenshot, method="tesseract", lang="en") -> str:
    index = min(index, 4)
    img = screenshotter.take_screenshot(NAME_X, NAME_Y[index] + DESC_SHIFT_Y, NAME_X_END - NAME_X, FONT_HEIGHT)
    return image_to_string(img, method=method, lang=lang)


def get_completed_status(index: int, screenshotter: Screenshot, method="tesseract", lang="en") -> tuple[bool, bool]:
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
        return True, True
    # Check if "Completed"
    calc_ratio = Levenshtein.ratio(image_to_string(img, whitelist='Completed', method=method, lang=lang), 'Completed')
    return calc_ratio >= 0.8, False


def ratio(s1, s2, wLev=1, wHam=1):
    ham_ratio = (1 - Levenshtein.hamming(s1, s2) / (len(s1) + len(s2)))
    return (wLev * Levenshtein.ratio(s1, s2) + wHam * ham_ratio) / (wLev + wHam)
