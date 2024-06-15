def sum_factors(n):
    if n < 1:
        return "Number should be greater than 0"
    factor_sum = 1
    
    for i in range(2, int(n**0.5) + 1):
        
        if n % i == 0:
           
            if n // i == i:
                factor_sum += i
           
            else:
                factor_sum += i + n // i
    
    return factor_sum

def main():
    num = int(input("Enter a number: "))
    result = sum_factors(num)
    print("Sum of factors of", num, "is:", result)

if __name__ == "__main__":
    main()