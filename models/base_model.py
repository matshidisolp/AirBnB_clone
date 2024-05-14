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

