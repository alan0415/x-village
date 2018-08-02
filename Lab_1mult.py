import multiprocessing
import numpy as np
import time


matA = np.random.randint(10, size = (10, 10))
matB = np.random.randint(10, size = (10, 10))
result = np.zeros((matA.shape[0], matB.shape[1]))
re = np.zeros((matA.shape[0], matB.shape[1]))

def thread_func(matA, matB):
    for row in range(0, matA.shape[0]):
        swap = np.matmul(matA[row], matB)
        result[row] = swap
    

def main():
    # Generate queue for communication
    global re
    result = multiprocessing.Manager().dict()
    processes = 10
    jobs = []
    start_time = time.time()
    print(matB)
    for i in range(processes):
        process = multiprocessing.Process(target = thread_func, args = (matA, matB))
        jobs.append(process)

    for process in jobs:
        process.start()

    for process in jobs:
        process.join()
    
    print(result)

    for j in range(0,len(result)):
        print(i)
        print(result[j])
        print('*'*20)
        re = result[j]

    end_time = time.time()
    print('Time elapsed:\t', end_time - start_time)
    print('Answer is correct:', np.all(np.matmul(matA, matB) == re))

if __name__ == "__main__":
    main()