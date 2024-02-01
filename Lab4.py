##Lab04 Required Questions ##
# Cameron Pocisk
#########
# Lists #
#########

# [start : stop : step]

# RQ1
def cascade(lst):
    """Returns the cascade of the given list running forward and back.

    >>> cascade([1, 2, 3, 4])
    [1, 2, 3, 4, 4, 3, 2, 1]
    """
    return lst + lst[::-1]

# RQ2
def maptwice(fn, seq):
    """Applies fn twice onto each element in seq and returns the resulting list.

    >>> maptwice(lambda x: x*x, [1, 2, 3])
    [1, 16, 81]
    """
    for i in range (len(seq)):
        seq[i] = fn(fn(seq[i]))
    return seq

#RQ3
def filterout(pred, seq):
    """Keeps elements in seq only if they do not satisfy pred.

    >>> filterout(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [1, 3]
    """
    #Recursive :D
    if len(seq) == 0:
        return []
    if(not pred(seq[0])):
        return [seq[0]] + filterout(pred, seq[1:])
    else:
        return filterout(pred, seq[1:])
        
#RQ4
def comp(n, pred):
    """ Uses a one line list comprehension to return list of the first n integers (0...n-1) which satisfy the predicate, pred.
    >>> comp(7, lambda x: x%2 ==0)
    [0, 2, 4, 6]
    """
    #newlist = [expression for item in iterable if condition == True]
    return [item for item in list(range(n)) if pred(item)]


#RQ5
def flatten(lst):
    """ Takes a nested list and "flattens" it.
    
    >>> flatten([1, 2, 3]) 
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] 
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> lst = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(lst)
    [1, 2, 3, 4, 5, 6]
    """
    # sorry but I am so goated for this (rly easy activity in C/cpp)
    if(type(lst) == list and len(lst) == 0):
       return []
    
    if(type(lst)!= list):
       return [lst]
    else:
       return flatten(lst[0]) + flatten(lst[1:])


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)