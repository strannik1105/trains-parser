from abc import ABC


class IService(ABC):

    _service = object
    _service_token = str
    def __init__(self):
        raise NotImplementedError

    def connect(self):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError