# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 19:41:59 2023

@author: ayesh
"""

import os
import pandas as pd
import numpy as np
os.chdir("C:/Users/ayesh/Documents/siva pythone 5 sem")
mydata=pd.read_csv("Computer_Data.csv")
mydata.head
mydata.tail
x = mydata.price
y=mydata.speed
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y, random_state = 50, test_size =0.25)
from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier()
import numpy as np
x_train = x_train.values.reshape(-1, 1)
clf.fit(x_train, y_train)
import pandas as pd
x_test = pd.DataFrame(x_test)
x_test = x_test.values.reshape(-1, 1)
y_pred = clf.predict(x_test)
from sklearn.metrics import accuracy_score
print("Train data accuracy:", accuracy_score(y_true=y_train, y_pred=clf.predict(x_train)))
from sklearn.metrics import classification_report
classification_report(y_test,y_pred)

