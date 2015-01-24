def sum_of_squares(max_n):
    return sum([i**2 for i in range(1, max_n+1)])

def square_of_sum(max_n):
    return sum(range(1, max_n+1)) ** 2

print(square_of_sum(100) - sum_of_squares(100))

'''
Equation found at this site:
http://codereview.stackexchange.com/questions/
58460/sum-of-squares-square-of-sum-difference
'''
max = 100
print(((max-1)*(max)*(max+1)*(3*max + 2))/12)
