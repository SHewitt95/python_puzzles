import time
'''
Plan: find longest substring of 13 numbers between 2 zeros.
Most likely, it should yield the greatest product.
'''

big_number = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

##############################################################################
def find_substring_of_thirteen(start):
    
    global big_number
    first_thirteen = big_number[start : start+13]
    new_thirteen = '0'

    new_start = 0
    while (new_thirteen.find('0') != -1):
        new_start = new_thirteen.find('0')+1
        new_thirteen = big_number[new_start : new_start+13]
        big_number = big_number[new_start :]

    return new_thirteen
##############################################################################
def largest_product():
    
    global big_number
    
    largest_product = 1
    while (len(big_number) > 12):
        substring = find_substring_of_thirteen(0)
        my_product = product(substring)
        if (my_product > largest_product):
            largest_product = my_product

    return largest_product
############################################################################## 
def product(substring):

    product = 1
    for i in range(0, len(substring)):
        product = product * int(substring[i])
    return product
##############################################################################

time_start = time.time()
solution = largest_product()
time_end = (time.time() - time_start) * 1000.0 # Time in milliseconds

print("The product %s was found in %s milliseconds." %(solution, time_end))
