def not_string(str):
    """
    Given a string, return a new string where "not" has been added to the front.
    However, if the string already begins with "not", return the string unchanged.
    not_string("cat") returns "notcat"
    not_string("not") returns not
    """ 
    if str[:3] == 'not':
        return str
    return 'not' + str

print(not_string('not'))
print(not_string('cat'))

print()

def swap(lst):
    """
    Given a list, find the minimum element in the list and swap it with the first
    element in the list. Return the list.
    swap([5,4,3,2,1]) returns [1, 4, 3, 2, 5]
    """
    x = min(lst)
    index = lst.index(x)
    temp = lst[0]
    lst[0] = x
    lst[index] = temp
    return lst

print(swap([5,4,3,2,1]))

def count_spaces(string):
    """
    Use comprehension to count the number of spaces in a string.
    *** Important: your code must use comprehensions and should not be more than
    two lines of code including the return statement ***
    count_spaces("the cow jumped over the moon") returns 5
    """
    