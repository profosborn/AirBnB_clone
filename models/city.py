#!/usr/bin/python3
"""The module contains the class City, a subclass of the BaseModel class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Task 8.
    This class is a subclass of the BaseModel class with additiona
        public class attributes
        a) state_id: string - empty string: it will be the State.id
        b) name:string - empty string
    """
    state_id = ''
    name = ''
