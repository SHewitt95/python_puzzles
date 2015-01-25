'''
By considering the terms in the Fibonacci 
sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
'''
even_sum = 0 # Sum of even-valued terms.
fib = 0 # Current Fibonacci number
number1 = 1
number2 = 0
while (fib < 4000000):
    fib = number1 + number2 # Calculates fib number
    number1 = number2 # Moves lesser fib sequence number forward
    number2 = fib # Moves greater fib sequence number forward
    if (fib % 2 == 0):
        even_sum = even_sum + fib

print(even_sum)
