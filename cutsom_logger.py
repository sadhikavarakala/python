import os
import time
from functools import wraps

class LogToFile:
    def __init__(self, filename):
        self.filepath = '/Users/sadhikavarakala/Practice' + filename

        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

        with open(self.filepath, 'w') as f:
            f.write("[LOG] New logging session started \n")

    def __enter__(self):
            self.file = open(self.filepath, 'a')
            self.file.write("[LOG] Entering context..\n")
            return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
         self.file.write("[LOG] Exiting context..\n\n")
         self.file.close()

# @log_function_call decorator

def log_function_call(func):
     @wraps(func)
     def wrapper(*args, **kwargs):
          print(f"[LOG] Calling function: {func.__name__}")
          start = time.time()
          result = func(*args, **kwargs)
          end = time.time()
          print(f"[LOG] Function {func.__name__} completed in {end - start:.4f} seconds")
          return result
     return wrapper

@log_function_call
def slow_add(a, b):
     time.sleep(1)
     return a + b

with LogToFile("log.txt"):
    result = slow_add(5, 10)
    print("Result:", result)
        