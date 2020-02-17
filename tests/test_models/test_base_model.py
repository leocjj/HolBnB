#!/usr/bin/python3
"""BaseModel test file
"""
#imports
import unittest
import os
import pep8
#import models
from models.base_model import BaseModel
#...


class TestBaseModel(unittest.TestCase):
    """Set the test for base model class
    """
    #First things first, the setupclass
    @classmethod
    def setUpClass(cls):
        """Called before test in an individual class are run
        """
        cls.b = BaseModel()
        cls.b.save()

    @classmethod
    def tearDown(cls):
        """Called after test in an individual class have run
        """
        del cls.b

    #Clean after run tests
    def tearDown(self):
        """Clean file created after run the test (json file)
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    #Run pep8 validate console.py
    def test_base_model_py(self):
        """pep8 base_model.py test
        """
        s = pep8.StyleGuide(quiet=True)
        f = p.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, 'pep8 error found!')

    #TO_DO Docstrings
    #TO_DO Test Save
    #TO_DO Test to_dict
    #TO_DO Instance creation (BaseModel)
    #TO_DO Check class for the listing methods

if __name__ == "__main__":
    unittest.main()