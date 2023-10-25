from multiprocessing import Pool
import time
def f(x):
    return x*x

if __name__ == '__main__':
    l=[]
    for i in range(10000):
      l.append(i)
    start_time = time.perf_counter()  
    with Pool(5) as p:
        print(p.map(f, l))
    print(" time taken : %.4s seconds" %(time.perf_counter()-start_time))  		