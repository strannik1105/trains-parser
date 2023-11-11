from abc import ABC


class IParser(ABC):

    def prepare_data(self, data):
        raise NotImplementedError
