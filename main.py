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

