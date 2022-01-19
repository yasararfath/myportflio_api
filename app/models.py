from sqlalchemy import Integer, String, Column, ForeignKey
from app.database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class User(Base):
    __tablename__ = "user"

    id = Column(Integer,primary_key=True)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("CURRENT_TIMESTAMP"))

class About(Base):
    __tablename__ = "about"

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    designation = Column(String,nullable=False)
    email = Column(String,nullable=False)
    phone = Column(String,nullable=False)
    website = Column(String,nullable=False)
    location = Column(String,nullable=False)
    objective = Column(String,nullable=True)
    user_id = Column(Integer,ForeignKey("user.id", ondelete="CASCADE"),nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
        nullable=True,server_default=text("CURRENT_TIMESTAMP"))


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
    user_id = Column(Integer,ForeignKey("user.id", ondelete="CASCADE"),nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
        nullable=True,server_default=text("CURRENT_TIMESTAMP"))

class Experience(Base):
    __tablename__ = "experience"

    id = Column(Integer,primary_key=True)
    designation = Column(String,nullable=False)
    company_name = Column(String,nullable=False)
    start_year = Column(Integer,nullable=False)
    end_year = Column(Integer,nullable=False)
    description = Column(String,nullable=True)
    location = Column(String,nullable=False)
    user_id = Column(Integer,ForeignKey("user.id", ondelete="CASCADE"),nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
        nullable=True,server_default=text("CURRENT_TIMESTAMP"))

class Skills(Base):
    __tablename__ = "skills"

    id = Column(Integer,primary_key=True)
    skill_name = Column(String,nullable=False)
    skill_type = Column(String,nullable=False)
    user_id = Column(Integer,ForeignKey("user.id", ondelete="CASCADE"),nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
        nullable=True,server_default=text("CURRENT_TIMESTAMP"))

class Projects(Base):
    __tablename__ = "projects"

    id = Column(Integer,primary_key=True)
    project_name = Column(String,nullable=False)
    description = Column(String,nullable=False)
    url = Column(String,nullable=False)
    user_id = Column(Integer,ForeignKey("user.id", ondelete="CASCADE"),nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
        nullable=True,server_default=text("CURRENT_TIMESTAMP"))

class Certification(Base):
    __tablename__ = "certification"

    id = Column(Integer,primary_key=True)
    certificate_name = Column(String,nullable=False)
    issue_by = Column(String,nullable=False)
    expire_year = Column(String,nullable=True)
    description = Column(String,nullable=True)
    url = Column(String,nullable=False)
    user_id = Column(Integer,ForeignKey("user.id", ondelete="CASCADE"),nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
        nullable=True,server_default=text("CURRENT_TIMESTAMP"))


class Connect(Base):
    __tablename__ = "connect"

    id = Column(Integer,primary_key=True)
    connect_name = Column(String,nullable=False)
    image_url = Column(String,nullable=False)
    url = Column(String,nullable=False)   
    user_id = Column(Integer,ForeignKey("user.id", ondelete="CASCADE"),nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
        nullable=True,server_default=text("CURRENT_TIMESTAMP"))


