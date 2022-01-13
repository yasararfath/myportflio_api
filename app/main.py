from fastapi import FastAPI
from app.router import auth, users
from app import models
from app.database import Base,engine

app = FastAPI()


models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return "hello"

app.include_router(auth.router)
app.include_router(users.router)

