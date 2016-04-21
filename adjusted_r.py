# pair problem week2 day4

import statsmodels.formula.api as smf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


n_feature = 20


def rand_fit(n_feature):
    Xy = np.random.randn(200, n_feature + 1)

    cols_x = ['X{}'.format(x) for x in range(1, n_feature + 1)]
    cols = ['Y'] + cols_x
    df = pd.DataFrame(Xy, columns=cols)

    r_formula = ' + '.join(cols_x)
    r_formula = 'Y ~ ' + r_formula

    lm1 = smf.ols(r_formula, data=df)
    fit1 = lm1.fit()

    valid_fit = False

    # check pvalues < 0.05
    if (fit1.pvalues < 0.05).sum() > 0:
        valid_fit = True

    # return r_square & r_square_adj
    return (valid_fit, fit1.rsquared, fit1.rsquared_adj)
    # print fit1.summary()


def rand_fit_valid(n_feature):
    valid_fit = False
    while not valid_fit:
        valid_fit, r_square, r_square_adj = rand_fit(int(n_feature))
    return (r_square, r_square_adj)

results = []
nfeature_list = np.linspace(1, 100, 100)
results = np.zeros((len(nfeature_list), 2))
for i, n in enumerate(nfeature_list):
    r_square, r_square_adj = rand_fit_valid(int(n))
    results[i-1, :] = (r_square, r_square_adj)

rsquared = results[:, 0]
rsquared_adj = results[:, 1]
plt.plot(nfeature_list, rsquared, label='R-squared')
plt.plot(nfeature_list, rsquared_adj, label='R-squared-adj')
plt.legend(loc='upper left')
plt.show()
