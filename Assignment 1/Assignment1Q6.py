
def ChkNum():
    Num = int(input("Enter The Number : "))

    if Num > 0 :
        print("The Number Is Postive" ,Num)

    elif Num < 0 :
        print("The Number Is Negative" , Num) 
    
    else:
        print("The Number Is Zero Number" , Num)

def main():
    ChkNum()
if __name__ =="__main__":
    main()
