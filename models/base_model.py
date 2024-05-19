#!/usr/bin/python3

"""A base model Python script."""

import models
import uuid
from datetime import datetime


class BaseModel:
    """This class is a base and defines all
    common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialization method for BaseModel.

        Arguments:
            *args: Not utilized.
            **kwargs: Arguments for initializing BaseModel.

        Attributes:
            id: Automatically generated unique identifier.
            created_at: Datetime of creation.
            updated_at: Datetime of last update.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Now should be able to save instances of BaseModel to a
        JSON file and reload them successfully
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Creates a dictionary of the class and returns
        a dictionary with all keys/values of __dict__ of the instance.
        """
        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy
