from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {
        'data': { 'message': 'Hello, World 2' }
        }

@app.get("/about")
async def about():
    return {'data': { 'message': 'About'  }}