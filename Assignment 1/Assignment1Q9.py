
def Even():
    for i in range(1 , 21):
        if i % 2 == 0:
            print(i , end = " ")
            if i == 21:
                break

def main():
    Even()
if __name__ =="__main__":
    main()
