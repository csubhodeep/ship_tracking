import json

from pathlib import Path
from typing import Dict
from typing import Iterator
from typing import Union
from typing import Tuple
from typing import List

from datetime import datetime



def transform_row(line: str, columns: List[str]) -> Tuple[bool, Union[None, Dict[str, Union[str, int, float]]]]:
	"""This function organizes the data present in ecah row
	:param line: a line in the CSV file
	:param columns: A list of field names that we wish to load the values for
	:return: A boolean flag denoting the success of transformation
	"""
	raw_values = line.split(",")
	try:
		transformed_values = {}
		for col, raw_val in zip(columns, raw_values):
			transformed_values[col.name] = raw_val if col.name != "TIMESTAMP" else datetime.strptime(raw_val, "%Y-%m-%d %H:%M:%S")
		return True, transformed_values
	except Exception:
		return False, None



def transform_csv(path_to_data: Path, schema: List[str]) -> Iterator[Dict[str, Union[str, int, float]]]:
	"""Return a generator after transforming each row of a CSV file given a schema
	:param path_to_data: path to the file
	:param schema: list of column names
	:return:
	"""
	with open(path_to_data, 'r') as f: # TODO: will run into an OOM if the data is bigger than the memory
		for line_no, line in enumerate(f):
			if line_no:
				is_sucessful, vals = transform_row(line, schema)
				if is_sucessful:
					yield vals
				else:
					pass
			else:
				pass


def transform_json(path_to_data: Path, schema: List[str]) -> Iterator[Dict[str, Union[str, int, float]]]:

	with open(path_to_data, 'r') as f: # TODO: will run into an OOM if the data is bigger than the memory
		json_obj = json.load(f)

	for raw_values_dict in json_obj:
		transformed_values = {}
		for col in schema:
			transformed_values[col.name] = raw_values_dict[col.name] if col.name != "TIMESTAMP" else datetime.strptime(raw_values_dict[col.name], "%Y-%m-%dT%H:%M:%S")
		yield transformed_values