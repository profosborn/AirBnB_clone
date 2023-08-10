#!/usr/bin/python3
"""
    Task 6: file_storage module
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
        Task 6: class FileStorage defines private class attributes
            (a) __file_path (b)__objects
            and public instance methods
            (a) all (b) new (c) save (d) reload
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        dump = {k: val.to_dict() for k, val in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(dump))

    def reload(self):
        """
            deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exits otherwise do nothing
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                payload = f.read()
            paydict = json.loads(payload)
            for key, val in paydict.items():
                classname, obj_id = key.split(".")
                cls = eval(classname)
                FileStorage.__objects[key] = cls(**val)
