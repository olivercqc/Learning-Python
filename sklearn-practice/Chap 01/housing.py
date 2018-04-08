import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def plot_feature_importances(feature_importances, title, feature_names):
    feature_importances = 100.0 * (feature_importances / max(feature_importances))
    index_sorted = np.flipud(np.argsort(feature_importances))
    pos = np.arange(index_sorted.shape[0])

    plt.figure()
    plt.bar(pos, feature_importances[index_sorted], align='center')
    plt.xticks(pos, feature_names[index_sorted])
    plt.ylabel('Relative Importance')
    plt.title(title)
    plt.show()

if __name__ == '__main__':

    housing_data = load_boston()
    # X, y = shuffle(housing_data.data, housing_data.target, random_state=7)
    X_train, X_test, y_train, y_test = train_test_split(housing_data.data, housing_data.target, random_state=0)

    dt_regressor = DecisionTreeRegressor(max_depth=4)
    dt_regressor.fit(X_train, y_train)

    ab_regressor = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4), n_estimators=400, random_state=7)
    ab_regressor.fit(X_train, y_train)

    y_pred_dt = dt_regressor.predict(X_test)
    mse = mean_squared_error(y_test, y_pred_dt)
    evs = explained_variance_score(y_test, y_pred_dt)
    print("\n#### Decision Tree performance ####")
    print("Mean Squared error =", round(mse, 2))
    print("Explained varience score =", round(evs, 2))

    y_pred_ab = ab_regressor.predict(X_test)
    mse = mean_squared_error(y_test, y_pred_ab)
    evs = explained_variance_score(y_test, y_pred_ab)
    print("\n#### Adaboost performance ####")
    print("Mean Squared error =", round(mse, 2))
    print("Explained varience score =", round(evs, 2))

    plot_feature_importances(dt_regressor.feature_importances_, "Decision Tree regressor", housing_data.feature_names)
    plot_feature_importances(ab_regressor.feature_importances_, "Adaboost regressor", housing_data.feature_names)

