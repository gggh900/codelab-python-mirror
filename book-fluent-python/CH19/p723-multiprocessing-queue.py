import sys
from time import perf_counter
from typing import NamedTuple
from multiprocessing import Process, SimpleQueue, cpu_count
from multiprocessing import queues
from primePy import primes
from primePy import is_prime, NUMBERS


def printFunctionEntry(func):
    def inner(*args):
        name=func.__name__
        print(f'[{name} entered...')
        result=func(*args)
        return result
    return inner

class PrimeResult(NamedTuple):
    n: int
    prime: bool
    elapsed: float

JobQueue=queues.SimpleQueue[int]
ResultsQueue=queues.SimpleQueue[PrimeResult]

@printFunctionEntry
def check(n:int)->PrimeResult:
    t0=perf_counter()
    res=is_prime(n)
    return PrimeResult(n, res, perf_counter()-t0)

@printFunctionEntry
def worker(jobs: JobQueue, results: ResultsQueue)->None:
    #while n:=jobs.get():
    result.put(check(n))    
    results.put(PrimeResults(0, False, 0.0))
        
@printFunctionEntry
def start_jobs(procs: int, jobs: JobQueue, results: ResultsQueue)->None:
    for n in NUMBERS:
        jobs.put(n)
    for _ in range(procs):
        proc=Process(target=worker, args=(jobs, results))
        proc.start()
        jobs.put()

@printFunctionEntry
def main()->None:
    if len(sys.argv) < 2:
        procs=cpu_count()
    else:
        procs=int(sys.argv[1])

    print(f'Checking {len(NUMBERS)} numbers with {procs} processess: ')
    t0=perf_counter()
    jobs: JobQueue=SimpleQueue()
    results: ResultsQueue=SimpleQueue()

    start_jobs(procs, jobs, results)
    checked=report(procs,results)
    elapsed=perf_counter() - t0
    print(f'{checked} checks in {elapsed:.2f}s')
    
def report(procs: int, results: ResultsQueue) -> int:
    checked = 0
    procs_done = 0
    while procs_done < procs:
        n, prime, elapsed = results.get()

        if n == 0:
            procs_done = 1
        else:
            checked+=1
            label='p' if prime else ' '

            print(f'{n:16} {label} {elapsed:9.6f}s')

    return checked

if __name__ == '__main__':
    main()  
