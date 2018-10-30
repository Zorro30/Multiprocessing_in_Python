import threading

def print_even(x):

    for i in range(x):
        if i%2 == 0:
            print('{} is Even'.format(i))

def print_odd(x):

    for i in range(x):
        if i%2 != 0:
            print('{} is Odd'.format(i))

def main():

    global x

    x = [10]
    first_thread = threading.Thread(target=print_even, args=x)
    first_thread.start()

    second_thread = threading.Thread(target=print_odd, args=x)
    second_thread.start()

main()