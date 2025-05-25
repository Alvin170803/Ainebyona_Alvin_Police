#2nd assignment from exception handling class
while True:
    try:
        num1 =float(input("Enter first number: "))
        num2 =float(input("Enter second number: "))
        
        result= num1/num2
    except ZeroDivisionError:
        print("Error caused by dividing the first number by zero.Please use a non-zero second num. ")
    except ValueError:
        print("Error due to invalid input that is not numeric.")
    else:
        print(f"Final Result: {result} ")
        
        break