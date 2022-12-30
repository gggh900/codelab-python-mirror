import sys
import time
import random
from time import perf_counter
from typing import NamedTuple
from multiprocessing import Process, SimpleQueue, cpu_count
from multiprocessing import queues
NUMBERS=range(20, 40)

class RandomSleepResult(NamedTuple):
    elapsed: float

JobQueue=queues.SimpleQueue[int]
ResultQueue=queues.SimpleQueue[RandomSleepResult]
print(f'JobQueue (type) {JobQueue} {type(JobQueue)}')

def printFunctionEntry(func):
    def inner(*args):
        name=func.__name__
        print(f'[{name} entered...')
        result=func(*args)
        return result
    return inner

@printFunctionEntry
def randomSleep(n:int)->RandomSleepResult:
    print("RandomSleep param n", n)
    sleepDuration=random.randint(1, 3)
    time.sleep(sleepDuration)
    print(f'randomSleep: slept for {sleepDuration}')
    return RandomSleepResult(sleepDuration)

@printFunctionEntry
def worker(jobs: JobQueue, results: ResultQueue)->None:
    while n:=jobs.get():
        results.put(randomSleep(n))    
    results.put(RandomSleepResult(0.0))
        
@printFunctionEntry
def start_jobs(procs: int, jobs: JobQueue)->None:
#   for n in NUMBERS:
#       jobs.put(n)
    for _ in range(procs):
        proc=Process(target=worker, args=(jobs, results))
        proc.start()
        jobs.put(0)

if len(sys.argv) < 2:
    procs=cpu_count()
else:
    procs=int(sys.argv[1])

print(f'procs: {procs}')
jobs=SimpleQueue()
results=SimpleQueue()
print(f'Jobs (type) {jobs} {type(jobs)}')
start_jobs(procs, jobs)
    
