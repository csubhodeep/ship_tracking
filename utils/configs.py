
from pathlib import Path

API_ENDPOINT_URL = "https://services.marinetraffic.com/api/exportvesseltrack/{API_KEY}/v:3/period:{PERIOD}/fromdate:{FROM_DATE}/todate:{TO_DATE}/mmsi:{MMSI}/protocol:jsono"

PATH_TO_DATA_FOLDER = Path.cwd().joinpath("data")

# the following is a schema to be used during the transformation step
POSITION_DATA_SCHEMA = {
	'SHIP_ID': str,
	'TIMESTAMP': str,
	'SPEED': float,
	'LON': float,
    'LAT': float,
    'IMO': int,
    'STATUS': int,
    'COURSE': int,
    'HEADING': int,
    'MMSI': int
}