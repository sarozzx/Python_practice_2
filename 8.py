# Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.

def is_prime(x):
    if x==2:
        return True
    z=0
    for y in range(2,x):
        if(x%y==0):
            return False
    return True


print(is_prime(6))