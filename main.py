from argparse import ArgumentParser

from lib.init_db import DbConnector
from utils.create_table import create_all_tables

def get_args():
	arg_parser = ArgumentParser()
	arg_parser.add_argument("--create_or_replace_tables",
							type=bool,
							default=True,
							help="forces the script to create/replace tables")

	return arg_parser.parse_args()


def initialize_connection():
	return DbConnector().get_connection()


if __name__ == "__main__":
	args = get_args()
	db_conn = initialize_connection()
	# time.sleep(5)
	# print("Waiting for DB to initialize")
	if args.create_or_replace_tables:
		create_all_tables(engine=db_conn.get_engine())