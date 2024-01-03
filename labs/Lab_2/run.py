import numpy as np
import scipy.io

from sklearn import svm
from collections import OrderedDict

from process_email import process_email
from process_email import email_features
from process_email import get_dictionary

# Задание 1
with open ('email.txt', 'r') as file:
    email = file.read().replace('\n', '')
print(email)

# Задание 2
p_e_list = process_email(email)
num = [num for tuple in p_e_list for array in tuple for num in array]
print(num)

# Задание 3
features = email_features(num)
print(features)
print('Dlina vektora priznakov: ', len(features))
print('Kolichestvo nenulevix elemntov: \n', sum(features))

# Задание 4
data = scipy.io.loadmat('train.mat')
X = data['X']
y = data['y'].flatten()

print('Trenirovka SVM-klassifikatora, s lineynim yadrom...')
clf = svm.SVC(C = 0.1, kernel = 'linear', tol = 1e-3)
model = clf.fit(X,y)
p = model.predict(X)

print('Tochnost na obuchaushey viborke: \n', np.mean(p == y)*100)
# print(len(y))
# print((sum(p == y)/len(y))*100)

# Задание 5
data = scipy.io.loadmat('test.mat')
Xtest = data['Xtest']
ytest = data['ytest'].flatten()

print('Trenirovka SVM-klassifikatora, s lineynim yadrom...')
clf = svm.SVC(C = 0.1, kernel = 'linear', tol = 1e-3)
model = clf.fit(Xtest,ytest)
p = model.predict(Xtest)

print('Tochnost na testovoi viborke: \n', np.mean(p == ytest)*100)

# Задание 6 
t = sorted(list(enumerate(model.coef_[0])), key = lambda e: e[1], reverse = True)
d = OrderedDict(t)
idx = list(d.keys())
weight = list(d.values())
dictionary = get_dictionary()

print('Top 15 slov v pismah so spamom: ')
for i in range(15):
    print('%-15s (%f)' %(dictionary[idx[i]], weight[i]))