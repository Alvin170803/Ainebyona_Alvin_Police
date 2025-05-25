#factorial assignment from class
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Find factorial of 5
result = factorial(5)

print("Factorial of 5 is:", result)
