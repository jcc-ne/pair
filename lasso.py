from sklearn import linear_model
from sklearn.linear_model import LassoCV
from sklearn.linear_model import LassoCV
import pandas as pd

df = pd.read_csv('Lasso_practice_data.csv')
y = df.iloc[:, -1].values
X = df.iloc[:, :-1].values

def runlasso(X_train, X_test, y_train, y_test, alpha):
    clf = linear_model.Lasso(alpha = alpha)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    SSE = ((y_pred - y_test)**2).sum()
    return SSE

alpha_dict = dict()

for alpha in np.linspace(0, 0.1, 500):

    kf = KFold(2000, n_folds = 5, random_state = 42)
    SSE_list = []

    for train_index, test_index in kf:
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        SSE_list.append(runlasso(X_train, X_test, y_train, y_test, alpha))

    alpha_dict[alpha] = np.mean(SSE_list)


# runlassocv

lassocv = linear_model.LassoCV(cv=5)
lassocv.fit(X, y)
print lassocv.alpha_

