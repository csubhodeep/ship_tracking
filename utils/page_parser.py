
from bs4 import BeautifulSoup

def parse_tech_specs(page: str):

    soup = BeautifulSoup(page, 'html.parser')

    tags = list(soup.findAll("div",{"class":"product-specs-category"}))

    engine_specs = tags[1]

    engine_model = engine_specs.span.text

    product_specs = tags[0].findAll("div", {"class": "spec spaced-spec"})

    minimum_rating = product_specs[0].span.text

    maximum_rating = product_specs[1].span.text

    frequency = product_specs[4].span.text

    voltage = product_specs[3].span.text

    speed = product_specs[5].span.text

    return {
        "Engine Model": engine_model,
        "Frequency": frequency,
        "Max. Rating": maximum_rating,
        "Min. Rating": minimum_rating,
        "Speed": speed,
        "Voltage": voltage
    }


