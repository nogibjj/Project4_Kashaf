from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki
from mylib.logic import wiki as wikilogic
from mylib.logic import phrase as wikiphrases
from mylib.logic import wikiurl as wikiurl
from mylib.logic import wikititle as wikititle
from mylib.logic import wikicontent as wikicontent


app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello, welcome to my Wikipedia API.  Call /search or /wiki or /phrase"
    }


@app.get("/search/{value}")
async def search(value: str):
    """Page to search in wikipedia"""

    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve wikipedia page"""

    result = wikilogic(name)
    return {"result": result}


@app.get("/phrase/{name}")
async def phrase(name: str):
    """Retrieve wikipedia page and return phrases"""

    result = wikiphrases(name)
    return {"result": result}


@app.get("/url/{name}")
async def url(name: str):
    """Retrieve wikipedia url"""

    result = wikiurl(name)
    return {"result": result}


@app.get("/title/{name}")
async def title(name: str):
    """Retrieve wikipedia title"""

    result = wikititle(name)
    return {"result": result}


@app.get("/content/{name}")
async def content(name: str):
    """Retrieve wikipedia content"""

    result = wikicontent(name)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
