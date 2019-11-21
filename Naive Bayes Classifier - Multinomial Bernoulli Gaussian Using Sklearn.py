import numpy as np
import  pandas as pd
import urllib
from urllib.request import urlopen as uReq
import  sklearn
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
import  glob
from sklearn import metrics

from sklearn.metrics import accuracy_score
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data"
#url=r"C:\Users\muham\Downloads\spambase.data"
#rawdata= urllib.urlopen(url)
rawdata= uReq(url)
#dataset = np.loadtxt(rawdata, delimiter=',')
#path =r'C:\Users\muham\PycharmProjects\stopwords\P-Acta Informatica.csv'
#rawdata = glob.glob(path)
print(rawdata)
dataset = np.loadtxt(rawdata, delimiter=',')
print(dataset[0])
"""
x = dataset[:,0:48]
y = dataset[:,-1]
X_train  = x
X_test= y

Y_train =  .33
Y_test =  17

MultiNB = MultinomialNB.fit(X_train,.33)

print(MultiNB)
y_pred = MultiNB.predict(X_test)
print (accuracy_score(Y_test, y_pred))
"""