from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime

app = FastAPI()

postdb = []

class Post(BaseModel):
    id: int
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: datetime
    published: Optional[bool] = False

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/blog")
async def get_posts():
    return postdb

@app.post("/blog")
async def add_post(post: Post):
    postdb.append(post.dict())
    return postdb[-1]

@app.get("/blog/{post_id}")
async def get_post(post_id: int):
    post = post_id - 1
    return postdb[post]

@app.post("/blog/{post_id}")
async def update_post(post_id: int, post: Post):
    postdb[post_id - 1] = post
    return {"message": "Post has been updated succesfully"}

@app.delete("/blog/{post_id}")
async def delete_post(post_id: int):
    postdb.pop(post_id - 1)
    return {"message": "Post has been deleted succesfully"}