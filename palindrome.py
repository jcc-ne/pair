def palindrome(listw):
    # time 2N
    reverse = listw[::-1]
    if listw == reverse:
        print 'yes'
    else:
        print 'no'

def palindrome2(listw):
    # time N
    half_text = len(text) / 2 + 1
    reverse = listw[::-1][0:half_text]
    if listw == reverse:
        print 'yes'
    else:
        print 'no'


def canyouspell(bagofwords, lword):
    """ this will take time O(N^2), workaround: dictionary,
    which is constant lookup """
    # TODO: empty strings?
    if len(lword) > len(bagofwords):
        return('no')
    for w in lword.strip():
        if w in bagofwords:
            bagofwords.remove(w)
        else:
            return('no')
    return('yes')

from collections import defaultdict
def canyouspell2(mylist, word):
    mydict = defaultdict(int)
    for char in mylist:
        mydict[char] += 1
    for char in word:
        mydict[char] -= 1
        if mydict[char] < 0:
            return False
    return True

# using array, ord(char) will give the ascii value 'a'=97

from array import array

def canyouspell3(mylist, word):
    ar = array([0]) * 26
    for char in mylist:
        ar[ord(char) - 97] += 1
    for char in word:
        ar[ord(char) - 97] -= 1
        if ar[ord(char) - 97] < 0:
            return False
    return True
