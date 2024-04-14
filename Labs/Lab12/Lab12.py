# #RQ1
class Cheer:

    """
    >>> UC = Cheer("Bearcats")
    >>> for c in UC:
    ...     print(c)
    ...
    Give me an B
    Give me an e
    Give me an a
    Give me an r
    Give me an c
    Give me an a
    Give me an t
    Give me an s
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, toCheer):
        self.phrase = toCheer

    def __iter__(self):
        self.printIndex = 0 # Start printing and hold the index
        return self

    def __next__(self):
        if(self.printIndex >= len(self.phrase)):
            raise StopIteration # YOU NEED TO LEAVE

        letterCheer = "Give me an " + self.phrase[self.printIndex]
        self.printIndex += 1
        return letterCheer


#RQ2
class Countdown:
    """
    An iterator that counts down from N to 0.
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in Countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    # "*** YOUR CODE HERE ***"
    def __init__(self, upperBound):
        self.upper = upperBound
    
    def __iter__(self):
        return self

    def __next__(self):
        if(self.upper < 0):
            raise StopIteration
        self.upper -= 1 # sorry for doing this, no post increment :/
        return self.upper + 1
    


##############
# Generators #
##############

# RQ3
def evens():
    """A generator function that yields the infinite sequence of all even natural
    numbers, starting at 1. Had to confirm type of gen fn in testing

    >>> m = evens()
    >>> type(m)
    <class 'generator'>

    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    # print("started evens generator")
    i = 2
    while True:
        yield i
        i += 2
#  yeild // Stops execution of fn and returns value and next will continue

# Extra question?
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.
    "*** YOUR CODE HERE ***"

    # >>> m = naturals()
    # >>> type(m)
    # <class 'generator'>

    # >>> [next(m) for _ in range(10)]
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # """
    i = 1
    while 1:
        yield i
        i += 1


#RQ4
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>

    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    # >>> m = scale(naturals(), 2)
    for item in s:
        item *= k
        yield item

# RQ5
def countdown(n):
    """
    A generator that counts down from N to 0.
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    while n >= 0:
        yield n
        n -= 1


# RQ6
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    while n != 1:
        yield n
        if(n %2 == 0):
            n = n // 2
        else:
            n = (n * 3) + 1
    yield 1 # slap n in the face

import doctest
if __name__ == '__main__':
    # read_eval_print_loop()
    doctest.testmod(verbose=True)
    # doctest.testmod()