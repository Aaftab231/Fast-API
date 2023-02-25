from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

class Blog(BaseModel):
    title: str
    description: Optional[str]
    published: bool
    author: str
    tax: float


app = FastAPI()

@app.get("/")
def index():
    return {
        "data": {
        "message": "data returned from fastapi"
    }}

@app.get("/about")
def about():
    return {
        "data": {
        "name": "About fastapi page"
    }}

@app.get("/blog/")
def show_blog(limit=10, sort:Optional[str] = None, published: bool=False):
    if published:
        return {
            "msg": f"fetch {limit} blogs from published db"
        }
    else:
        return {
            "msg": "All blogs are unpublished"
        }

@app.get("/blog/unpublished")
def show_unpublished():
    return {
        "msg": "All unpublished blogs are unpublished"
    }

@app.get("/blog/{id}")
def show(id: int):
    return {
        "msg": {"data": id}
    }



@app.get("/blog/{id}/comments")
def show_comment(id, limit=10):
    return {
        "msg":{
                "comments": id,
                "data": id + " comments with limit " + limit
        }
    }

@app.post("/blog/")
def post_comment(request: Blog):
    return{
        "msg": f"Title of blog is {request.title}"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9000)
