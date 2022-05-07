from dataclasses import dataclass
from typing import Any, Mapping
from pymongo import MongoClient, errors
from pymongo.database import Database
from pymongo.collection import Collection
from dotenv import dotenv_values


@dataclass
class PymongoDatabase:
    DB: Database

    def document(self, collection_name: str, schema: dict) -> Mapping[str, Any] | Collection | None:
        try:
            self.DB.command("collmod", collection_name, validator=schema)
        except errors.OperationFailure as e:
            return e.details
        return self.DB[collection_name]

config = dotenv_values(".env")
client = MongoClient(config["DB_URL"])
microblog_db = PymongoDatabase(client.microblog)
