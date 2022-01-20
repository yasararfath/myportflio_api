from cmath import exp
from fastapi import FastAPI
from app.router import (
    auth,
    users,
    about,
    education,
    experience,
    projects,
    certification,
    connect,
)
from app import models
from app.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


models.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Check out /docs for portfolio api in Swagger UI"}


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(about.router)
app.include_router(education.router)
app.include_router(experience.router)
app.include_router(projects.router)
app.include_router(certification.router)
app.include_router(connect.router)
