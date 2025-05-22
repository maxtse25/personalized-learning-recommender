from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class UserSkill(Base):
    __tablename__ = "user_skills"

    id = Column(Integer, primary_key=True, index=True)
    skill_name = Column(String, index=True)
    proficiency = Column(String)  # e.g. beginner, intermediate, advanced
    acquired_at = Column(DateTime(timezone=True), default=func.now())

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    url = Column(Text)
    type = Column(String)  # e.g. video, article, course
    skill_tag = Column(String, index=True)
    is_recommended = Column(Boolean, default=True)

class CareerGoal(Base):
    __tablename__ = "career_goals"

    id = Column(Integer, primary_key=True, index=True)
    goal_title = Column(String)
    description = Column(Text)
    target_date = Column(DateTime(timezone=True), nullable=True)
