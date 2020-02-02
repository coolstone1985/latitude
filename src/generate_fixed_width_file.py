import random
import string

from src.latitude_exceptions import *


def generate_fixed_width_file(file_spec, output_file_name):
    try:
        with open(output_file_name, 'w', encoding=file_spec['InputEncoding']) as file:
            for i in range(0, random.randrange(10, 100)):
                ln = []
                for word_len in file_spec['Offsets'].split(','):
                    word = generate_fixed_length_string(word_len)
                    ln.append(word)
                file.write('%s\n' % ''.join(ln))
    except LookupError:
        raise UnknownEncodingError('Unknown encoding: %s' % file_spec['InputEncoding'])
    except ValueError:
        raise BadOffsetError('Incorrect value in offsets: %s' % file_spec['Offsets'])
    except FileNotFoundError:
        raise MissingOutputLocationError('output location: %s does not exist' % output_file_name)


def generate_fixed_length_string(word_length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(int(word_length)))
