from pydantic import BaseModel
from Schema import Link
import random


class LinkDB(BaseModel):
    """
    Temporary database to store shortened links
    Will be replaced with a proper database in the future
    Something like Redis or MongoDB
    """

    data: dict[str, str] = {}

    def shorten(self, link: Link) -> str:
        return "".join(
            [
                random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
                for s in range(5)
            ]
        )

    def set(self, value: Link) -> str:
        key = self.shorten(value)
        while self._exists(key):
            key = self.shorten(value)
        self.data[key] = value.url
        return key

    def get(self, key: str) -> Link:
        if self._exists(key):
            return {"url": self.data.get(key)}
        return None

    def delete(self, key: str):
        if self._exists(key):
            del self.data[key]

    def show(self):
        return self.data

    def _exists(self, key: str):
        return key in self.data
