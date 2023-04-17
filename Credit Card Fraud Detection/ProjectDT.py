import pandas as pd
import numpy as np
import keras

np.random.seed(2)

data = pd.read_csv('creditcard.csv')

#Data Exploration
data.head()
data.tail()
data.describe()

#Data Pre-processing 
from sklearn.preprocessing import StandardScaler
data['normalizedAmount'] = StandardScaler().fit_transform(data['Amount'].values.reshape(-1,1))
data = data.drop(['Amount'],axis=1)

data.head()
data = data.drop(['Time'],axis=1)
data.head()

X = data.iloc[:, data.columns != 'Class']
y = data.iloc[:, data.columns == 'Class']

y.head()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state=0)

X_train.shape
X_test.shape

#Model Traning
from sklearn.tree import DecisionTreeClassifier
decision_tree = DecisionTreeClassifier()

decision_tree.fit(X_train,y_train.values.ravel())

y_pred = decision_tree.predict(X_test)

decision_tree.score(X_test,y_test)

y_pred = decision_tree.predict(X)

y_expected = pd.DataFrame(y)

cnf_matrix = confusion_matrix(y_expected,y_pred.round())
plot_confusion_matrix(cnf_matrix,classes=[0,1])
plt.show()

