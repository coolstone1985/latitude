class LatitudeError(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def __repr__(self):
        return repr('Exception %d: %s' % (self.code, self.msg))

class InvalidSpecError(LatitudeError):
    def __init__(self, msg):
        self.code = 1001
        self.msg = msg

class UnknownEncodingError(LatitudeError):
    def __init__(self, msg):
        self.code = 1002
        self.msg = msg

class BadOffsetError(LatitudeError):
    def __init__(self, msg):
        self.code = 1003
        self.msg = msg

class MissingSpecFileError(LatitudeError):
    def __init__(self, msg):
        self.code = 1004
        self.msg = msg

class MissingOutputLocationError(LatitudeError):
    def __init__(self, msg):
        self.code = 1005
        self.msg = msg

class FieldNumberMismatchError(LatitudeError):
    def __init__(self, msg):
        self.code = 1006
        self.msg = msg

class MissingInputLocationError(LatitudeError):
    def __init__(self, msg):
        self.code = 1007
        self.msg = msg

class BadHeaderVal(LatitudeError):
    def __init__(self, msg):
        self.code = 1008
        self.msg = msg
