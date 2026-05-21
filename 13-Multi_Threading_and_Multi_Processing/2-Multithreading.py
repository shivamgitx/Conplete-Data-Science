### MultiThreading
## When to use MultiThreading
### I/O bound tasks: Tasks that spend more time waiting for I/O operations (eg.file operations, network requests)
### Concurrent execution: when you want to improve the throughout of your application by performing multiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Numbers: {i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

## create 2 threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)

t=time.time()
##start the thread
t1.start()
t2.start()

### wait for the threads to finish
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)