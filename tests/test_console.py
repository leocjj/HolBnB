#!/usr/bin/python3
"""Testing file to test console
"""
#Imports
import unittest
import json
import pep8
import console
import os
import test
#Import console
from console import HBNBCommand
#Import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
#...


class TestConsole(unittest.TestCase):
    """Create testcases for the console
    """
    #First things first, the setupclass
    @classmethod
    def setUpClass(cls):
        """Called before test in an individual class are run (HHNBCommand)
        """
        cls.console = HBNBCommand()

    @classmethod
    def tearDown(cls):
        """Called after test in an individual class have run (del HHNBCommand)
        """
        del cls.console

    #Clean after run tests
    def tearDown(self):
        """Clean file created after run the test (json file)
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    unittest.main()
