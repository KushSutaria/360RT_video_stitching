import time
def f(x):
    return x*x

if __name__ == '__main__':
    start_time = time.perf_counter()
    for i in range(10000):
       print(f(i))
    print(" time taken : %.4s seconds" %(time.perf_counter()-start_time))  		