from fastapi import FastAPI

app = FastAPI()


@app.get("/item")
async def get_item():
    return {"message": "Hello World"}