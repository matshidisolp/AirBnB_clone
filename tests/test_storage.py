import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_initialization(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_all_method(self):
        self.assertEqual(self.storage.all(), {})

        # Adding objects to storage
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        
        self.assertEqual(len(self.storage.all()), 2)

    def test_new_method(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(len(self.storage.all()), 1)

        # Check if object is correctly added
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save_method(self):
        # Adding objects to storage
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)

        # Save objects to file
        self.storage.save()

        # Check if file exists
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

        # Check if file is not empty
        self.assertTrue(os.path.getsize(FileStorage._FileStorage__file_path) > 0)

    def test_reload_method(self):
        # Adding objects to storage
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        # Clear storage and reload from file
        self.storage._FileStorage__objects = {}
        self.storage.reload()

        # Check if objects are reloaded
        self.assertEqual(len(self.storage.all()), 2)

        # Check if objects are instances of BaseModel
        for obj in self.storage.all().values():
            self.assertIsInstance(obj, BaseModel)


if __name__ == "__main__":
    unittest.main()
