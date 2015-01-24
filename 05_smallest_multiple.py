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
