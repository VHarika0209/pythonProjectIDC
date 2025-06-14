def find_factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*find_factorial(n-1)

number = int(input("Enter a number to find its factorial:"))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = find_factorial(number)
    print(f"Factorial of {number} is {result}.")