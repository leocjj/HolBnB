#!/usr/bin/python3
""" BaseModel class. Used as base for future classes."""
from datetime import datetime
from uuid import uuid4


class BaseModel():
	def __init__(self, *args, **kwargs ):
		"""Validate non interactive and init method
		"""
		if len(kwargs) is not 0:
			for key, value in kwargs.items():
				if key == "id":
					self.id = kwargs.get(key)
				if key == "created_at":
					self.created_at = datetime.strptime(kwargs.get(key),
														'%Y-%m-%dT%H:%M:%S.%f')
				if key == "updated_at":
					self.updated_at = datetime.strptime(kwargs.get(key),
														'%Y-%m-%dT%H:%M:%S.%f')
		else:
			self.id = str(uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()

	def __str__(self):
		"""Return the string representation
		"""
		return ("[{}] ({}) {}".format(self.__class__.__name__,
									self.id, self.__dict__))

	def save(self):
		"""Update date
		"""
		self.updated_at = datetime.now()

	def to_dict(self):
		""" Return the dictionary 
		"""
		_dict = self.__dict__.copy()
		_dict['created_at'] = self.created_at.isoformat()
		_dict['updated_at'] = self.updated_at.isoformat()
		_dict['__class__'] = self.__class__.__name__
		return(_dict)
