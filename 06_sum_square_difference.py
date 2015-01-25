'''
Puzzle: Find the difference between the sum of the squares of 
the first one hundred natural numbers and the square of the sum
of the first hundred natural numbers.
'''
def sum_of_squares(numbers):
    return sum([i**2 for i in range(1, numbers+1)])

def square_of_sum(numbers):
    return sum(range(1, numbers+1)) ** 2

number_of_numbers = 100
print(square_of_sum(number_of_numbers) - sum_of_squares(number_of_numbers))

'''
Equation found at this site:
http://codereview.stackexchange.com/questions/
58460/sum-of-squares-square-of-sum-difference

max = 100
print(((max-1)*(max)*(max+1)*(3*max + 2))/12)
'''