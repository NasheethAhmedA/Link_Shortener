from fastapi import APIRouter, Response, status, HTTPException
from Schema import Link, Shortened
from DataBase import LinkDB
from dotenv import dotenv_values
import validators

config = dotenv_values(".env")

router = APIRouter()

db = LinkDB()


@router.get("/", response_model=dict[str, str])
def root(response: Response, Admin_Token: str = "") -> dict[str, str]:
    """
    Root endpoint of the application.

    **Parameters**:
    - *response (Response)*: The response object to set the status code if needed.
    - *Admin_Token (str, optional)*: The token used for admin validation. Defaults to an empty string.

    **Returns**:
    - *dict[str, str]*: A dictionary containing the result of the `db.show()` function, which represents the current state of the database.

    **Raises**:
    - *HTTPException*: If the provided Admin_Token is invalid, a 403 Forbidden status code is returned with a message.
    """
    if Admin_Token == config["ADMIN_VALIDATION_TOKEN"]:
        return db.show()
    else:
        response.status_code = status.HTTP_403_FORBIDDEN
        return {"message": "Forbidden"}


@router.get("/{short_link}", response_model=Link)
def get_original_link(short_link: str) -> Link:
    """
    Retrieve the original link associated with the given short link.

    **Parameters**:
    - short_link (*str*): The short link to retrieve the original link for.

    **Returns**:
    - *Link*: The original link associated with the given short link.

    **Raises**:
    - HTTPException: If the link is not found, returns a *404 error*.
    """
    link = db.get(short_link)
    if link:
        return link
    else:
        raise HTTPException(status_code=404, detail="Link not found")


@router.post("/", response_model=Shortened)
def create_link(link: Link) -> Shortened:
    """
    Create a shortened link.

    **Request Argument**:
    - link (*Link*): The original link to be shortened.

    **Returns**:
    - *Shortened*: The response containing the shortened link.

    """
    if not validators.url(link.url):
        raise HTTPException(status_code=400, detail="Invalid URL")
    short_link = db.set(link)
    return {"short_link": short_link}
