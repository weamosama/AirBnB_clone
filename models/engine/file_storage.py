# models/engine/file_storage.py

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """Class to serialize and deserialize instances to a JSON file and vice versa"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects (only if the file exists)"""
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                obj_dict = json.load(file)
            for key, value in obj_dict.items():
                class_name, obj_id = key.split('.')
                class_dict = {"BaseModel": BaseModel, "State": State, "City": City,
                              "Amenity": Amenity, "Place": Place, "Review": Review}
                obj = class_dict[class_name](**value)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
