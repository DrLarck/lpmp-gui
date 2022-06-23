
import subprocess
import sys

from typing import List
from collections import deque
from core.errors.errors import NoProcessToRun, NoMoreProcessToRun


class ProcessManager: 

    def __init__(self):
        self.__current: (str, List[str]) = None
        self.__queued: deque((str, List[str])) = deque()
    
    def run(self):
        """Runs the command with the options"""
        current = self.get_current()
        if current is None:
            raise NoProcessToRun

        current_command: [str] = self.__full_command()
        process = subprocess.run(current_command)

        while True:
            try:
                self.__next()
            except NoMoreProcessToRun:
                break
                
            command: [str] = self.__full_command()
            process = subprocess.run(command)

    def __next(self):
        """Updates the current process being run

        Arguments:
        process -- the process that is currently being run"""
        self.set_current(None)

        next_process = self.__pop()
        if next_process is not None:
            self.set_current(next_process)
        else:
            raise NoMoreProcessToRun

    def __pop(self) -> (str, List[str]):
        """Pop the left most process"""
        dequeued = None

        try:
            dequeued = self.__queued.popleft()
        except Exception:
            pass

        return dequeued
    
    def __full_command(self) -> [str]:
        """Returns the full command of the current process to execute"""
        current = self.get_current()
        command = current[0]
        options = current[1]
        full_command = [command]

        if options is not None:
            for option in options:
                full_command.append(option)

        return full_command
    
    def get_current(self) -> (str, List[str]):
        """Returns the current process"""
        return self.__current

    def get_queued(self) -> deque((str, List[str])):
        """Returns the queued processes"""
        return self.__queued

    def set_current(self, process: (str, List[str])):
        """Sets the current process

        Arguments:
        process -- the current process"""
        self.__current = process

    def enqueue(self, process: (str, List[str])):
        """Enqueues a process

        Arguments:
        process -- the process to enqueue"""
        self.__queued.append(process)
