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
    CursorNoneError,
)
from pymongo import MongoClient
from typing import Optional

from database.db_basetype import ConfigDB, DataBase


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
        self.conn = None
        self.datasource_settings = {}
        self.current_db = None

    def connect(self, database: Optional[str] = None):
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
        # connect to the MongoDB server
        print(f"Connecting to MongoDB database with name {database}")
        # self.current_db = self.conn[f"{database}"]
        return self.conn[f"{database}"]
    
    def execute(self, sql_command: str, values: tuple[str, ...] | None = None):...



if __name__ == "__main__":
    import datetime
    post_1 = {
        "author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.now(tz=datetime.timezone.utc),
    }
    post_2 = {
        "author": "John",
        "text": "My 2nd blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.now(tz=datetime.timezone.utc),
    }
    db = MongoDB(filename="./database/database.ini", section="mongodb")
    print(isinstance(db, DataBase))  # True
    # db = PostgresDB(filename="Asdasd") # raises error
    mongodb = db.connect("podcasts")
    print(mongodb.my_episodes.count_documents({})) # 0
    mongodb.my_episodes.insert_many([post_1])
    print(mongodb.my_episodes.count_documents({})) # 1
    print(mongodb.my_episodes.insert_many([post_2]))
    print(mongodb.my_episodes.count_documents({})) # 2
    print(mongodb.my_episodes.delete_many({}))
    print(mongodb.my_episodes.count_documents({})) # 0