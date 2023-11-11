from yadisk import YaDisk
from propan import RabbitBroker, PropanApp
from interfaces.common.parser import IParser


class YandexParser(IParser):

    app = object

    def __init__(self, ya_token, connection_link, queue_name):
        super().__init__()
        self._broker = RabbitBroker(connection_link)
        self._queue_name = queue_name
        self._token = ya_token
        self.connect_to_broker()
        self.connect_to_service()

    def connect_to_broker(self):
        self.app = PropanApp(self._broker)

    def connect_to_service(self):
        self._service = YaDisk(token=self._token)

    def prepare_data(self):
        self._raw_data = self.get()

    def get(self):
        pass

