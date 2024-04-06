import Levenshtein
import requests

from utils.screenshot import Screenshot
from utils.ocr import get_achievement_name, get_achievement_desc, ratio

GAME_DATA_URL = "https://github.com/hashblen/HSRAchievementData/raw/main/output/achievement_processed_data.json"


class GameData:
    """GameData class for storing and accessing game data"""

    def __init__(self) -> None:
        try:
            response = requests.get(GAME_DATA_URL)
            data = response.json()
        except requests.exceptions.RequestException:
            raise Exception("Failed to fetch game data from " + GAME_DATA_URL)

        # self.version = data["version"]
        self.data = data

    def get_closest_name_match(self, index: int, screenshotter: Screenshot) -> tuple[str, int]:
        """Get closest match from name

        :param index: The index of the achievement to get the closest match from
        :param screenshotter: The screenshotter to use
        :return: The closest match name and ID
        """
        name_from_image: str = get_achievement_name(index, screenshotter)
        max_cost: float = 0.
        max_name: str = ""
        max_id: int = -1
        for c_id_str in self.data.keys():
            c_id: int = int(c_id_str)
            chive_name = self.data[c_id_str]["title"]
            cost = Levenshtein.ratio(name_from_image, chive_name)
            if max_name == chive_name:  # If the max and the current achievements have the same name, look at desc.
                desc_from_image = get_achievement_desc(index, screenshotter)
                desc_cost = Levenshtein.ratio(desc_from_image, self.data[c_id_str]["desc"])
                max_desc_cost = Levenshtein.ratio(desc_from_image, self.data[str(max_id)]["desc"])
                if desc_cost > max_desc_cost:
                    max_cost = cost
                    max_name = chive_name
                    max_id = c_id
                    continue
            if cost > max_cost:
                max_cost = cost
                max_name = chive_name
                max_id = c_id
        if max_cost < 0.5:
            raise ValueError("No close match")
        return max_name, max_id
