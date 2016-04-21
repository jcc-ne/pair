import numpy as np
import matplotlib.pyplot as plt


def funct(xarray, n):
    var = (xarray - n) ** 2
    return sum(var)

xarray = np.array([2., 7., 1., 5., 10.])
ans = np.zeros(100)
narray = np.arange(0, 10., 0.1)

for i, n in enumerate(narray):
    ans[i] = funct(xarray, n)

print "Min is", ans.min(),
plt.plot(narray, ans)

def general_solution(xarray):
    return xarray.mean()

print "Mininum distance is viable by finding the mean", xarray.mean()

