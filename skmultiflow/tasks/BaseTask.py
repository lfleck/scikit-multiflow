__author__ = 'Guilherme Matsumoto'

from abc import abstractmethod, ABCMeta
from skmultiflow.core.BaseObject import BaseObject

class BaseTask(BaseObject, metaclass=ABCMeta):

    def __init__(self):
        super().__init__()
        pass

    @abstractmethod
    def do_task(self, stream = None, classifier = None):
        pass

    def get_class_type(self):
        return 'task'