import json

from pathlib import Path
from typing import Dict
from typing import Iterator
from typing import Union
from typing import Callable
from typing import Tuple


def transform_row(line: str, schema: Dict[str, Callable]) -> Tuple[bool, Union[None, Dict[str, Union[str, int, float]]]]:
	"""This function casts the value of each row in a CSV file according to the schema supplied
	:param line: a line in the CSV file
	:param schema: A dictionary that maps each column in a row to its specific data-type
	:return: A boolean flag denoting
	"""
	raw_values = line.split(",")
	if len(raw_values) <= len(schema):
		try:
			transformed_values = {}
			for (field_name, data_type), raw_val in zip(schema.items(), raw_values):
				try:
					transformed_values[field_name] = raw_val # data_type(raw_val)
				except ValueError:
					transformed_values[field_name] = None
			return True, transformed_values
		except Exception:
			return False, None
	else:
		return False, None


def transform_csv(path_to_data: Path, schema: Dict[str, Callable]) -> Iterator[Dict[str, Union[str, int, float]]]:

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


def transform_json(path_to_data: Path, schema: Dict[str, Callable]) -> Iterator[Dict[str, Union[str, int, float]]]:

	with open(path_to_data, 'r') as f: # TODO: will run into an OOM if the data is bigger than the memory
		json_obj = json.load(f)

	for raw_values_dict in json_obj:
		transformed_values = {}
		for (field_name, data_type), (_, raw_val) in zip(schema.items(), raw_values_dict.items()):
			transformed_values[field_name] = raw_val # data_type(raw_val)
		yield transformed_values