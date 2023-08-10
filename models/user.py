#!/usr/bin/python3
"""This module contains the class User which is a subclass of BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Task 8.
    This class is a subclass of the BaseModel class with the
        additional attributes
        a. email
        b. password
        c. first_name
        d. last_name
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
