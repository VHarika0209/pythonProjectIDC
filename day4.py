# check given number is Prime
user_number = int(input("Enter the number:"))

def is_prime(number):
    if number < 1:
        return f"Given {number} is not a prime."
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is divisible by {i}, so it is not a prime number.")
            break
        else:
            continue
    return f"Given {number} is a prime."

print(is_prime(user_number))

