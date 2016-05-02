# import string
import sys
from collections import defaultdict
import operator
import re
from collections import Counter


def most_beautiful_string(s):
    # make a list
    s = re.sub('[^a-z]', '',  s.lower())
    letters = list(s)

    # find freq high to low
    l_dict = defaultdict(int)

    for l in letters:
        l_dict[l] += 1

    # assign values (26, 25, )
    sorted_dict = sorted(l_dict.items(), key=operator.itemgetter(1),
                         reverse=True)

    # return sum
    sum_of_values = 0
    value = 26
    for _, cnt in sorted_dict:
        sum_of_values += value * cnt
        value -= 1


    return sum_of_values

filename = sys.argv[1]
with open(filename, 'r') as f:
    lines = f.readlines()

for line in lines:
    print most_beautiful_string(line)

# other ways

counts = sorted([v for k, v in l_dict.items()], reverse=True)
values = range(26, 0, -1)


counter = Counter(re.sub("[^a-z]", '', s))
counter.most_common()
