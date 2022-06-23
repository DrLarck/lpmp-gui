
from threading import Thread
from core.process_manager import ProcessManager


def main():
    process_manager = ProcessManager()
    lpmp = ("include/large_PMP", ["-gui"])
    lpmp_2 = lpmp
    lpmp_3 = lpmp

    process_manager.set_current(lpmp)
    process_manager.enqueue(lpmp_2)
    process_manager.enqueue(lpmp_3)
    process_manager.run()

    # process = Thread(target=process_manager.run, args=(["./include/large_PMP", "-gui"],))
    # process.start()
    # process.join()


if __name__ == "__main__":
    main()
