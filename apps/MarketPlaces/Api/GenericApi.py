from abc import ABC, abstractmethod


class GenericSaleItemApi(ABC):

    @abstractmethod
    def get_title(self):
        return None

    @abstractmethod
    def get_price(self):
        return None

    @abstractmethod
    def get_properties(self):
        return None

    @abstractmethod
    def get_description(self):
        return None

    @abstractmethod
    def getItem(self):
        return None
