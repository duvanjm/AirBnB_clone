#!/usr/bin/python3


""" Hbnb project - test Cases - User

"""


import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from datetime import datetime
import pep8
import os
from os import path


class TestReview(unittest.TestCase):
    """ Test cases for user.py
    """

    @classmethod
    def setUp(self):
        """ Setting up before start all cases
        """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        FileStorage._FileStorage__objects = {}

    def test_pep8(self):
        """ PEP 8 validation
        """
        pep8_style = pep8.StyleGuide(quiet=True)
        pep8_result = pep8_style.check_files(['models/user.py'])
        self.assertEqual(pep8_result.total_errors, 0, "fix pep8")

    def test_doc(self):
        """ Check for documentation
        """
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)

    def test_init(self):
        """ Review all the class and BaseModel attributes
        """
        my_class = User()
        self.assertTrue(hasattr(my_class, "email"))
        self.assertTrue(hasattr(my_class, "password"))
        self.assertTrue(hasattr(my_class, "first_name"))
        self.assertTrue(hasattr(my_class, "last_name"))
        self.assertIsInstance(my_class, User)
        self.assertTrue(type(my_class.updated_at) is datetime)
        self.assertTrue(type(my_class.created_at) is datetime)

    def test_init_kwargs(self):
        """ Review all the class and BaseModel attributes using Kwargs
        """
        obj = {"updated_at": "2020-06-30T23:36:25.091664",
               "created_at": "2020-06-30T23:36:25.091664",
               "__class__": "User",
               "id": "77822a4e-7aa5-4bb9-871c-5d32f34080e0",
               "email": "hbnb@holb.com",
               "password": "12345",
               "first_name": "Betty",
               "last_name": "Holberton"}
        my_class = User(**obj)
        self.assertTrue(hasattr(my_class, "email"))
        self.assertTrue(hasattr(my_class, "password"))
        self.assertTrue(hasattr(my_class, "first_name"))
        self.assertTrue(hasattr(my_class, "last_name"))
        self.assertIsInstance(my_class, User)
        self.assertTrue(type(my_class.updated_at) is datetime)
        self.assertTrue(type(my_class.created_at) is datetime)

    def test_heritage(self):
        """ check it is a subclass of BaseModel
        """
        my_class = User()
        self.assertTrue(issubclass(type(my_class), BaseModel))

    def test_str(self):
        """ review format: [<class name>] (<self.id>) <self.__dict__>
        """
        my_class = User()
        string = "[{:s}] ({:s}) {}".format(my_class.__class__.__name__,
                                           my_class.id, my_class.__dict__)
        self.assertEqual(string, my_class.__str__())

    def test_todict(self):
        """ review the dictionary representation of an object
        """
        obj = {"updated_at": "2020-06-30T23:36:25.091664",
               "created_at": "2020-06-30T23:36:25.091664",
               "__class__": "User",
               "id": "77822a4e-7aa5-4bb9-871c-5d32f34080e0",
               "email": "hbnb@holb.com",
               "password": "12345",
               "first_name": "Betty",
               "last_name": "Holberton"}
        my_class = User(**obj)
        my_dict = my_class.to_dict()
        for k, v in obj.items():
            self.assertTrue(k in my_dict)
            self.assertEqual(my_dict[k], v)

    def test_update_time(self):
        """ check if updated_at changes
        """
        my_class = User()
        old_updated_time = my_class.updated_at
        my_class.save()
        self.assertNotEqual(old_updated_time, my_class.updated_at)


if __name__ == "__main__":
    unittest.main()
