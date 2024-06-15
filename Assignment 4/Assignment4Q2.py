multiply = lambda A , B : A*B

def main():
    A = int(input("ENTER THE FIRST NUMBER : ")) 
    B = int(input("ENTER THE SECOND NUMBER : ")) 

    RESULT = multiply(A,B)
    print (f"OUTPUT : {RESULT}")

if __name__ == "__main__":
    main()