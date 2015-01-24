even_sum = 0
fib = 0
number1 = 1
number2 = 0
while (fib < 4000000):
    fib = number1 + number2
    number1 = number2
    number2 = fib
    if (fib % 2 == 0):
        even_sum = even_sum + fib

print(even_sum)
