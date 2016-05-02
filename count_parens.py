import re


def right_parens(s):

    # clean the string to "(" ")" left
    s = re.sub('[^()]', '', s)

    # count from left to right
    cnt_o = 0
    cnt_c = 0

    for i in s:
        if i == '(':
            cnt_o += 1
        elif i == ')':
            cnt_c += 1
        if cnt_c > cnt_o:
            return False
    if cnt_o != cnt_c:
        return False
    return True


def checkBrackets(text):
    text = re.sub('[^()]', '', text)
    while '()' in text:
        text = text.replace('()', '')
    return not text

def checkBrackets_v2(text):
    if '()' in text:
        return checkBrackets_v2(text.replace('()', ''))
    else:
        return not text

