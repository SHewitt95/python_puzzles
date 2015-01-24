divisor = 2
my_number = 600851475143

'''
The function isprime() was found at this website:
https://www.daniweb.com/software-development/python/code/216880/check-if-a-number-is-a-prime-number-python
'''

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

while (divisor <= my_number):
    if (my_number % divisor == 0):
        if (isprime(divisor)):
            print(divisor)
    divisor += 1


