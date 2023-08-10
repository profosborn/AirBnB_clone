#!/usr/bin/python3
"""
    TASK 3: base_model module
    The module defines the BaseModel class
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Task 3: The BaseModel class defines all common attributes/methods
        for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Task 3: The constructor for the BaseModel class that initializes
            the public instances
            a) id
            b) created_at
            c) updated_at
        Task 4: Updating the constructor arguments to account for *args
            and kwargs. kwargs if present would be used to create a new
            instance of the BaseModel instead.
        """
        if kwargs:
            kwargs.pop('__class__', None)
            kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'],
                    "%Y-%m-%dT%H:%M:%S.%f"
                    )
            kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'],
                    "%Y-%m-%dT%H:%M:%S.%f"
                    )
            for key, val in kwargs.items():
                setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Task 3: overriding the toString method"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """
        Task 3: updates the public instance attribute updated_at with
            the current datetime.
        """
        models.storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        task 3: returns a dictionary containing all keys/values of __dict__
            of the current BaseModel instance
        """
        my_dict = {}
        for key, val in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                my_dict[key] = val.isoformat()
            elif key == "number":
                my_dict["my_number"] = val
            else:
                my_dict[key] = val
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
