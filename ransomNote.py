""" 
Given a list of words in a magazine, determine if a given ransom note can be
constructed from the magazine.

Print 'Yes' iff it can be constructed, else print 'No'
"""

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    
    d = createDict(magazine)
    
    complete = 'Yes'

    for word in note:
        if word[0] not in d or word not in d[word[0]]:
            complete = 'No'
            break
        else:
            d[word[0]].remove(word)
    
    print(complete)


def createDict(magazine):
    d = {}

    for word in magazine:
        if word[0] not in d:
            d[word[0]] = [word]
        else:
            d[word[0]].append(word)
    
    return d