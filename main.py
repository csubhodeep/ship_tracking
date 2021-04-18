from argparse import ArgumentParser
import os

from lib.init_db import DbConnector
from utils.create_table import create_all_tables
from utils.extraction import get_ship_data
from utils.transformation import transform_csv
from utils.loading import load_postion_data

from utils.configs import PATH_TO_DATA_FOLDER, POSITION_DATA_SCHEMA

def get_args():
	arg_parser = ArgumentParser()
	arg_parser.add_argument("--create_or_replace_tables",
							type=bool,
							default=True,
							help="forces the script to create/replace tables")

	return arg_parser.parse_args()


MMSI_IDS = ["269057500", "269057489"]

if __name__ == "__main__":
	args = get_args()
	db_conn = DbConnector()
	# time.sleep(5)
	# print("Waiting for DB to initialize")
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

		# get_ship_data(config=config)

	## TRANSFORM & LOAD
	# 1. transform CSV data
	# for ele in transform_csv(path_to_data=PATH_TO_DATA_FOLDER.joinpath("position_data.csv"), schema=POSITION_DATA_SCHEMA):
	# 	load_postion_data(ele, connector=db_conn)