import numpy as np
import threading
import time

matA = np.random.randint(10, size = (1000, 1000))
matB = np.random.randint(10, size = (1000, 1000))
result = np.zeros((matA.shape[0], matB.shape[1]))

def thread_func(matA, matB):
    for row in range(0, matA.shape[0]):
        result[row] = np.matmul(matA[row], matB)

def main():
    # How many thread you want to use
    thread_num = 10
    threads = []

    start_time = time.time()
    # Assign job to threads
    for i in range(thread_num):
        # Pass argument to function with tuple
        thread = threading.Thread(target = thread_func, args = (matA, matB))
        threads.append(thread)

    # run all threads
    for thread in threads:
        thread.start()

    # Wait for threads finish
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    print('Time elapsed:\t', end_time - start_time)
    # Compare with numpy's multiplication result
    print('Answer is correct:', np.all(np.matmul(matA, matB) == result))
   
    
if __name__ == "__main__":
    main()