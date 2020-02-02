import os
import unittest

from src.generate_fixed_width_file import *
from src.parse_fixed_width_file import *


class TestParser(unittest.TestCase):
    def test_bad_include_header_va(self):
        file_spec = {
            'ColumnNames': 'c1, c2, c3',
            'Offsets': '12, 10',
            'IncludeHeader': 'Maybe'
        }
        with self.assertRaises(BadHeaderVal) as cm:
            parse_fixed_width_file(file_spec, 'input.txt', 'output.csv')
        the_exception = cm.exception
        self.assertEqual(the_exception.code, 1008)

    def test_field_mismatch(self):
        file_spec = {
            'ColumnNames': 'c1, c2, c3',
            'Offsets': '12, 10',
            'IncludeHeader': 'True'
        }
        with self.assertRaises(FieldNumberMismatchError) as cm:
            parse_fixed_width_file(file_spec, 'input.txt', 'output.csv')
        the_exception = cm.exception
        self.assertEqual(the_exception.code, 1006)

    def test_unknown_output_encoding(self):
        file_spec = {
            'ColumnNames': 'c1, c2, c3',
            'Offsets': '12, 10, 14',
            'IncludeHeader': 'True',
            'OutputEncoding': 'unknown'
        }
        with self.assertRaises(UnknownEncodingError) as cm:
            parse_fixed_width_file(file_spec, 'input.txt', 'output.csv')
        the_exception = cm.exception
        self.assertEqual(the_exception.code, 1002)

    def test_missing_output_file(self):
        file_spec = {
            'ColumnNames': 'c1, c2, c3',
            'Offsets': '12, 10, 14',
            'IncludeHeader': 'True',
            'OutputEncoding': 'utf-8'
        }
        with self.assertRaises(MissingOutputLocationError) as cm:
            parse_fixed_width_file(file_spec, 'input.txt', '/abc/def/ghe/output.csv')
        the_exception = cm.exception
        self.assertEqual(the_exception.code, 1005)

    def test_missing_input_file(self):
        file_spec = {
            'ColumnNames': 'c1, c2, c3',
            'Offsets': '12, 10, 14',
            'IncludeHeader': 'True',
            'OutputEncoding': 'utf-8',
            'InputEncoding': 'windows-1252'
        }
        with self.assertRaises(MissingInputLocationError) as cm:
            parse_fixed_width_file(file_spec, '/abc/def/ghe/input.txt', 'output.csv')
        the_exception = cm.exception
        self.assertEqual(the_exception.code, 1007)

    def test_unknown_input_encoding(self):
        file_spec = {
            'ColumnNames': 'c1, c2, c3',
            'Offsets': '12, 10, 14',
            'IncludeHeader': 'True',
            'OutputEncoding': 'utf-8',
            'InputEncoding': 'unknown'
        }
        open('input.txt', 'a').close()
        with self.assertRaises(UnknownEncodingError) as cm:
            parse_fixed_width_file(file_spec, 'input.txt', 'output.csv')
        the_exception = cm.exception
        self.assertEqual(the_exception.code, 1002)
        os.remove('input.txt')

    def test_bad_offsets(self):
        with self.assertRaises(BadOffsetError) as cm:
            parse_row('abscdgfhhfhgf', ['abc', '12', '3'])
        the_exception = cm.exception
        self.assertEqual(the_exception.code, 1003)

    def test_with_header(self):
        file_spec = {
            'ColumnNames': 'c1, c2, c3',
            'Offsets': '2, 3, 4',
            'IncludeHeader': 'True',
            'OutputEncoding': 'utf-8',
            'InputEncoding': 'windows-1252'
        }
        with open('test.txt', 'w', encoding=file_spec['InputEncoding']) as in_file:
            in_file.write('aabbbcccc\n')
            in_file.write('ddeeeffff\n')
            in_file.write('gghhhiiii\n')

        parse_fixed_width_file(file_spec, 'test.txt', 'test.csv')
        with open('test.csv', 'r', encoding=file_spec['OutputEncoding']) as out_file:
            lines = out_file.readlines()
        self.assertEqual(file_spec['ColumnNames'] + '\n', lines[0])
        self.assertEqual('aa,bbb,cccc\n', lines[1])
        self.assertEqual('dd,eee,ffff\n', lines[2])
        self.assertEqual('gg,hhh,iiii\n', lines[3])
        os.remove('test.txt')
        os.remove('test.csv')

    def test_without_header(self):
        file_spec = {
            'ColumnNames': 'c1, c2, c3',
            'Offsets': '2, 3, 4',
            'IncludeHeader': 'False',
            'OutputEncoding': 'utf-8',
            'InputEncoding': 'windows-1252'
        }
        with open('test.txt', 'w', encoding=file_spec['InputEncoding']) as in_file:
            in_file.write('aabbbcccc\n')
            in_file.write('ddeeeffff\n')
            in_file.write('gghhhiiii\n')

        parse_fixed_width_file(file_spec, 'test.txt', 'test.csv')
        with open('test.csv', 'r', encoding=file_spec['OutputEncoding']) as out_file:
            lines = out_file.readlines()
        self.assertEqual('aa,bbb,cccc\n', lines[0])
        self.assertEqual('dd,eee,ffff\n', lines[1])
        self.assertEqual('gg,hhh,iiii\n', lines[2])
        os.remove('test.txt')
        os.remove('test.csv')

    def test_quotes(self):
        file_spec = {
            'ColumnNames': 'c1, c2, c3',
            'Offsets': '2, 3, 4',
            'IncludeHeader': 'False',
            'OutputEncoding': 'utf-8',
            'InputEncoding': 'windows-1252'
        }
        with open('test.txt', 'w', encoding=file_spec['InputEncoding']) as in_file:
            in_file.write('"aab""bc"')
        parse_fixed_width_file(file_spec, 'test.txt', 'test.csv')
        with open('test.csv', 'r', encoding=file_spec['OutputEncoding']) as out_file:
            lines = out_file.readlines()
        self.assertEqual('"""a","ab""","""bc"""\n', lines[0])
        os.remove('test.txt')
        os.remove('test.csv')
