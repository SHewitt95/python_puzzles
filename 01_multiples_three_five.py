'''
Puzzle: Find the sum of all the multiples of 3 or 5 below 1000.
'''
sum = 0
max_number = 999

for i in range(max_number, 0, -1): # Counts down from max_number to 0.

    # If the number (i) is divisible by 3 or 5, increment sum by i.
    if (i % 3 == 0 or i % 5 == 0):
        sum += i

print(sum)
