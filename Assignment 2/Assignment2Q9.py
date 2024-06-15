def Count_Digits(n):
    return len(str(n))


def main():
    num = int(input("Enter A Number : "))
    result = Count_Digits(num)
    print("Number Of Digits In ", num , "is" , result)
if __name__ =="__main__":
    main()