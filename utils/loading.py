
from typing import Union, Dict

from lib.init_db import DbConnector

from lib.table_schema import PositionData, ShipEngines

from sqlalchemy import and_

def load_postion_data(vals: Dict[str, Union[str, int, float]], connector: DbConnector):

	connection = connector.get_connection()

	upds = PositionData.update().where(and_(PositionData.c.SHIP_ID == vals["SHIP_ID"],
											PositionData.c.TIMESTAMP == vals["TIMESTAMP"])).values(**vals)

	result = connection.execute(upds)

	if result.rowcount == 0:
		ins = PositionData.insert().values(**vals)
		result = connection.execute(ins)

	return True

def load_engine_data(vals: Dict[str, Union[str, int, float]], connector: DbConnector):

	connection = connector.get_connection()

	upds = ShipEngines.update().where(and_(ShipEngines.c.SHIP_ID == vals["SHIP_ID"],
											ShipEngines.c.MMSI == vals["MMSI"])).values(**vals)

	result = connection.execute(upds)

	if result.rowcount == 0:
		ins = ShipEngines.insert().values(**vals)
		result = connection.execute(ins)

	return True

