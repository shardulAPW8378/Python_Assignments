import threading

def Even_number():
    for i in range (2,21,2):
        print("Even" , i)

def Odd_number():
    for i in range (1,20,2):
        print("Odd" , i)

even_thread = threading.Thread(target =  Even_number)

odd_thread = threading.Thread(target = Odd_number)

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()