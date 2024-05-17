#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON
    file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    """Define a dictionary of classes to manage dynamic class creation"""
    __class_map = {
        "BaseModel": BaseModel,
        "User": User
    }

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objs = {}
        for key, value in FileStorage.__objects.items():
            serialized_objs[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                objs = json.load(file)
                for key, value in objs.items():
                    class_name, obj_id = key.split('.')
                    obj_dict = {k: v for k, v in value.items()}
                    obj_dict['__class__'] = class_name
                    self.new(eval(class_name)(**obj_dict))
        except FileNotFoundError:
            pass
