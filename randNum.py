# my attempt at making some sort of randomness

randPlaces = 4 # how many places?
DIGITS = 10000 # how many digits of pi

# function to generate pi, taken from stack overflow
# can't remember what it was called
def pi_digits(x):
    """Generate x digits of Pi."""
    k,a,b,a1,b1 = 2,4,1,12,4
    while x > 0:
        p,q,k = k * k, 2 * k + 1, k + 1
        a,b,a1,b1 = a1, b1, p*a + q*a1, p*b + q*b1
        d,d1 = a/b, a1/b1
        while d == d1 and x > 0:
            yield int(d)
            x -= 1
            a,a1 = 10*(a % b), 10*(a1 % b1)
            d,d1 = a/b, a1/b1

digits = [str(n) for n in list(pi_digits(DIGITS))] 
digits = ''.join(digits) # join list into single string, we lose the whole '3'
import time # import library for time

for i in range(100): # generate 100 numbers
    time.sleep(.1) # sleep to introduce more time diffs
    timeSeed = str(time.time()) # take nano second time
    timeSeed = ''.join(timeSeed.split('.')) #split/join on the '.'
    timeSeed = timeSeed[-4:] # select last 4 digits

    randNum = int(digits[int(timeSeed):int(timeSeed)+int(randPlaces)]) # select digits

    print(randNum) # print number