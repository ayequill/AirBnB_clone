import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        obj = BaseModel()
        obj_key = type(obj).__name__ + "." + obj.id
        self.storage.new(obj)
        self.assertIn(obj_key, self.storage._FileStorage__objects)

    def test_save_reload(self):
        obj1 = BaseModel()
        obj2 = User()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertIn(type(obj1).__name__ + "." + obj1.id,
                      new_storage._FileStorage__objects)
        self.assertIn(type(obj2).__name__ + "." + obj2.id,
                      new_storage._FileStorage__objects)

    def test_reload_no_file(self):
        # Ensure reload doesn't raise an exception if the file doesn't exist
        self.storage.reload()
