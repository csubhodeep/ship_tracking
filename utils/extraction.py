from json import dump
from pathlib import Path
from typing import Dict
from typing import Union

import requests

from configs import API_ENDPOINT_URL
from configs import PATH_TO_DATA_FOLDER

def get_ship_data(config: Dict[str, Union[str, int]]) -> None:
	"""This function makes an API call to the marinetraffic endpoint and saves the data received as results on disk.
	:param config: Its a dict of values to pass while making the API call
	"""
	response_data = requests.get(url=API_ENDPOINT_URL.format(**config)).json()

	file_path = Path(PATH_TO_DATA_FOLDER).joinpath(f"position_{config['MMSI']}.json")

	with open(file_path, 'w') as f:
		dump(response_data, f)