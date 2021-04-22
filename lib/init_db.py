import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from utils.configs import PATH_TO_DATA_FOLDER


class DbConnector:
    """This class abstracts the connectivity with the DB"""

    def __init__(self,
                 user_id: str = "abcd",
                 password: str = "abcd",
                 dialect: str = "sqlite",
                 driver: str = "psycopg2",
                 port: int = 5432,
                 host: str = "0.0.0.0",
                 db_name: str = "ship_data"):
        self._session = None
        self._user_id = os.getenv('TRACKING_DB_USER', user_id)
        self._password = os.getenv('TRACKING_DB_PASSWORD', password)
        self._engine = None
        self._session = None
        self._dialect = dialect
        self._driver = driver
        self._port = port
        self._host = os.getenv('TRACKING_DB_HOST', host)
        self._db_name = db_name
        self._conn = None

    def get_engine(self):
        if not self._engine:
            if self._dialect == "sqlite":
                link = f"{self._dialect}:////{PATH_TO_DATA_FOLDER}/{self._db_name}.db"
            else:
                link = f"{self._dialect}+{self._driver}://{self._user_id}:{self._password}@{self._host}:{self._port}/{self._db_name}"
            self._engine = create_engine(link)

        return self._engine

    def _get_session(self):
        if not self._session:
            if not self._engine:
                self.get_engine()
            self._session = Session(bind=self._engine,
                                    autocommit=True)

    def get_connection(self):
        if not self._conn:
            if not self._session:
                self._get_session()
            self._conn = self._session.connection()

        return self._conn
