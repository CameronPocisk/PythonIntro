## Lab 8: Trees  ##
# Four Required Questions 


# pyTunes
def make_pytunes(username):
    """Return a pyTunes tree as shown in the diagram with USERNAME as the value
    of the root.

    >>> pytunes = make_pytunes('i_love_music') 
    >>> print_tree(pytunes)
    i_love_music
      pop
        justin bieber
          single
            what do you mean?
        2024 pop mashup
      trance
        darude
          sandstorm
    """
    pyTunesTree = tree(username, [tree("pop",
                                    [tree("justin bieber", 
                                        [tree("single", 
                                            [tree("what do you mean?")])]), 
                                        tree("2024 pop mashup")]),
                                  tree("trance",
                                    [tree("darude", 
                                        [tree("sandstorm")])])])
    # print_tree(pyTunesTree)
    return pyTunesTree

# t = tree(1,
#          [tree(2),
#           tree(3,
#                [tree(4),
#                 tree(5)]),
#           tree(6,
#                [tree(7)])])
#    1
#  / | \
# 2  3  6
#   / \  \
#  4   5  7



def num_songs(t):
    """Return the number of songs in the pyTunes tree, t.

    >>> pytunes = make_pytunes('i_love_music')
    >>> num_songs(pytunes)
    3
    """
    # base case for leaf
    if(is_leaf(t)):
        return 1
    #itterate w/ recirsion through rest of tree
    curSum = 0
    for branch in branches(t):
        curSum += num_songs(branch)
    return curSum

def add_song(t, song, category):
    """Returns a new tree with SONG added to CATEGORY. Assume the CATEGORY
    already exists.

    >>> indie_tunes = tree('indie_tunes',
    ...                  [tree('indie',
    ...                    [tree('vance joy',
    ...                       [tree('riptide')])])])
    >>> new_indie = add_song(indie_tunes, 'georgia', 'vance joy')
    >>> print_tree(new_indie)
    indie_tunes
      indie
        vance joy
          riptide
          georgia
    """
    #base case
    if root(t) == category:
        return tree(root(t), branches(t) + [tree(song)])
    else:
        curBranch = []
        
        for branch in branches(t):
            curBranch.append(add_song(branch, song, category))
        
        return tree(root(t), curBranch)

# Tree ADT
def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, indent=0):
    # """Print a representation of this tree in which each node is
    # indented by two spaces times its depth from the entry.

    # >>> print_tree(tree(1))
    # 1
    # >>> print_tree(tree(1, [tree(2)]))
    # 1
    #   2
    # >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    # >>> print_tree(numbers)
    # 1
    #   2
    #   3
    #     4
    #     5
    #   6
    #     7
    # """
    print('  ' * indent + str(root(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    # """Returns a copy of t. Only for testing purposes.

    # >>> t = tree(5)
    # >>> copy = copy_tree(t)
    # >>> t = tree(6)
    # >>> print_tree(copy)
    # 5
    # """
    return tree(root(t), [copy_tree(b) for b in branches(t)])


def delete(t, target):
    """Returns the tree that results from deleting TARGET from t. If TARGET is
    a category, delete everything inside of it.

    >>> my_account = tree('kpop_king',
    ...                    [tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                            tree('uptown funk'),
    ...                            tree('see you again')])])
    >>> new = delete(my_account, 'pop')
    >>> print_tree(new)
    kpop_king
      korean
        gangnam style
        wedding dress
    """
    if root(t) == target:
        return None
    else:
        curBranch = []
        for branch in branches(t):
            newBranch = delete(branch, target)
            if newBranch != None:
                curBranch.append(newBranch)
                
        return tree(root(t), curBranch)


import doctest
if __name__ == '__main__':
    # read_eval_print_loop()
    doctest.testmod(verbose=True)