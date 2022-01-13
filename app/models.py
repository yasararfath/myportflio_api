from sqlalchemy import Integer, String, Column
from app.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer,primary_key=True)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=True)

class About(Base):
    __tablename__ = "about"

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    designation = Column(String,nullable=False)
    email = Column(String,nullable=False)
    phone = Column(String,nullable=False)
    location = Column(String,nullable=False)
    objective = Column(String,nullable=True)

class Education(Base):
    __tablename__ = "education"

    id = Column(Integer,primary_key=True)
    school_name = Column(String,nullable=False)
    grade = Column(Integer,nullable=False)
    out_of = Column(Integer,nullable=False)
    degree = Column(String,nullable=False)
    start_year = Column(Integer,nullable=False)
    end_year = Column(Integer,nullable=False)
    location = Column(String,nullable=False)
    description = Column(String,nullable=True)

class Experience(Base):
    __tablename__ = "experience"

    id = Column(Integer,primary_key=True)
    designation = Column(String,nullable=False)
    company_name = Column(String,nullable=False)
    start_year = Column(Integer,nullable=False)
    end_year = Column(Integer,nullable=False)
    description = Column(String,nullable=True)
    location = Column(String,nullable=False)

class Skills(Base):
    __tablename__ = "skills"

    id = Column(Integer,primary_key=True)
    skill_name = Column(String,nullable=False)
    skill_type = Column(String,nullable=False)

class Projects(Base):
    __tablename__ = "projects"

    id = Column(Integer,primary_key=True)
    project_name = Column(String,nullable=False)
    description = Column(String,nullable=False)
    url = Column(String,nullable=False)

class Certification(Base):
    __tablename__ = "certification"

    id = Column(Integer,primary_key=True)
    certificate_name = Column(String,nullable=False)
    issue_by = Column(String,nullable=False)
    expire_year = Column(String,nullable=True)
    description = Column(String,nullable=True)
    url = Column(String,nullable=False)


class Connect(Base):
    __tablename__ = "connect"

    id = Column(Integer,primary_key=True)
    connect_name = Column(String,nullable=False)
    image_url = Column(String,nullable=False)
    url = Column(String,nullable=False)   

