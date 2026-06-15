from abc import ABC, abstractmethod
import logging

class BaseTask(ABC):
    def __init__(self, config):
        self.config = config
        self.task_name = config["task_name"]
        self.file_path = config["file_path"]
        self.logger = logging.getLogger()

    @abstractmethod
    def execute(self):
        pass