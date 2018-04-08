import csv
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, explained_variance_score

from housing import plot_feature_importances

def load_dataset(filename):
    file_reader = csv.reader(open(filename, 'r'), delimiter=',')
    X, y = [], []
    for row in file_reader:
        X.append(row[2:13])
        y.append(row[-1])

    feature_names = np.array(X[0])
    return np.array(X[1:]).astype(np.float32), np.array(y[1:]).astype(np.float32), feature_names
 
if __name__=='__main__':
    X, y, feature_names = load_dataset("bike_day.csv")
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    rf_regressor = RandomForestRegressor(n_estimators=1000, max_depth=40, min_samples_split=2)
    rf_regressor.fit(X_train, y_train)

    y_pred = rf_regressor.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    evs = explained_variance_score(y_test, y_pred)
    print("\n### Random Forest regressor preformance ###")
    print("Mean squared error =", round(mse, 2))
    print("Explained varience score =", round(evs, 2))

    plot_feature_importances(rf_regressor.feature_importances_, "Random Forest regressor", feature_names)
