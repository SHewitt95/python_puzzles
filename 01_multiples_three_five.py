sum = 0
max_number = 999

for i in range(max_number, 0, -1):
    if (i % 3 == 0 or i % 5 == 0):
        sum += i

print(sum)
