import os
from argparse import ArgumentParser

from lib.init_db import DbConnector
from lib.table_schema import PositionData, ShipEngines, EngineTechSpecs
from utils.configs import PATH_TO_DATA_FOLDER, WEB_PAGE_ADDRESS
from utils.create_table import create_all_tables
from utils.extraction import get_ship_data, get_engine_tech_specs
from utils.loading import load_postion_data, load_engine_data, load_owner_data, load_engine_tech_specs
from utils.transformation import transform_csv, transform_json, transform_ship_owner


def get_args():
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--create_or_replace_tables",
                            type=bool,
                            default=False,
                            help="forces the script to create/replace tables")

    return arg_parser.parse_args()


MMSI_IDS = ["269057500", "269057489"]

if __name__ == "__main__":
    args = get_args()
    db_conn = DbConnector()
    if args.create_or_replace_tables:
        create_all_tables(engine=db_conn.get_engine())

    # EXTRACT - from marinetraffic.com API
    for mmsi in MMSI_IDS:
        config = {
            "API_KEY": os.getenv("API_KEY"),
            "PERIOD": "hourly",
            "DAYS": 2,
            "FROM_DATE": "2021-03-01 00:00:00",
            "TO_DATE": "2021-03-02 23:59:59",
            "MMSI": mmsi
        }

        get_ship_data(config=config, path_to_data=PATH_TO_DATA_FOLDER.joinpath(f"position_{config['MMSI']}.json"))

    ## TRANSFORM & LOAD
    schema_position_data = [ele.name for ele in PositionData.c if ele.name != "key"]
    # 1. CSV data - position
    for ele in transform_csv(path_to_data=PATH_TO_DATA_FOLDER.joinpath("position_data.csv"),
                             schema=schema_position_data):
        load_postion_data(ele, connector=db_conn)
    # pass

    # 2. JSON data - position
    for mmsi in MMSI_IDS:
        for ele in transform_json(path_to_data=PATH_TO_DATA_FOLDER.joinpath(f"position_{mmsi}.json"),
                                  schema=schema_position_data):
            if ele:
                load_postion_data(ele, connector=db_conn)
        # pass

    # 3. CSV data - engines
    schema_engine_data = [ele.name for ele in ShipEngines.c if ele.name != "key"]
    for ele in transform_csv(path_to_data=PATH_TO_DATA_FOLDER.joinpath("ship_engines.csv"), schema=schema_engine_data):
        load_engine_data(ele, connector=db_conn)
    # pass

    # 4. CSV data - owners
    for ele in transform_ship_owner(path_to_data=PATH_TO_DATA_FOLDER.joinpath("ships_per_owner.csv")):
        if ele:
            load_owner_data(ele, connector=db_conn)
    # pass

    ## EXTRACT - engine tech specs from webpage
    get_engine_tech_specs(source_uri=WEB_PAGE_ADDRESS, path_to_data=PATH_TO_DATA_FOLDER.joinpath(f"engine_data.json"))

    ## LOAD
    schema_engine_tech_specs = [ele.name for ele in EngineTechSpecs.c if ele.name != "key"]
    for ele in transform_json(path_to_data=PATH_TO_DATA_FOLDER.joinpath(f"engine_data.json"),
                              schema=schema_engine_tech_specs):
        if ele:
            load_engine_tech_specs(ele, connector=db_conn)
    # pass
