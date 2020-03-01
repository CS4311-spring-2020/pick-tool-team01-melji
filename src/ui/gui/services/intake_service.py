from abc import ABC

from rx import Observable
import os

from src.ui.gui.dao.splunk_dao import SplunkDAO
from src.ui.gui.services.ocr_service import OCRService
from src.ui.gui.services.transcriber_service import TranscriberService

"""
Service for ingesting files into the system and returning log-entries. Its going to be using :Validation Service:, 
:Transcriber Service:, and :OCR Service:
"""


class IntakeService(Observable):

    def subscribe(self, observer):
        pass

    def __init__(self):
        self.etl = SplunkDAO()
        self.ocr_service = OCRService()
        self.transcriber_service = TranscriberService()

    def register_validation_observer(self, observer):
        self.subscribe(observer)

    def register_intake_observer(self):
        pass

    def ingest_files(self, path):
        file = open('/Users/eddie/Documents/SchoolProjects/pick-tool-team01-melji/testing.txt', 'r')
        for line in file:
            self.etl.transform_log_entry(line)
        # print(file)
        pass


# Testing Intake Service
intake = IntakeService()
intake.ingest_files('/Users/eddie/Documents/SchoolProjects/pick-tool-team01-melji/')
