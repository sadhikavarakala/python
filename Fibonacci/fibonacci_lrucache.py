import time
from functools import lru_cache
import os

#Recurive Finbonacci without memoisation

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

#Recrusive Fibonacci with memoisation using lru_cache

@lru_cache(maxsize=None)
def fibonacci_memoized(n):
    if n <= 1:
        return n
    return fibonacci_memoized(n-1) + fibonacci_memoized(n-2)

n = 30

#measure for fibonacci without memoization
start = time.time()
fib1 = fibonacci(n)
end = time.time()
time_recursive = end - start

#measure for fibonacci with memoization
start = time.time()
fib2 = fibonacci_memoized(n)
end = time.time()
time_memoized = end - start

#print
print(f"fibonacci{n} without memoization: {fib1}")
print(f"time taken without memoization: {time_recursive:.6f} seconds")

print(f"fibonacci{n} with memoization: {fib2}")
print(f"time taken with memoization: {time_memoized:.6f} seconds")

#save results to a file
output_path = "/Users/sadhikavarakala/GitHub/python/fibonacci_results.txt"

with open(output_path, 'w') as f:
    f.write(f"fibonacci comparison for n = {n}\n\n")
    f.write(f"fibonacci{n} without memoization: {fib1}\n")
    f.write(f"time taken without memoization: {time_recursive:.6f} seconds\n")
    f.write(f"fibonacci{n} with memoization: {fib2}\n")
    f.write(f"time taken with memoization: {time_memoized:.6f} seconds\n")

print(f"Results saved to {output_path}")