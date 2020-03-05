
class ValidationStatus (object):
    VALIDATED= 0,
    INVALID=1,
    NOT_VALIDATED=0

class LogFile(object):
    def __init__(self, name, path, is_cleansed=False, ):
        self.is_cleansed = is_cleansed
        self.name = name
        self.path = path
