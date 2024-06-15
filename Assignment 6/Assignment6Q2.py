import threading


def evenfactor(num):
    sum_even = 0
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 == 0:
            sum_even += i
    print("Sum of even factors:", sum_even)


def oddfactor(num):
    sum_odd = 0
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 != 0:
            sum_odd += i
    print("Sum of odd factors:", sum_odd)


evenfactor_thread = threading.Thread(target=evenfactor, args=(24,))
oddfactor_thread = threading.Thread(target=oddfactor, args=(24,))


evenfactor_thread.start()
oddfactor_thread.start()


evenfactor_thread.join()
oddfactor_thread.join()

print("Exit from main")