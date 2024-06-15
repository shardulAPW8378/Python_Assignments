
def ChkNumBy5(num):
    if num % 5 == 0:
        return True
    else:
        return False

   
def main():
    Number = int (input("Enter The Number :"))
    result = ChkNumBy5(Number)
    print(result)
if __name__ =="__main__":
    main()
