
import subprocess

from .process import Process
from .process_status import ProcessStatus


class ProcessManager:
    
    def run(self, process: Process) -> ProcessStatus:
        """Creates a new process and runs the command contained in process

        Argument:
        process -- the process to run"""

        # creates the process status to return
        process_status = ProcessStatus(
            process.get_name(), 
            process,
            False
        )

        completed_process = subprocess.run(
            self.__full_command(process),
            capture_output=False
        )

        if completed_process.returncode == 0:
            process_status.set_status(True)

        return process_status

    def __full_command(self, process: Process) -> [str]:
        """Takes a process and returns its full command

        Arguments:
        process -- the process from which to extract the full command"""

        if process.get_options() is None or len(process.get_options()) == 0:
            return [process.get_command()]

        full_command = [process.get_command()]

        for option in process.get_options():
            full_command.append(f"-{option}")

        return full_command

