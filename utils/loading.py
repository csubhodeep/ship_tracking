from typing import Union, Dict

from sqlalchemy import and_

from lib.init_db import DbConnector
from lib.table_schema import PositionData, ShipEngines, ShipOwner, EngineTechSpecs


def load_postion_data(vals: Dict[str, Union[str, int, float]], connector: DbConnector):
    """This function loads the position details of a vessel into its respective table in the DB
    :param vals: the row-tuple containing all the values
    :param connector: the class to connect to the DB
    """
    connection = connector.get_connection()

    upds = PositionData.update().where(and_(PositionData.c.SHIP_ID == vals["SHIP_ID"],
                                            PositionData.c.TIMESTAMP == vals["TIMESTAMP"])).values(**vals)

    result = connection.execute(upds)

    if result.rowcount == 0:
        ins = PositionData.insert().values(**vals)
        result = connection.execute(ins)


def load_engine_data(vals: Dict[str, Union[str, int, float]], connector: DbConnector):
    """This function loads the engine details of a vessel into its respective table in the DB
    :param vals: the row-tuple containing all the values
    :param connector: the class to connect to the DB
    """
    connection = connector.get_connection()

    upds = ShipEngines.update().where(and_(ShipEngines.c.SHIP_ID == vals["SHIP_ID"],
                                           ShipEngines.c.MMSI == vals["MMSI"])).values(**vals)

    result = connection.execute(upds)

    if result.rowcount == 0:
        ins = ShipEngines.insert().values(**vals)
        result = connection.execute(ins)


def load_owner_data(vals: Dict[str, str], connector: DbConnector):
    """This function loads the owner details of a vessel into its respective table in the DB
    :param vals: the row-tuple containing all the values
    :param connector: the class to connect to the DB
    """
    connection = connector.get_connection()

    ins = ShipOwner.insert().values(**vals)
    result = connection.execute(ins)


def load_engine_tech_specs(vals: Dict[str, str], connector: DbConnector):
    """This function loads the engine-tech-spec details of a vessel into its respective table in the DB
    :param vals: the row-tuple containing all the values
    :param connector: the class to connect to the DB
    """
    connection = connector.get_connection()

    ins = EngineTechSpecs.insert().values(**vals)
    result = connection.execute(ins)
