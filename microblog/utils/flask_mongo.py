from dataclasses import dataclass
from pymongo.database import Database
from pymongo.collection import Collection



@dataclass
class PymongoDB_Collection:
    database : Database

    def collection_doc(self, name: str, schema: dict) -> Collection:
        db = self.database
        db.command("collMod", name, validator=schema)

        collection = db[name]

        return collection       
        