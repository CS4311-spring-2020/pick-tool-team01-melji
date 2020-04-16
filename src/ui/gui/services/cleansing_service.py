import subprocess

from src.ui.gui.configuration.configuration import Configuration


class CleansingService(object):

    def __init__(self):

        self.configuration = Configuration()
        self.configuration_values = self.configuration.get_intake_values(service="cleansing")

    # remove the empty lines from a log file
    def remove_empty_lines_logfile(self, log_file_ref):
        uncleansed_data = log_file_ref.data.split('\n')
        cleansed_data = ''
        for line in uncleansed_data:
            if line.rstrip():
                cleansed_data += (line + '\n')
        log_file_ref.replace_data(cleansed_data)
        pass

    def cleanse_log_files_script(self, log_file_ref):
        try:
            script_path = self.configuration_values['script']
        except KeyError:
            raise Exception('Make sure to define absolute path for script')
        cleansed_data = subprocess.check_output([script_path, log_file_ref.data])
        log_file_ref.replace_data(cleansed_data)


# cleansing_service = CleansingService()
# file = open("/Users/eddie/Documents/SchoolProjects/pick-tool-team01-melji/example/uncleansed_logfile.txt", mode="r")
# data = file.read()
# file.close()
# log_file = LogFile(name="Example Text File",
#                    path="/Users/eddie/Documents/SchoolProjects/pick-tool-team01-melji/example/uncleansed_logfile.txt",
#                    data=data)
# print(log_file.data)
# cleansing_service.remove_empty_lines_logfile(log_file)
# print("cleansed")
# print(log_file.data)
# print("done")
# cleansing_service.cleanse_log_files_script(log_file)
# print(log_file.data)
