import numpy as np
from sklearn.naive_bayes import GaussianNB
from logistic_regression import plot_classfier
from sklearn.model_selection import train_test_split
if __name__ == "__main__":
    input_file = "data_multivar.txt"
    X = []
    y = []
    with open (input_file, "r") as f:
        for line in f.readlines():
            data = [float(x) for x in line.split(",")]
            X.append(data[:-1])
            y.append(data[-1])
    X = np.array(X)
    y = np.array(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=5)
    
    gaussiannb_clf = GaussianNB()
    gaussiannb_clf.fit(X, y)
    y_pred = gaussiannb_clf.predict(X)

    gaussiannb_new_clf = GaussianNB()
    gaussiannb_new_clf.fit(X_train, y_train)
    y_test_pred = gaussiannb_new_clf.predict(X_test)

    # accuracy = 100.0 * (y == y_pred).sum() / X.shape[0]
    accuracy = 100.0 * (y_test == y_test_pred).sum() / X_test.shape[0]
    print("Accuracy of the classifier =", round(accuracy, 2), "%")
    plot_classfier(gaussiannb_new_clf, X_test, y_test)