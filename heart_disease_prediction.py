# -*- coding: utf-8 -*-
"""Heart Disease Prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PYLv9DbcnbIvgGLHLyH5IKGxl1XEb3pd

Importing dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import  accuracy_score

"""Data collection and presprocessing

"""

# loading the csv data to a pandas dataframe
heart_data = pd.read_csv('/content/heart.csv')

#print first 5 rows of the dataset
heart_data.head()

# print last 5 rows of the dataset
heart_data.tail()

# numbers of rows and columns in the dataset
heart_data.shape

# getting some info about the data
heart_data.info()

# checking for missing values
heart_data.isnull().sum()

# stastical measures about the data
heart_data.describe()

# checking the distribution of target variable
heart_data['target'].value_counts()

"""1 --> Defective heart
2 --> Healthy heart
"""

x = heart_data.drop(columns='target', axis = 1)
y = heart_data['target']

print(x)

print(y)

"""Splitting the Data into Training data & Test Data"""

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,stratify=y, random_state=2)

print(x.shape, x_train.shape, x_test.shape)

"""Model Training

Logistic Regression
"""

model = LogisticRegression()

# training the Logistic Regression model with Training data
model.fit(x_train, y_train)

"""Model Evaluation

Accuracy **Score**
"""

# accuracy on training data
x_train_prediction = model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)

print('Accuracy on Training data : ', training_data_accuracy)

# accuracy on test data
x_test_prediction = model.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction, y_test)

print('Accuracy on Test data : ', test_data_accuracy)

"""**Building the predictive system**"""

input_data = (51,1,0,140,298,0,1,122,1,4.2,1,3,3)

# change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]==0):
  print('the person does not have a heart disease')
else:
  print('the person has heart disease')

