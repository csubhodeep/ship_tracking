import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from json import dump
from pathlib import Path
from typing import Dict
from typing import List
from typing import Union
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen

import requests

from configs import API_ENDPOINT_URL
from utils.page_parser import parse_tech_specs, parse_links


def get_ship_data(config: Dict[str, Union[str, int]], path_to_data: Path) -> None:
    """This function makes an API call to the marinetraffic endpoint and saves the data received as results on disk.
    :param config: Its a dict of values to pass while making the API call
    """
    response_data = requests.get(url=API_ENDPOINT_URL.format(**config)).json()

    with open(path_to_data, 'w') as f:
        dump(response_data, f)


def extract_tech_specs(source_uri: str) -> Dict[str, str]:
    try:
        html_page = urlopen(url=source_uri).read()
    except urllib.error.URLError as ex:
        print(f"Could not fetch tech specs for - {source_uri}. Error - {ex}")
        return None

    try:
        res = parse_tech_specs(html_page)
        # Below field is added for QA purposes only
        res['source_page'] = source_uri
        return res
    except Exception as ex:
        print(f"Could not fetch tech specs for - {source_uri}. Error - {ex}")


def extract_product_links(source_uri: str) -> List[str]:
    html_page = urlopen(url=source_uri).read()

    return parse_links(html_page)


def get_engine_tech_specs(source_uri: str, path_to_data: Path) -> None:
    urls = [urljoin(base="https://" + urlparse(source_uri).netloc + "/", url=ele) for ele in
            extract_product_links(source_uri)]

    res = []
    with ThreadPoolExecutor() as executor:
        jobs = (executor.submit(extract_tech_specs, url) for url in urls)
        for ftr in as_completed(jobs):
            res.append(ftr.result())

    with open(path_to_data, 'w') as f:
        dump(res, f)
