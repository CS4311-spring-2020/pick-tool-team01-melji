import splunklib.searchcommands.search_command as splunk

from src.ui.gui.dao.extract_transform_load_dao import ExtractTransformLoadDAO


class SplunkDAO(ExtractTransformLoadDAO):

    def __init__(self):
        pass

    def transform_log_entry(self, text):
        # result = splunk.
        print(text)
