from json import dump
from pathlib import Path
from typing import Dict
from typing import Union

import requests

from configs import API_ENDPOINT_URL
from configs import PATH_TO_DATA_FOLDER

def get_vessel_data(config: Dict[str, Union[str, int]]) -> None:
	"""This function makes an API call to the marinetraffic endpoint and saves the data received as results on disk.
	:param config: Its a dict of values to pass while making the API call
	"""
	response_data = requests.get(url=API_ENDPOINT_URL.format(**config)).json()

	file_path = Path(PATH_TO_DATA_FOLDER).joinpath(f"position_{config['MMSI']}.json")

	with open(file_path, 'w') as f:
		dump(response_data, f)


if __name__ == "__main__":
	config = {
		"API_KEY": "955c8d65542b8efb143438a1c8cbcd9e126e0413",
		"PERIOD": "hourly",
		"DAYS": 2,
		"FROM_DATE": "2021-03-01 00:00:00",
		"TO_DATE": "2021-03-02 23:59:59",
		"MMSI": "269057500"
	}

	get_vessel_data(config=config)