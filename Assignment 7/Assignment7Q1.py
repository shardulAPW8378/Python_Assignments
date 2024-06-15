class Demo:
    Value = 10  

    def __init__(self, no1, no2):
        self.no1 = no1  
        self.no2 = no2  

    def Fun(self):
        print(f"Values of instance variables: {self.no1}, {self.no2}")

    def Gun(self):
        print(f"Class variable Value: {Demo.Value}")

def main():


    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)


    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()