import threading

def print_even(x):

    lock.acquire()
    try:
        for i in range(x):
            if i%2 == 0:
                print('{} is Even'.format(i))
    finally:
        lock.release()

def print_odd(x):

    lock.acquire()
    try:
        for i in range(x):
            if i%2 != 0:
                print('{} is Odd'.format(i))
    finally:
        lock.release()

def main():

    global x
    global lock
    lock = threading.Lock()

    x = [10]
    first_thread = threading.Thread(target=print_even, args=x)
    first_thread.start()

    second_thread = threading.Thread(target=print_odd, args=x)
    second_thread.start()

main()