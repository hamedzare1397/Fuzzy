from numba import jit, cuda, errors,njit,prange
import numpy as np
# to measure exec time
from timeit import default_timer as timer
import random

# normal function to run on cpu
def func(n,array):
    for i in range(n):
        x = random.random()
        a = random.random()
        b = random.random()
        c = random.random()
        if a>x:
            array[i] = 0
        elif a<=x and x<= b:
            array[i] = np.divide((np.subtract(x,a)),(np.subtract(b,a)))
        elif b<=x and x<= c:
            array[i] = np.divide(np.subtract(c,x),np.subtract(c,b))
        elif c<=x:
            array[i] = 0
        array[i] = 0


@njit()
def func2(n,array):
    for i in range(n):
        x = random.random()
        a = random.random()
        b = random.random()
        c = random.random()
        if a > x:
            array[i] = 0
        elif a <= x and x <= b:
            array[i] = np.divide((np.subtract(x, a)), (np.subtract(b, a)))
        elif b <= x and x <= c:
            array[i] = np.divide(np.subtract(c, x), np.subtract(c, b))
        elif c <= x:
            array[i] = 0
        array[i] = 0

@njit(nogil=True)
def func3():
    x = random.random()
    a = random.random()
    b = random.random()
    c = random.random()
    if a > x:
        return 0
    elif a <= x and x <= b:
        return np.divide((np.subtract(x, a)), (np.subtract(b, a)))
    elif b <= x and x <= c:
        return np.divide(np.subtract(c, x), np.subtract(c, b))
    elif c <= x:
        return 0
    return 0


@njit(parallel=True)
def logistic_regression(n):
    for i in prange(n):
        func3()
    return 0


if __name__ == "__main__":
    n = 1000000
    a = np.ones(n, dtype=np.float64)
    b = np.ones(n, dtype=np.float32)
    start = timer()
    func(n,a)
    print("without GPU:", timer() - start)

    start = timer()
    func2(n,a)
    print("with GPU:", timer() - start)

    start = timer()
    func2(n,a)
    print("with GPU:", timer() - start)

    start = timer()
    logistic_regression(n)
    print("with GPU:", timer() - start)

    start = timer()
    logistic_regression(n)
    print("with GPU:", timer() - start)