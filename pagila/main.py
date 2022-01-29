from fastapi import FastAPI
from routers import actors, films

app = FastAPI()
app.include_router(actors.router)
app.include_router(films.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
