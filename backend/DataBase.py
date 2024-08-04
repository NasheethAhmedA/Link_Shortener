from pydantic import BaseModel
from Schema import Link
from utils import LinkHash
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import dotenv_values

env_values = dotenv_values(".env")

URI = env_values["MONGO_URI"]

client = MongoClient(URI, server_api=ServerApi("1"))


class LinkDB(BaseModel):
    """
    Database to store shortened links
    Currently using MongoDB as the database
    """

    def shorten(self, link: Link) -> str:
        return LinkHash(link.url)

    def set(self, value: Link) -> str:
        key = self.shorten(value)
        client.short.link.update_one({"hash": "table"}, {"$set": {key: value.url}})
        return key

    def get(self, key: str) -> Link:
        lookup_data = client.short.link.find_one()
        if key in lookup_data:
            return {"url": lookup_data.get(key)}
        return None

    def delete(self, key: str):
        client.short.link.update_one({"hash": "table"}, {"$unset": {key: ""}})

    def show(self):
        all = client.short.link.find_one()
        all.pop("_id")
        all.pop("hash")
        return all
