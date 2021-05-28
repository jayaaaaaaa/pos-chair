import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import GridSearchCV
import main2
from time import sleep
# import pickle

df = pd.read_csv("/home/pi/Adafruit_Python_DHT/pos-chair/Final data.csv")
X = df.iloc[:,[3,6,9,12,15]]
# print(X.head())
y = df.iloc[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7)

dtc = DecisionTreeClassifier()
cv_scores = cross_val_score(dtc, X, y, cv=10)
#sns.displot(cv_scores)
plt.title('Average score: {}'.format(np.mean(cv_scores)))

dtc = DecisionTreeClassifier()

parameter_grid = {'criterion': ['gini', 'entropy'],
                  'splitter': ['best', 'random'],
                  'max_depth': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]}

skf = StratifiedKFold(n_splits=5)
cross_validation = skf.get_n_splits(X_train, y_train)

grid_search = GridSearchCV(dtc, param_grid=parameter_grid, cv=cross_validation)

grid_search.fit(X, y)
print('Best score: {}'.format(grid_search.best_score_))
print('Best parameters: {}'.format(grid_search.best_params_))

dtc = grid_search.best_estimator_

dtc.fit(X_train, y_train)
predictions = dtc.predict(X_test)
# joblib.dump(dtc, open('savedmodel.pickle'), 'wb')
# loaded_model = joblib.load(open('savedmodel.pickle', 'rb'))
# result = loaded.model.accuracy_score(y_test, predictions)
# print(result)

# predictions = dtc.predict(X_test)
# prob = dtc.predict_proba(X_test)
# print("Accuracy:", accuracy_score(y_test, predictions))
# 
# precision = precision_score(y_true=y_test,y_pred=predictions, average='micro')
# print("Precision:", precision)
# 
# recall = recall_score(y_true=y_test,y_pred=predictions, average='micro')
# print("Recall:", recall)

count = 1

while count:
    ch0_value = round(main2.poschair()[0],2)
    ch1_value = round(main2.poschair()[2],2)
    ch2_value = round(main2.poschair()[4],2)
    ch3_value = round(main2.poschair()[6],2)
    ch4_value = round(main2.poschair()[8],2)

    X_new = pd.DataFrame([[ch0_value, ch1_value, ch2_value, ch3_value, ch4_value]])
    # print(X_new)
    result = dtc.predict(X_new)
    sleep(5)
    print(result)
