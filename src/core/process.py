
from typing import List


class Process:
    
    def __init__(self, name: str, command: str, options: List[str]):
        self.__name: str = name
        self.__command: str = command
        self.__options: List[str] = options

    def get_name(self) -> str:
        """Returns the Process' name"""
        return self.__name
    
    def get_command(self) -> str:
        """Returns the Process' command"""
        return self.__command
    
    def get_options(self) -> List[str]:
        """Returns the Process' command options"""
        return self.__options
    
    def set_name(self, name: str):
        """Sets the Process name"""
        self.__name = name
    
    def set_command(self, command: str):
        """Sets the Process command"""
        self.__command = command
    
    def set_options(self, options: List[str]):
        """Sets the Process command options"""
        self.__options = options

