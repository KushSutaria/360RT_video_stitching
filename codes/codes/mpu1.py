from multiprocessing import Process
import time

def print_func(continent='Asia'):
    print('The name of continent is : ', continent)

if __name__ == "__main__":  # confirms that the code is under main function
    start_time = time.perf_counter()
    names = ['America', 'Europe', 'Africa']
    # instantiating process with arguments
    for name in names:
        # print(name)
       print_func(name)
    print(" time taken : %.4s seconds" %(time.perf_counter()-start_time))  	