from fastapi import FastAPI
import uvicorn
from Schema import Link, Shortened
from DataBase import LinkDB
from fastapi import HTTPException


app = FastAPI(
    title="Link Shortener Backend",
    description="A simple link shortener backend using FastAPI.",
    version="0.2",
)

db = LinkDB()


@app.get("/")
def root() -> dict[str, str]:
    """
    Root endpoint of the application.

    **Returns**:
    - *dict[str, str]*: A dictionary containing the result of the `db.show()` function.
        (i.e) the current state of the database.
    """
    return db.show()


@app.get("/link/{short_link}", response_model=Link)
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


@app.post("/link/", response_model=Shortened)
def create_link(link: Link) -> Shortened:
    """
    Create a shortened link.

    **Request Argument**:
    - link (*Link*): The original link to be shortened.

    **Returns**:
    - *Shortened*: The response containing the shortened link.

    """
    short_link = db.set(link)
    return {"short_link": short_link}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
