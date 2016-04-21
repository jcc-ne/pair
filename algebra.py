import numpy as np

# <markdowncell>

# ## Pair problem solve linear algebra

# <codecell>
def algebra_solve(X, y):
    """ [x][a] = [y], return a """
    mat_X = np.matrix(X)
    mat_y = np.matrix(y)

    a = np.linalg.linalg.solve(mat_X, mat_y)

    return a

# <codecell>
algebra_solve([[2]], [8])

# <markdowncell>

# Problem A:
#
# ```
# X = [[2]]        y = [8]
# ```
#
#
# Problem B:
#
# ```
# X = [[0]]        y = [8]
# ```
#
#
# Problem C:
#
# ```
# X = [[2, 4]]     y = [8]
# ```

# <markdowncell>>
# ###Problem D:
#
# ```
# X = [[2, 4],     y = [8,
#      [0, 1]]          3]
# ```

# <codecell>

X = [[2, 4], [0, 1]]
y = [8, 3]
algebra_solve(X, y)

# Problem E:
#
# ```
# X = [[2, 4],     y = [8,
#      [0, 1],          3,
#      [9, 5]]          1]
# ```
#
#
# Problem F:
#
# ```
# X = [[2, 2],     y = [4,
#      [3, 3]]          6]
# ```
#
#
# Problem G:
#
# ```
# X = [['dog'],    y = [8,
#      ['cat']]         6]
# ```
#
#
# Problem H:
#
# ```
# X = [[1, 0],    y = [8,
#      [0, 1]]         6]
# ```
#
#
# Problem I:
#
# ```
# X = [[1, 1, 0],    y = [8,
#      [1, 0, 1]]         6]
# ```
#
#
# Problem J:
#
# ```
# X = [[1, 0],    y = [8,
#      [1, 1]]         6]
# ```


# <codecell>
