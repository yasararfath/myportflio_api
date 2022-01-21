from hashlib import new
from app.main import app
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
import pytest
from app.schema import user_schema

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},  # this is for sqlite
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def client():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    def get_test_db():
        try:
            db = TestSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = get_test_db
    yield TestClient(app)


@pytest.mark.parametrize(
    "email,password",
    [("test@example.com", "yasar"), ("test1@example.com", "yasar1")],
)
def test_user(client, email, password):
    response = client.post(
        "/user/",
        json={"email": email, "password": password},
    )
    new_user = user_schema.CreateUserResponse(**response.json())
    assert response.status_code == 201
    assert new_user.email == email
