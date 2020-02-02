import json
import os
import unittest
from src.latitude_exceptions import *
from src.config import load_spec

specs = {
    'ColumnNames' : 'f1,f2,f3',
    'Offsets' : '1,2,5',
    'InputEncoding' : 'windows-1252',
    'IncludeHeader' : 'True',
    'OutputEncoding' : 'utf-8'
}

class TestConfig(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._valid_spec_file =  cls.generate_valid_specs(cls)
        cls._invalid_spec_file = cls.generate_invalid_specs(cls)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls._invalid_spec_file)
        os.remove(cls._valid_spec_file)

    def generate_valid_specs(self):
        with open('valid_spec.json', 'w') as valid_spec:
            json.dump(specs, valid_spec)
        return 'valid_spec.json'

    def generate_invalid_specs(self):
        invalid_specs = specs.copy()
        del invalid_specs['Offsets']
        with open('invalid_spec.json', 'w') as invalid_spec:
            json.dump(invalid_specs, invalid_spec)
        return 'invalid_spec.json'


    def test_spec_file_missing(self):
        with self.assertRaises(MissingSpecFileError) as cm:
            load_spec()
        the_exception = cm.exception
        self.assertEqual(the_exception.code, 1004)

    def test_invalid_specs(self):
        with self.assertRaises(InvalidSpecError) as cm:
            load_spec(self._invalid_spec_file)
        the_exception = cm.exception
        self.assertEqual(the_exception.code, 1001)

    def test_valid_spec_file(self):
        self.assertDictEqual(specs, load_spec(self._valid_spec_file))
