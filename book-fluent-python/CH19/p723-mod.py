import sys
import time
import random
from time import perf_counter
from typing import NamedTuple
from multiprocessing import Process, SimpleQueue, cpu_count
from multiprocessing import queues
NUMBERS=range(20, 40)

JobQueue=queues.SimpleQueue[int]

class RandomSleepResult(NamedTuple):
    elapsed: float

def printFunctionEntry(func):
    def inner(*args):
        name=func.__name__
        print(f'[{name} entered...')
        result=func(*args)
        return result
    return inner

#@printFunctionEntry
def randomSleep(n:int)->RandomSleepResult:
    #t0=perf_counter()
    #res=is_prime(n)
    #return RandomSleepResult(n, res, perf_counter()-t0)
    sleepDuration=random.randint(20, 40)
    time.sleep(sleepDuration)
    return RandomSleepResult(sleepDuration)

@printFunctionEntry
def worker(jobs: JobQueue)->None:
    while n:=jobs.get():
        result.put(randomSleep(n))    
    #results.put(RandomSleepResult(0, False, 0.0))
        
@printFunctionEntry
def start_jobs(procs: int, jobs: JobQueue)->None:
    for n in NUMBERS:
        jobs.put(n)
    for _ in range(procs):
        proc=Process(target=worker, args=(jobs))
        proc.start()
        jobs.put()

if len(sys.argv) < 2:
    procs=cpu_count()
else:
    procs=int(sys.argv[1])

jobs=SimpleQueue()
start_jobs(procs, jobs)
    
