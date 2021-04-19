from json import dump
import os
from pathlib import Path
from typing import Dict
from typing import Tuple
from typing import Union

from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

from configs import API_ENDPOINT_URL
from utils.page_parser import parse_tech_specs


def get_ship_data(config: Dict[str, Union[str, int]], path_to_data: Path) -> None:
	"""This function makes an API call to the marinetraffic endpoint and saves the data received as results on disk.
	:param config: Its a dict of values to pass while making the API call
	"""
	response_data = requests.get(url=API_ENDPOINT_URL.format(**config)).json()

	with open(path_to_data, 'w') as f:
		dump(response_data, f)


def extract_tech_specs(source_uri: str) -> Dict[str, float]:

	# html_page = requests.get(url=source_uri).text

	html_page = os.popen(f"curl -X GET {source_uri}").read()


	return parse_tech_specs(html_page)


def extract_product_links(source_uri: str) -> Tuple[str, ...]:

	return (
		"https://www.finning.com/en_CA/products/new/power-systems/electric-power-generation/diesel-generator-sets/1000033110.html",
		"https://www.finning.com/en_CA/products/new/power-systems/electric-power-generation/diesel-generator-sets/1000001866.html"
	)


def get_engine_tech_specs(source_uri: str, path_to_data: Path) -> None:

	urls = extract_product_links(source_uri)


	res = []
	with ThreadPoolExecutor() as executor:
		jobs = (executor.submit(extract_tech_specs, url) for url in urls)
		for ftr in as_completed(jobs):
			res.append(ftr.result())

	with open(path_to_data, 'w') as f:
		dump(res, f)
