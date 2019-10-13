"""
Given two strings, return "YES" iff the strings share a substring,
else return "NO"
"""

# Complete the twoStrings function below.
def twoStrings(s1, s2):

    lst_s1 = createList(s1)
    lst_s2 = createList(s2)

    match = "NO"

    for i in range(len(lst_s1)):
        if lst_s1[i] in lst_s2:
            match = "YES"
            break
    
    return match


def createList(s):
    lst= []
    for char in s:
        if char not in lst:
            lst.append(char)
    lst.sort()
    return lst