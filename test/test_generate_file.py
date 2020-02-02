import os
import unittest

from src.generate_fixed_width_file import generate_fixed_width_file
from src.latitude_exceptions import *


class TestGenerator(unittest.TestCase):

    def test_bad_file_encoding(self):
        file_spec = {
            'InputEncoding' : 'dummy',
            'Offsets' : '12,3,5'
        }
        with self.assertRaises(UnknownEncodingError) as cm:
            generate_fixed_width_file(file_spec, 'test.txt')
        the_exception = cm.exception
        self.assertEqual(the_exception.code, 1002)

    def test_invalid_offsets(self):
        file_spec = {
            'InputEncoding': 'windows-1252',
            'Offsets': '12,3,abcd'
        }
        with self.assertRaises(BadOffsetError) as cm:
            generate_fixed_width_file(file_spec, 'test.txt')
        the_exception = cm.exception
        self.assertEqual(the_exception.code, 1003)


    def test_invalid_file_location(self):
        file_spec = {
            'InputEncoding': 'windows-1252',
            'Offsets': '12,3,5'
        }
        with self.assertRaises(MissingOutputLocationError) as cm:
            generate_fixed_width_file(file_spec, '/abcd/efgh/test.txt')
        the_exception = cm.exception
        self.assertEqual(the_exception.code, 1005)


    def test_valid_options(self):
        file_spec = {
            'InputEncoding': 'windows-1252',
            'Offsets': '12,3,5'
        }
        os.remove('test.txt')
        self.assertFalse(os.path.isfile('test.txt'))
        generate_fixed_width_file(file_spec, 'test.txt')
        self.assertTrue(os.path.isfile('test.txt'))
        os.remove('test.txt')