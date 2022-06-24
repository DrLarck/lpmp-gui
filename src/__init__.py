
import time
from typing import List
from threading import Thread

from core.process import Process
from core.process_status import ProcessStatus
from core.process_manager import ProcessManager


def main():
    begin = time.time()

    process_manager = ProcessManager()
    processes: List[Process] = [
        Process("lpmp_thread_1", "res/include/large_PMP", ["gui"]),
        Process("lpmp_thread_2", "res/include/large_PMP", ["gui"]),
        Process("lpmp_thread_3", "res/include/large_PMP", ["gui"]),
        Process("lpmp_thread_4", "res/include/large_PMP", ["gui"]),
        Process("lpmp_thread_5", "res/include/large_PMP", ["gui"]),
        Process("lpmp_thread_6", "res/include/large_PMP", ["gui"]),
        Process("lpmp_thread_7", "res/include/large_PMP", ["gui"]),
        Process("lpmp_thread_8", "res/include/large_PMP", ["gui"]),
        Process("lpmp_thread_9", "res/include/large_PMP", ["gui"]),
        Process("lpmp_thread_10", "res/include/large_PMP", ["gui"]),
        Process("lpmp_thread_11", "res/include/large_PMP", ["gui"]),
        Process("lpmp_thread_12", "res/include/large_PMP", ["gui"]),
    ]
    result_threaded: List[ProcessStatus] = []

    t_ = Thread(
        target=process_manager.run_threaded,
        args=(processes, result_threaded)
    )
    t_.start()
    t_.join()

    for i in result_threaded:
        print(f"Process \"{i.get_name()}\" terminated successfuly: {i.get_status()}")

    end = time.time()
    print(f"Ran in {end-begin}s")


if __name__ == "__main__":
    main()
