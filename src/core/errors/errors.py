
class NoProcessToRun(Exception):
    
    def __init__(self, message=None):
        exception_message = "No process to run, use set_process() first."
        if message is not None:
            exception_message = message
        
        super().__init__(exception_message)

class NoMoreProcessToRun(Exception):

    def __init__(self, message=None):
        exception_message = "No more process to run."
        if message is not None:
            exception_message = message
        
        super().__init__(exception_message)
