import threading

def small_chars_count(string):
    count = sum(1 for char in string if char.islower())
    print(f"Thread ID: {threading.get_ident()}, Name: {threading.current_thread().name}")
    print("Number of small characters:", count)

def capital_chars_count(string):
    count = sum(1 for char in string if char.isupper())
    print(f"Thread ID: {threading.get_ident()}, Name: {threading.current_thread().name}")
    print("Number of capital characters:", count)

def digits_count(string):
    count = sum(1 for char in string if char.isdigit())
    print(f"Thread ID: {threading.get_ident()}, Name: {threading.current_thread().name}")
    print("Number of digits:", count)

string = "Shardul Tapkire 8378909261234"

small_thread = threading.Thread(target=small_chars_count, args=(string,))
capital_thread = threading.Thread(target=capital_chars_count, args=(string,))
digits_thread = threading.Thread(target=digits_count, args=(string,))

small_thread.start()
capital_thread.start()
digits_thread.start()

small_thread.join()
capital_thread.join()
digits_thread.join()

print("Exit from main")