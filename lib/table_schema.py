from sqlalchemy import (MetaData, Table, Column,
                        Integer, DateTime, Float, String,
                        PrimaryKeyConstraint)

metadata = MetaData()

PositionData = Table('position_data',
                     metadata,
                     Column('key', Integer, nullable=False, autoincrement=True),
                     Column('SHIP_ID', String),
                     Column('TIMESTAMP', DateTime, nullable=False),
                     Column('SPEED', Float),
                     Column('LON', Float),
                     Column('LAT', Float),
                     Column('IMO', Integer),
                     Column('STATUS', Integer),
                     Column('COURSE', Integer),
                     Column('HEADING', Integer),
                     Column('MMSI', Integer),
                     PrimaryKeyConstraint('key'),
                     )

ShipEngines = Table('ship_engines',
                    metadata,
                    Column('key', Integer, nullable=False, autoincrement=True),
                    Column('MMSI', Integer),
                    Column('SHIP_ID', String),
                    Column('engine1_id', String),
                    Column('engine1_name', String),
                    Column('engine2_id', String),
                    Column('engine2_name', String),
                    Column('engine3_id', String),
                    Column('engine3_name', String),
                    PrimaryKeyConstraint('key'),
                    )

ShipOwner = Table('ship_owner',
                  metadata,
                  Column('key', Integer, nullable=False, autoincrement=True),
                  Column('SHIP_ID', String, nullable=False),
                  Column('owner', String, nullable=False),
                  PrimaryKeyConstraint('key'),
                  )

EngineTechSpecs = Table('engine_tech_specs',
                        metadata,
                        Column('key', Integer, nullable=False, autoincrement=True),
                        Column('source_page', String),
                        Column('Engine Model', String),
                        Column('Minimum Rating', String),
                        Column('Maximum Rating', String),
                        Column('Voltage', String),
                        Column('Frequency', String),
                        Column('Speed', String),
                        PrimaryKeyConstraint('key'),
                        )
