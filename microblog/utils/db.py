from dataclasses import dataclass, field
from flask import Flask
from pymongo import MongoClient
from pymongo.database import Database



@dataclass
class PymongoDB_Flask:
    """A class to initialize mongodb database and get/create collections

    Returns:
        _type_: PymongoDB_Flask
    """
    app: Flask
    __client: MongoClient = field(init=False, default=None)
    __database: Database = field(init=False, default=None)

    def __post_init__(self) -> None:
        """get db config variables from the app and get mongo client
        """
        MONGO_URI = self.app.config['MONGO_URI']
        DATABASE = self.app.config['DATABASE']
        self.__client = MongoClient(MONGO_URI, tz_aware=True)
        self.__database = self.__client[DATABASE]

    @property
    def database(self) -> Database:
        """Gets the database

        Returns:
            Database: A mongob database
        """
        return self.__database

def init_db(app:Flask):
    "Initialize the app to set up all db config"    
    flask_mongodb = PymongoDB_Flask(app)
    app.db = flask_mongodb.database