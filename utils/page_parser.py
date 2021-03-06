from typing import Dict, List

from bs4 import BeautifulSoup


def parse_tech_specs(page: str) -> Dict[str, str]:
    """This function scrapes the engine tech specs from a single page
    :param page: the HTML page as a long running string
    :return: a dict containing all the relevant elements
    """
    soup = BeautifulSoup(page, 'html.parser')

    tags = soup.findAll("div", {"class": "product-specs-category"})

    model_specs = tags[1].findAll("div", {"class": "spec spaced-spec"})

    engine_model = ""
    for ele in model_specs:
        if ele.strong.text == "Engine Model":
            engine_model = ele.span.text

    product_specs = tags[0].findAll("div", {"class": "spec spaced-spec"})

    result = {ele.strong.text: ele.span.text for ele in product_specs}

    result["Engine Model"] = engine_model

    return result


def parse_links(page: str) -> List[str]:
    """This function scrapes all the links in the base page
    :param page: the HTML page as a long running string
    :return: a list of links to the page for each engine details
    """
    soup = BeautifulSoup(page, 'html.parser')

    tags = list(soup.findAll("div", {"class": "parbase productCards productCardTop3Specs selector-container"}))

    soup2 = BeautifulSoup(str(tags[0]), 'html.parser')

    tags = list(soup2.findAll("li"))

    return [tags[i].a["href"].lstrip("/") for i in range(242)]
