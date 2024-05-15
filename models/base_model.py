#!/usr/bin/python3

"""a base model python script"""

import uuid
from datetime import datetime


class BaseModel:
    """This class is a base and defines all
    common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initialization method for BaseModel
            Arguments:
                Args: Not utilized
                kwargs: arguments for initializing BaseModel

            Attributes:
                id: automatically generated unique identifier
                create_at: datetime of creation
                updated_at: datetime of last update
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
        """String representation of the BaseModel instance
        returns a string of class, name, id, and dictionary
        """
        return ("[{}] ({}) {}".format(
          self.__class__.__name__,
          self.id,
          self.__dict__
          ))

    def save(self):
        """Updates the instance attribute updated_at
          with the current date and time."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Creates a dictionary of the class and returns
          a dictionary with all keys/values of __dict__ of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
