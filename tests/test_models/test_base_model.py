#!/usr/bin/python3


""" Almost a circle project - test Cases

"""


import unittest
from models.base_model import BaseModel
import pep8
from datetime import datetime
import os.path
from os import path


class TestBase_model(unittest.TestCase):
    """ Test cases for base_model.py
    """
    @classmethod
    def setUp(self):
        """ Setting up before start all cases
        """
        self.my_model = BaseModel()
        self.my_model_2 = BaseModel()

    def tearDown(self):
        """ Executed after each test
        """

    def test_pep8(self):
        """ PEP 8 validation
        """
        pep8_style = pep8.StyleGuide(quiet=True)
        pep8_result = pep8_style.check_files(['models/base_model.py'])
        self.assertEqual(pep8_result.total_errors, 0, "fix pep8")

    def test_doc(self):
        """ Check for documentation
        """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_init(self):
        """ correct creation if instance
        """
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertTrue(type(self.my_model.updated_at) is datetime)

    def test_unique_id(self):
        """[summary]
        """
        self.assertNotEqual(self.my_model.id, self.my_model_2.id)

    def test_aditional_attr(self):
        """[summary]
        """
        self.my_model.name = "Holberton"
        self.my_model.my_number = 89
        self.assertEqual(self.my_model.name, "Holberton")

    def test_update_time(self):
        """[summary]
        """
        old_updated_time = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(old_updated_time, self.my_model.updated_at)

if __name__ == '__main__':
    unittest.main()