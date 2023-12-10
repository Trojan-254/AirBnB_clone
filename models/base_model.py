#!/usr/bin/python3
"""The base module"""

import uuid
import datetime

class BaseModel():
    """The base model of all the classes"""

    def __init__(self, *args, **kwargs):
        """The class initializer"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns a string representation of aclass object"""
        return f"[{self.__class__.__name__}]({self.id}) {self.__dict__}"
    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns the dictionary representation of 
        all key/value of __dict__ of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__

        return obj_dict
