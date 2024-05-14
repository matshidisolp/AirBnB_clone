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


