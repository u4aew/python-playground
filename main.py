import uvicorn
from fastapi import FastAPI
from db.base import databases

app = FastAPI()

@app.get('/')
def home():
    return {"Hello": "World"}

@app.on_event("startup")
async def startup():
    await databases.connect()

@app.on_event("shutdown")
async def shutdown():
    await databases.disconnect()

if __name__ == '__main__':
     uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)