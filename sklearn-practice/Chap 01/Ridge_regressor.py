import numpy as np
filename = "data_multivar.txt"
X = []
y = []
with open (filename, 'r') as f:
    for line in f.readlines():
        data = [float(i) for i in line.split(',')]
        xt, yt = data[:-1], data[-1]
        X.append(xt)
        y.append(yt)
# num_training = int(0.8 * len(X))
# num_test = len(X) - num_training
# X_train = np.array(X[:num_training])
# y_train = np.array(y[:num_training])

# X_test = np.array(X[num_training:])
# y_test = np.array(y[num_training:])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

from sklearn import linear_model
ridge_regressor = linear_model.Ridge(alpha=0.001, fit_intercept=True, max_iter=100000)
ridge_regressor.fit(X_train, y_train)
y_test_pred_ridge = ridge_regressor.predict(X_test)
import sklearn.metrics as sm
print("Mean absolute error =", round(sm.mean_absolute_error(y_test, y_test_pred_ridge), 2))
print("Mean squared error =", round(sm.mean_squared_error(y_test, y_test_pred_ridge), 2))
print("Median absolute error =", round(sm.median_absolute_error(y_test, y_test_pred_ridge), 2))
print("Explain varience score =", round(sm.explained_variance_score(y_test, y_test_pred_ridge), 2))
print("R2 score =", round(sm.r2_score(y_test, y_test_pred_ridge), 2))

