from abc import ABC
from typing import TypeVar, List

T = TypeVar("T")


class IParser(ABC):

    _broker = object
    _service = object
    _queue_name = str
    _service_token = str
    _result_data = List
    _raw_data = List

    def __init__(self):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError

    def prepare_data(self):
        raise NotImplementedError

    def connect_to_service(self):
        raise NotImplementedError

    def connect_to_broker(self):
        raise NotImplementedError
