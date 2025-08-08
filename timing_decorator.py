## timing decorator.py - measures how long the function takes to run

import time
from functools import wraps

def time_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Starting {func.__name__}...")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} completed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@time_function
def slow_function(seconds):
    time.sleep(seconds)
    return f"done sleeping"

slow_function(2)