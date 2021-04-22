import json
from datetime import datetime
from pathlib import Path
from typing import Dict
from typing import Iterator
from typing import List
from typing import Tuple
from typing import Union


def transform_row(line: str, columns: List[str]) -> Tuple[bool, Union[None, Dict[str, Union[str, int, float]]]]:
    """This function organizes (and casts) the data present in each row
    :param line: a line in the CSV file
    :param columns: A list of field names that we wish to load the values for
    :return: A boolean flag denoting the success of transformation
    """
    raw_values = line.split(",")
    try:
        transformed_values = {}
        for col, raw_val in zip(columns, raw_values):
            transformed_values[col] = raw_val if col != "TIMESTAMP" else datetime.strptime(raw_val, "%Y-%m-%d %H:%M:%S")
        return True, transformed_values
    except Exception:
        return False, None


def transform_csv(path_to_data: Path, columns: List[str]) -> Iterator[Dict[str, Union[str, int, float]]]:
    """This function is a generator that yields transformed rows of a CSV file
    :param path_to_data: path to the file
    :param columns: A list of field names that we wish to load the values for
    :return: one transformed row
    """
    with open(path_to_data, 'r') as f:  # TODO: will run into an OOM if the data is bigger than the memory
        for line_no, line in enumerate(f):
            if line_no:
                is_sucessful, vals = transform_row(line, columns)
                if is_sucessful:
                    yield vals
                else:
                    pass
            else:
                pass


def transform_json(path_to_data: Path, columns: List[str]) -> Iterator[Dict[str, Union[str, int, float]]]:
    """This function is a generator that yields transformed rows from a multi-line JSON
    :param path_to_data: path to the file
    :param columns: A list of field names that we wish to load the values for
    :return: one transformed row
    """
    with open(path_to_data, 'r') as f:  # TODO: will run into an OOM if the data is bigger than the memory
        json_obj = json.load(f)

    for raw_values_dict in json_obj:
        if raw_values_dict:
            transformed_values = {}
            for col in columns:
                try:
                    transformed_values[col] = raw_values_dict[col] if col != "TIMESTAMP" else datetime.strptime(
                        raw_values_dict[col], "%Y-%m-%dT%H:%M:%S")
                except KeyError:
                    transformed_values[col] = None
            yield transformed_values
        else:
            yield None


def transform_ship_owner(path_to_data: Path) -> Iterator[Dict[str, str]]:
    """This transforms the ship-owner data into a meaningful schema.
    :param path_to_data: path to the file
    :return: one transformed row
    """
    with open(path_to_data, 'r') as f:
        for line_no, line in enumerate(f):
            if line_no:
                for i, ship_id in enumerate(line.split(",")):
                    if ship_id:
                        yield {"owner": owners[i], "SHIP_ID": ship_id}
                    else:
                        yield None
            else:
                owners = line.split(",")
