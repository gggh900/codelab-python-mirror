THREADS=10
import time
import random
from threading import Thread, Event
from multiprocessing import Process, Event
from multiprocessing import synchronize

def sleepRandom(msg: str )->None:
    sleepDuration=random.randint(20, 40)
    print(msg, ": sleeping for ", sleepDuration)
    time.sleep(sleepDuration)
    print(msg, ": done...(slept for ", sleepDuration, "...")
def main() -> None:
    threadArr=[]
    
    for i in range(0, 10):
        threadInst=Process(target=sleepRandom, args=(str(i)))
        print("thread ", i, ": ", threadInst)
        threadArr.append(threadInst)
        
    for i in range(0, 10):
        threadArr[i].start()
    for i in range(0, 10):
        threadArr[i].join()

if __name__ == '__main__':
    main()

