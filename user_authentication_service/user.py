#!/usr/bin/env python3
"""User Class File"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """
    -----------
    CLASS: User
    -----------
    Description:
        Creates a SQLAlchemy model for the users table.
    """
    __tablename__ = 'users'
    __table_args__ = {'comment': 'Table storing user data for authentication'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    session_id = Column(String(255), nullable=True)
    reset_token = Column(String(255), nullable=True)

    def __repr__(self):
        """String representation of the User object."""
        return f"<User(id={self.id}, email={self.email})>"
