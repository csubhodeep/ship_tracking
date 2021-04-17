

from sqlalchemy import (MetaData, Table, Column,
                        Integer, DateTime, Float, String,
                        PrimaryKeyConstraint, CheckConstraint)


metadata = MetaData()


# the following table is created to record the recos that user has finally bought and selected to buy
PositionData = Table('position_data',
                     metadata,
                     Column('key', Integer, nullable=False, autoincrement=True),
                     Column('TIMESTAMP', DateTime, nullable=False),
                     Column('SHIP_ID', String, nullable=False),
                     Column('LON', Float),
                     Column('LAT', Float),
                     Column('SPEED', Float),
                     Column('IMO', Integer),
                     Column('STATUS', Integer),
                     Column('COURSE', Integer),
                     Column('HEADING', Integer),
                     Column('MMSI', Integer),
                     PrimaryKeyConstraint('key'),
                     CheckConstraint("scale IN ('Alpha', 'EU')")
                     )

ShipEngines = Table('ship_engines',
                    metadata,
                    Column('key', Integer, nullable=False, autoincrement=True),
                    Column('SHIP_ID', String, nullable=False),
                    Column('MMSI', Integer),
                    Column('engine1_id', Integer),
                    Column('engine1_name', Integer),
                    Column('engine2_id', Integer),
                    Column('engine2_name', Integer),
                    Column('engine3_id', Integer),
                    Column('engine3_name', Integer),
                    PrimaryKeyConstraint('key'),
                    CheckConstraint("scale IN ('Alpha', 'EU')")
                    )

ShipOwner = Table('ship_owner',
                  metadata,
                  Column('key', Integer, nullable=False, autoincrement=True),
                  Column('SHIP_ID', String, nullable=False),
                  Column('owner', String, nullable=False),
                  )



