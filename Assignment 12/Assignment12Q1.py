import psutil

def Displayprocess():
    print("List Of Running Process Are :")
    print("____________________________________________")

    for proc in psutil.process_iter(['pid', 'name', 'username']):
        print(proc.info)

    print("____________________________________________")

def main():
    Displayprocess()

if __name__ == "__main__":
    main()
