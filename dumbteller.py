import numpy as np
import matplotlib.pyplot as plt


def swapped(y):
    """ x: cents
        y: dollars
        (orig)
    """
    # equation to solve
    x = 199./98. * y -1./98.
    return x

ans_x = []
ans_y = []

for y in range(0, 100):
    x = swapped(y)

    # check if x is integer
    if x == np.floor(x):
        ans_x.append(x)
        ans_y.append(y)

y_array = np.arange(0, 100)
x_array = swapped(y_array)

plt.plot(ans_x, ans_y, 'o', markersize=10, label='integer')
plt.plot(x_array, y_array, '--', label='virtual money line')
plt.xlabel('x (orig. cents)')
plt.ylabel('y (orig. dollars)')
plt.legend(loc='upper left')
plt.show()
