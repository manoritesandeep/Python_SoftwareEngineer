from database import Database
from abc import ABCMeta, abstractmethod


class Saveable(metaclass=ABCMeta):
    def save(self):
        Database.insert(self.to_dict())

    # The purpose of the abstract method is to force the subclass to implent it needs
    @abstractmethod
    def to_dict(self):
        pass