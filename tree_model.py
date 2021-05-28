import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import GridSearchCV

df = pd.read_csv("poschair.csv")
X = df.iloc[:,:-1]
y = df.iloc[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7)

dtc = DecisionTreeClassifier()
cv_scores = cross_val_score(dtc, X, y, cv=10)
sns.displot(cv_scores)
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
prob = dtc.predict_proba(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))

precision = precision_score(y_true=y_test,y_pred=predictions, average='micro')
print("Precision:", precision)

recall = recall_score(y_true=y_test,y_pred=predictions, average='micro')
print("Recall:", recall)
