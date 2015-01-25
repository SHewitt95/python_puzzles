'''
Puzzle: Find the largest palindrome made from the product of two 3-digit numbers.
'''
def is_palindrome(n):
    ''' Checks if number n is a palindrome '''
    number_string = str(n)

    #Returns false if the number's reverse is not equal to original
    if (number_string[::-1] != number_string):
        
        #number_string[begin:end:step]
        #by leaving 'begin' and 'end' off and specifying a 'step' of -1,
        #it reverses a string.
        
        return False

    return True

product = 0
largest_number = 0

#These two numbers must have same number of digits
largest_digit_number = 999
smallest_digit_number = 100

for i in range(largest_digit_number, smallest_digit_number, -1): # Establishes multiplicand
    for j in range(largest_digit_number, smallest_digit_number, -1): # Establishes multiplier
        product = i * j
        if (is_palindrome(product) and product > largest_number):
            largest_number = product
            
print(largest_number) # Prints answer
    
    
    
