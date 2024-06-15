import threading


def evenlist(lst):
    sum_even = sum([x for x in lst if x % 2 == 0])
    print("Sum of even elements:", sum_even)


def oddlist(lst):
    sum_odd = sum([x for x in lst if x % 2 != 0])
    print("Sum of odd elements:", sum_odd)


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


evenlist_thread = threading.Thread(target=evenlist, args=(input_list,))
oddlist_thread = threading.Thread(target=oddlist, args=(input_list,))


evenlist_thread.start()
oddlist_thread.start()


evenlist_thread.join()
oddlist_thread.join()

print("Exit from main")