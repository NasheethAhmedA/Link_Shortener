from pydantic import BaseModel


class Link(BaseModel):
    """
    Represents a link object.

    Attributes:
        url (str): The URL of the link.
    """

    url: str


class Shortened(BaseModel):
    """
    Represents a shortened link.

    Attributes:
        short_link (str): The shortened link.
    """

    short_link: str
