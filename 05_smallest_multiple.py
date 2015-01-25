'''
2520 is the smallest number that can be divided 
by each of the numbers from 1 to 10 without any remainder.

Puzzle: What is the smallest positive number that is 
evenly divisible by all of the numbers from 1 to 20?
'''
def check_num(num):
    for i in range(11,21):
        if (num % i == 0):
            continue
        else:
            return False
    return True

x = 2520
while not check_num(x):
    x += 2520

print(x)

'''
Solution found in this video:
https://www.youtube.com/watch?v=EMTcsNMFS_g
'''
