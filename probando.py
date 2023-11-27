# create arrays in a parent process and read in children via queue
from multiprocessing import Process
from multiprocessing import Queue
from random import randint
from numpy.random import random
 
# read numpy arrays from the queue and compute something
def task(queue):
    # read arrays
    while True:
        # read one array
        data = queue.get()
        # check for final item
        if data is None:
            # report message
            print('Task done.', flush=True)
            # push signal back into queue
            queue.put(data)
            # exit the task
            break
        # compute max of array
        result = data.max()
        # report a message
        print(f'Task read an array {data.shape}, max={result}', flush=True)
 
# protect the entry point
if __name__ == '__main__':
    # create the shared queue
    queue = Queue()
    # issue task processes
    tasks = [Process(target=task, args=(queue,)) for _ in range(4)]
    for t in tasks:
        t.start()
    # generate many arrays of random numbers
    for _ in range(20):
        # generate random dimensions
        dim = (randint(500,2000),randint(500,2000))
        # generate array of random floats with random dimensions
        data = random(dim)
        # push into queue
        queue.put(data)
    # signal no further arrays
    queue.put(None)
    # wait for task processes to be done
    for t in tasks:
        t.join()
    # report a final message
    print('Done.', flush=True)