from yadisk import YaDisk
from interfaces.common.service import IService
import pandas

class MockService(IService):

    def __init__(self, token, url):
        self._service_token = token
        self._service_url = url

    def connect(self):
        self._service = YaDisk(token=self._service_token)

    def get(self):
        data = pandas.read_excel('uploads/disl_hackaton.xlsx', nrows=1)
        return data.values.tolist()

    def download(self):
        self._service.upload_url(self._service_url, 'uploads/')