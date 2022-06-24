
from .process import Process


class ProcessStatus:
    
    def __init__(self, name: str, process: Process, status: bool):
        self.__name: str = name
        self.__process: Process = process
        self.__status: bool = status

    def get_name(self) -> str:
        """Returns the Process status name"""
        return self.__name
    
    def get_process(self) -> Process:
        """Returns the Process status process"""
        return self.__process
    
    def get_status(self) -> bool:
        """Returns the Process status status"""
        return self.__status
    
    def set_name(self, name: str):
        """Sets the Process status name"""
        self.__name = name
    
    def set_process(self, process: Process):
        """Sets the Process status process"""
        self.__process = process
    
    def set_status(self, status: bool):
        """Setst the Process status status"""
        self.__status = status
