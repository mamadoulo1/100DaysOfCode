# Write your code below this line 👇


# Write your code above this line 👆
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            return is_prime
    return is_prime

# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)
