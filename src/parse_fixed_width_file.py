import ast
import csv
from src.latitude_exceptions import *


def parse_fixed_width_file(file_spec, input_file, output_file):
    try:
        include_header = ast.literal_eval(file_spec['IncludeHeader'])
    except ValueError:
        raise BadHeaderVal('Incorrect value for IncludeHeader spec: %s' % file_spec['IncludeHeader'])
    headers = file_spec['ColumnNames'].split(',')
    word_lengths = file_spec['Offsets'].split(',')
    if len(headers) != len(word_lengths):
        raise FieldNumberMismatchError(
            'Number of columns in csv [%d] is not same as number of columns in fixed width file [%d]' % (
                len(headers), len(word_lengths)))
    try:
        with open(output_file, 'w', encoding=file_spec['OutputEncoding']) as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL)
            if include_header:
                csv_writer.writerow(h for h in headers)
            for line in read_fixed_width_data(input_file, file_spec['InputEncoding']):
                csv_writer.writerow(l for l in parse_row(line, word_lengths))
    except FileNotFoundError:
        raise MissingOutputLocationError('Unable to locate output directory: %s' % output_file)
    except LookupError:
        raise UnknownEncodingError('Unknown encoding for csv file: %s' % file_spec['OutputEncoding'])


def read_fixed_width_data(input_file, encoding):
    try:
        with open(input_file, 'r', encoding=encoding) as fixed_width_file:
            lines = fixed_width_file.readlines()
            return lines
    except LookupError:
        raise UnknownEncodingError('Unknown encoding for fixed width file: %s' % encoding)
    except FileNotFoundError:
        raise MissingInputLocationError('Unable to find input file: %s' % input_file)


def parse_row(line, word_lengths):
    try:
        row = []
        index = 0
        for x in word_lengths:
            length = int(x)
            row.append(line[index:index + length])
            index = index + length
        return row
    except ValueError:
        raise BadOffsetError('Bad offset values: %s' % word_lengths)
