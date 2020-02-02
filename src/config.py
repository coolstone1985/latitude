import json

from src.latitude_exceptions import InvalidSpecError, MissingSpecFileError

mandatory_columns = [
    'ColumnNames',
    'Offsets',
    'InputEncoding',
    'IncludeHeader',
    'OutputEncoding'
]

def load_spec(spec_file='/etc/conf/spec.json'):
    try:
        with open(spec_file, 'r') as specs:
            data = specs.read()
            conf = json.loads(data)
            if not all(key in conf for key in mandatory_columns):
                raise InvalidSpecError('some or all of mandatory specs: %s are missing' % mandatory_columns)
        return conf
    except FileNotFoundError:
        raise MissingSpecFileError('spec file: %s does not exist' % spec_file)
