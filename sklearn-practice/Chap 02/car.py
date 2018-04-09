from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
import numpy as np

if __name__ == "__main__":
    input_file = "car.data.txt"
    X = []
    count = 0

    with open(input_file, 'r') as f:
        for line in f.readlines():
            data = line[:-1].split(",")
            X.append(data)
    
    X = np.array(X)
    label_encoder = []
    X_encoded = np.empty(X.shape)
    for i, item in enumerate(X[0]):
        label_encoder.append(preprocessing.LabelEncoder())
        X_encoded[:, i] = label_encoder[-1].fit_transform(X[:, i])

    X = X_encoded[:, :-1].astype(int)
    y = X_encoded[:, -1].astype(int)

    params = {"n_estimators": 200, "max_depth": 8, "random_state": 7}
    clf = RandomForestClassifier(**params)
    clf.fit(X, y)
    
    from sklearn.model_selection import cross_val_score
    accuracy = cross_val_score(clf, X, y,
                        scoring='accuracy', cv= 3)
    print("Accuracy of the classfier: " + str(round(100*accuracy.mean(), 2)) + "%")
 
    input_data = ['vhigh', 'vhigh', '2', '2', 'small', 'low']
    input_data_encoded = [-1] * len(input_data)
    for i, item in enumerate(input_data):
        input_data_encoded[i] = int(label_encoder[i].transform(input_data[i]))

    input_data_encoded = np.array(input_data_encoded)

    output_class = clf.predict(input_data_encoded)
    print("Output class:", label_encoder[-1].inverse_transform(output_class)[0])