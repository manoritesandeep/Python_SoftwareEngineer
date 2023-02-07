import time
from threading import Thread

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


thread1 = Thread(target=complex_calc)
thread2 = Thread(target=ask_user)
thread3 = Thread(target=complex_calc)

start = time.time()
thread1.start()
thread2.start()
thread3.start()

# blocking operations, below we tell our main thread,
# i.e. above, for thread1 and thread2 to finish
thread1.join()
thread2.join()
thread3.join()
print(f"Three thread total time: {time.time() - start}")

## if we are doing things that require the CPU all the time,
# it is pointless to use Threads in Python. There are better things