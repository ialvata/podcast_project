"""
This module is responsible for defining everything related to databases, at a lower level than
the ORM design pattern.
I would usually separate into different modules the parent class from the subclasses, but in
this situation the number of code lines is too few to justify it...
"""
from configparser import ConfigParser
from database.exceptions import (
    ConfigEmptyError,
    ConfigFormatError,
    ConnectFirstError,
)
from pymongo import MongoClient, DESCENDING,ASCENDING
from typing import Optional,Any

from database.db_basetype import ConfigDB, DataBase
from pymongo.database import Database as PyMongo_Database
from pymongo.errors import BulkWriteError

#####################                 Decorators                   ############################
def check_connection(class_method):
    """
    Decorator to check whether we've established a connection to a MongoDB database, or not.
    """
    def wrapper(*args, **kwargs):
        if not isinstance(args[0].conn, MongoClient):
            raise ConnectFirstError()
        else:
            class_method(*args, **kwargs)
        
    return wrapper

class MongoDB:
    type = "mongodb"

    def __init__(
        self,
        config: ConfigDB | None = None,
        filename: str | None = None,
        section: str | None = "mongodb",
    ):
        """
        Class responsible for all the operations on the MongoDB database.
        It will try to be hide all the implementation details of MongoDB.
        """
        self.filename = filename
        self.section = section
        if self.filename is not None and self.section is not None:
            # create a parser
            parser = ConfigParser()
            # read config file
            parser.read(self.filename)

            # get section, default to mongodb
            config_dict = {}
            if parser.has_section(self.section):
                params = parser.items(self.section)
                for param in params:
                    config_dict[param[0]] = param[1]
            else:
                raise ConfigFormatError(section=self.section, filename=self.filename)
            config_dict: dict[str, str]
            self.config = ConfigDB(**config_dict)
        if config is not None:
            self.config = config
        if not hasattr(self, "config"):
            raise ConfigEmptyError
        self.conn = None  # type: ignore
        self.datasource_settings = {}
        self.current_db = None

    def connect(self) -> None:
        """
        Connect to the MongoDB database server

        Parameters
        ----------
            database: str
                A string representing the name of the MongoDB database to which we 
                want to connect.

        ## Example usage:
        database = MongoDB(filename="./db/database.ini", section="mongodb")
        database.connect("my_database")
        """
        try:
            self.conn = MongoClient(
                f'mongodb://{self.config.user}:{self.config.password}@{self.config.host}'
                f':{self.config.port}/'
            )
        except Exception as error: # to be altered
            print(error)
            raise error
    
    def execute(self, sql_command: str, values: tuple[str, ...] | None = None):...
    
    @check_connection
    def send_files(self, database:str, collection:str, list_files:list[dict[str,Any]]):
        self.conn:MongoClient
        self.current_db = PyMongo_Database(client= self.conn, name= database)
        if list_files == []:
            print(
                "No document to send to MongoDB"
                f" or some documents are already in MongoDB {self.current_db.name}.{collection}"
            )
        self.current_db.get_collection(collection).create_index(
            [("episode_url", DESCENDING)], unique = True
        )
        print(
            f"We have {self.current_db.get_collection(collection).count_documents({})}"
            f" documents in MongoDB {self.current_db.name}.{collection}"
        )
        try:
            self.current_db.get_collection(collection).insert_many(list_files)
            print(
                f"We have {self.current_db.get_collection(collection).count_documents({})}"
                f" documents in MongoDB {self.current_db.name}.{collection}"
            )
        except BulkWriteError as error:
            # pymongo throws an error on 1st doc to create a write clash,
            # so data after index may not have been added yet.
            index_already_in_db = error.details["writeErrors"][0]["index"]
            # recursive call to send remaining data.
            self.send_files(database, collection, list_files[index_already_in_db+1:])




if __name__ == "__main__":
    import datetime
    post_1 = {
        "episode_url": "mike.com",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.now(tz=datetime.timezone.utc),
    }
    post_2 = {
        "episode_url": "john.com",
        "text": "My 2nd blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.now(tz=datetime.timezone.utc),
    }
    db = MongoDB(filename="./database/database.ini", section="mongodb")
    print(isinstance(db, DataBase))  # True
    db.connect()
    db.send_files(database="test_database",collection="episodes",
                  list_files= [post_1,post_1, post_2])
    print("OLA")
    # print(mongodb.my_episodes.delete_many({}))
    # print(mongodb.my_episodes.count_documents({})) # 0