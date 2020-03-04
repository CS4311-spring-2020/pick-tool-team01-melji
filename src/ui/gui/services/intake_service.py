from abc import ABC

from rx import Observable
import asyncio
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
        path = "/Users/eddie/Documents/SchoolProjects/pick-tool-team01-melji/example"
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.etl.transform_log_entry(path))


# Testing Intake Service
intake = IntakeService()
intake.ingest_files('/Users/eddie/Documents/SchoolProjects/pick-tool-team01-melji/')
