from abc import abstractmethod, ABC


class ExtractTransformLoadDAO(ABC):

    # Going to transform log files into log entry
    @abstractmethod
    def transform_log_entry(self, log_files):
        pass
