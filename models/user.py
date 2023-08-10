#!/usr/bin/python3
"""This module contains the class User which is a subclass of BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Task 8.
    This class is a subclass of the BaseModel class with the
        additional attributes
        a. email: string - empty string
        b. password: string - empty string
        c. first_name: stirng - empty string
        d. last_name: string - empty string
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
