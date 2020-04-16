class ValidationStatus(object):
    VALIDATED = 0,
    INVALID = 1,
    NOT_VALIDATED = 0


class LogFile(object):
    def __init__(self, name, path, data, is_cleansed=False):
        self.is_cleansed = is_cleansed
        self.name = name
        self.path = path
        self.data = data

    # Mostly used when cleansing the data in a log file
    def replace_data(self, data):
        self.data = data
