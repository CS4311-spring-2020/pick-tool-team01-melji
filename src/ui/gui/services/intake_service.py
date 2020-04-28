from abc import ABC

from rx import Observable
import asyncio
import os
import asyncio
import string

from dao.splunk_dao import SplunkDAO
from services.ocr_service import OCRService
from services.transcriber_service import TranscriberService

"""
Service for ingesting files into the system and returning log-entries. Its going to be using :Validation Service:, 
:Transcriber Service:, and :OCR Service:
TODO: right now the other services are converted multimedia files into text files.
"""


class IntakeService(Observable):

    def subscribe(self, observer):
        pass

    def __init__(self):
        self.etl = SplunkDAO()
        self.ocr_service = OCRService()
        self.transcriber_service = TranscriberService()
        self.transformation_services = [self.ocr_service, self.transcriber_service]

    def register_validation_observer(self, observer):
        self.subscribe(observer)

    def register_intake_observer(self):
        pass

    def get_files(self, file_path):
        for service in self.transformation_services:
            if service.is_file_supported(file_path):
                result = service.convert_to_string(file_path)
                result = str(result)
                info = os.path.split(file_path)[1]
                path = os.path.split(file_path)[0]
                info = "example_log.txt"
                # os.makedirs(os.path.join(path, info))
                text_file = open(os.path.join(path, info), "a")
                result = "\n" + result + "\n"
                text_file.write(result)
                text_file.close()
                return 0
        return 1

    def ingest_files(self, path):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                indv_path = os.path.join(root, name)
                is_text = self.etl.is_file_supported(indv_path)
                #if not is_text:
                    #self.get_files(indv_path)
        entries = self.etl.transform_log_entry(path)
        return entries


# intake = IntakeService()
# intake.ingest_files("/Users/eddie/Documents/SchoolProjects/pick-tool-team01-melji/example/")
# print(entries)
