import splunklib.client as client
import splunklib.results as results
import asyncio, concurrent.futures
import os

from src.ui.gui.dao.extract_transform_load_dao import ExtractTransformLoadDAO
from src.ui.gui.model.log_entry import LogEntry

HOST = "localhost"
PORT = 8089
USERNAME = "admin"
PASSWORD = "eherreraga858408"
INDEX = "main"
DEBUG = True


class SplunkDAO(ExtractTransformLoadDAO):

    def __init__(self):
        self.service = client.connect(
            host=HOST,
            port=PORT,
            username=USERNAME,
            password=PASSWORD)
        self.pool = concurrent.futures.ThreadPoolExecutor()

    async def upload_logfile(self, path):
        if DEBUG:
            print('uploading ', path)
        index = self.service.indexes[INDEX]
        index.upload(path)

    async def upload_logfiles(self, directory_path):
        if DEBUG:
            print("uploading directory ", directory_path)
        for root, dirs, files, in os.walk(directory_path, topdown=False):
            for name in files:
                path = os.path.join(root, name)
                await self.upload_logfile(path)
        return 0

    def transform_to_logentry(self, result):
        return LogEntry(identifier=result['_bkt'], timestamp=result['_time'], content=result['_raw'],
                        host=result['host']
                        , source=result['source'], source_type=result['sourcetype'])

    async def retrieving_splunk_events(self):
        jobs = self.service.jobs
        entries = list()
        kwargs_blockingsearch = {"exec_mode": "blocking"}
        searchquery_blocking = "search * | head 100"
        print("waiting for search job to finish")

        job = jobs.create(searchquery_blocking, **kwargs_blockingsearch)
        for result in results.ResultsReader(job.results()):
            if DEBUG:
                print(result)
            entries.append(self.transform_to_logentry(result))
        return entries

    async def transform_log_entry(self, log_file_directory_path):
        status = await self.upload_logfiles(log_file_directory_path)
        entries = await self.retrieving_splunk_events()

        for entry in entries:
            print("host: " + entry.host + "\ncontent: " + entry.content + "\nsource: " + entry.source + "\ntime: "
                  + entry.timestamp)
            print("===========")
        return entries
