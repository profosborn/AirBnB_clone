#!/usr/bin/python3
"""The module contains the class State which is a subclass of the BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Task 9.
    The class is a subclass of the Baseodel class with the
        additional public class attributes defined
        a) name: string-empty string
    """
    name = ''
