from typing import final
from app.main import app
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},  # this is for sqlite
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def get_test_db():
    try:
        db = TestSessionLocal()
        yield db
    finally:
        db.close()


client = TestClient(app)
app.dependency_overrides[get_db] = get_test_db


# def test_user():
#     response = client.post(
#         "/user",
#         data={"username": "test@example.com", "password": "yasar"},
#         json={
#             "id": 1,
#             "email": "test@example.com",
#             "created_at": "2022-01-19T16:30:10",
#         },
#     )
#     assert response.status_code == 200
