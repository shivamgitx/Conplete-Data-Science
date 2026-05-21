"""
Real-World Example: Multiprocessing for CPU-bound Tasks

Scenario: Factorial Calculation

Factorial calculations, especially for large numbers,
involve significant computational work. Multiprocessing
can be used to distribute the workload across multiple
CPU cores, improving performance.
"""

import multiprocessing
import math
import sys
import time

# Increase he maxmium number of digits for integer conversation
sys.set_int_max_str_digits(100000)

# function to compute factorials of a given number

def compute_factorial(number):
    print(f"Copmputing factorial of {number}")
    result=math.factorial(number)
    return result

if __name__ == "__main__":
    numbers=[5000,6000,7000,8000]
    
    start_time=time.time()
    
    #create a pool for worker process
    with multiprocessing.Pool() as pool:
        results=pool.map(compute_factorial,numbers)
    
    end_time=time.time()
    
    print(f"Results: {results}")
    print(f"Time Taken: {end_time-start_time} seconds")