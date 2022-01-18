from fastapi import FastAPI
from app.router import auth, users,about,education
from app import models
from app.database import Base,engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware,
 allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )


models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message":"hello"}

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(about.router)
app.include_router(education.router)
