
import subprocess

from .process import Process
from .process_status import ProcessStatus


class ProcessManager:
    
    def run(self, 
            process: Process,
            result: List[ProcessStatus]=None) -> ProcessStatus:
        """Creates a new process and runs the command contained in process

        Argument:
        process -- the process to run
        [Optional] result -- the result list that will hold the result of the process"""

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

        if result is not None:
            result.clear()
            result[0] = process_status

        return process_status

    def run_sync(self, 
                 processes: List[Process], 
                 result: List[ProcessStatus]=None) -> List[ProcessStatus]:
        """Runs a sequence of processes synchronously and returns their status

        Arguments:
        processes -- the sequence of processes to execute synchronously
        [Optional] result -- the result list that will hold the result of the process"""

        processes_status: List[ProcessStatus] = []
        for process in processes:
            processes_status.append(self.run(process))

        if result is not None:
            result.clear()
            for status in processes_status:
                result.append(status)

        return processes_status

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

