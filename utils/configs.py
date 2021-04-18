
from pathlib import Path

API_ENDPOINT_URL = "https://services.marinetraffic.com/api/exportvesseltrack/{API_KEY}/v:3/period:{PERIOD}/fromdate:{FROM_DATE}/todate:{TO_DATE}/mmsi:{MMSI}/protocol:jsono"

PATH_TO_DATA_FOLDER = Path.cwd().joinpath("data")

WEB_PAGE_ADDRESS = "https://www.finning.com/en_CA/products/new/power-systems/electric-power-generation.html"