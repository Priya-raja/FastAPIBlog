from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

posts: list[dict] = [
    {
        "id":1,
        "author": "Priya Raja",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20,2025",
    },
    {
        "id":2,
        "author": "Arya Raja",
        "title": "Python is great for AI",
        "content": "All the AI libraries are supported by Python",
        "date_posted": "April 21,2025",

    },
]

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"


@app.get("/api/posts")
def get_posts():
    return posts