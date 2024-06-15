import threading

def display_forward():
    for i in range(1, 51):
        print("Thread1:", i)

def display_reverse():
    for i in range(50, 0, -1):
        print("Thread2:", i)

thread1 = threading.Thread(target=display_forward)
thread2 = threading.Thread(target=display_reverse)

thread1.start()
thread1.join()  
thread2.start()
thread2.join()

print("Exit from main")