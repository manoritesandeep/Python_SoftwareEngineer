import time
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor

def ask_user():
    start = time.time()
    #user_i is a blocking operation, the thread is waiting for something to happen, in this case receive input
    user_i = input("Enter your name: ")
    greet111 = f"Hello, {user_i}"
    print(greet111)
    print(f"ask_user, {time.time() - start}")

def complex_calc():
    start = time.time()
    print('Started calculating....')
    [x ** 2 for x in range(2000000)]
    print(f"complex_calc, {time.time() - start}")

start = time.time()
ask_user()
complex_calc()
print(f'Single thread total time: {time.time() - start}')


# Processes, we use multiprocessing when we need two things to run in the CPU at the same time.
# if __name__ == '__main__':
#     process = Process(target=complex_calc)
#     process2 = Process(target=complex_calc)
#     process.start()
#     process2.start()
#
#     start = time.time()
#
#     process.join()
#     process2.join()
#     print(f'Two process total time: {time.time() - start}')

# we can also use ProcessPoolExecutor
start = time.time()

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_calc)
        pool.submit(complex_calc)

    print(f"Two process total time: {time.time() - start}")