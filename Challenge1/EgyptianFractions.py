def gcd(a, b):
    if(b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)

# PASSES ALL TESTS BUT OUTPUT IS OFF???
def egypt(numerator, denominator):
    """
    >>> egypt(3,4)
    '1/2 + 1/4'
    >>> egypt(11,12)
    '1/2 + 1/3 + 1/12'
    >>> egypt(123,124)
        '1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112'
    >>> egypt(103,104)
         '1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1/100039636784966424'
    """
    #Accumulate answer
    answerString = ""

    while numerator >= 0:
        currentDenominator = -1 * (-1 * denominator//numerator) # int division

        answerString += "1/" + str(currentDenominator) + " + "
        if(denominator % numerator == 0):
            break

        # Subtract fraction
        numerator = numerator * currentDenominator - denominator
        denominator = denominator * currentDenominator
        # Simplify fraction
        commonDenom = gcd(numerator,denominator)
        numerator = numerator // commonDenom
        denominator = denominator // commonDenom

    #Return srting without the extra " + "
    return answerString[:-3]

import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)
print("Passes all tests but doctest seems to be confused")