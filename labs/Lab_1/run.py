import scipy.io as sio
import numpy as np
import svm

mat1 = sio.loadmat('dataset1.mat')
y = mat1['y'].astype(np.float64)
X = mat1['X']

#Задание 1
svm.visualize_boundary_linear(X,y,None, "Исходные данные dataset1.mat")

#Задание 2
C1 = 1
model = svm.svm_train(X,y,C1,svm.linear_kernel, 0.001,20)
svm.visualize_boundary_linear(X,y,model,"Разделяющая граница при C = 1")

#Задание 3
C2 = 100
model = svm.svm_train(X,y,C2,svm.linear_kernel, 0.001,20)
svm.visualize_boundary_linear(X,y,model,"Разделяющая граница при C = 100")

#Задание 4
svm.contour(1)
svm.contour(3)

#Задание 5
mat2 = sio.loadmat('dataset2.mat')
y1 = mat2['y'].astype(np.float64)
X1 = mat2['X']
svm.visualize_boundary_linear(X1,y1,None, "Исходные данные dataset2.mat")

#Задание 6
sigma = 0.1
gaussian = svm.partial(svm.gaussian_kernel, sigma=sigma)
gaussian.__name__ = svm.gaussian_kernel.__name__
model = svm.svm_train(X1,y1,C1,gaussian)
svm.visualize_boundary(X1,y1,model, "Получившиеся границы")

#Задание 7
mat3 = sio.loadmat('dataset3.mat')
y3 = mat3['y'].astype(np.float64)
X3 = mat3['X']
yval = mat3['yval'].astype(np.float64)
Xval = mat3['Xval']
svm.visualize_boundary_linear(X3,y3,None, "Исходные данные dataset3.mat")
svm.visualize_boundary_linear(Xval,yval,None, "Исходные данные тестовой выборки")

#Задание 8
sigma = 0.5
gaussian = svm.partial(svm.gaussian_kernel, sigma=sigma)
gaussian.__name__ = svm.gaussian_kernel.__name__
model = svm.svm_train(X3,y3,C1,gaussian)
svm.visualize_boundary(X3,y3,model, "Модель при неоптимиальных параметрах")

#Задание 9
new_C = 0
new_sigma = 0
new_error = len(yval)
new_model = None

for C in [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]:
    for sigma in [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]:
        gaussian = svm.partial(svm.gaussian_kernel, sigma=sigma)
        gaussian.__name__ = svm.gaussian_kernel.__name__
        model = svm.svm_train(X3, y3, C, gaussian)
        #svm.visualize_boundary(X3, y3, model, "Модель с параметрами C и sigma")
        ypred = svm.svm_predict(model, Xval)
        error = np.mean(ypred != yval.ravel())
        if error < new_error:
            new_C = C
            new_error = error
            new_sigma = sigma
            new_model = model
            
svm.visualize_boundary(X3, y3, new_model, "Новая модель с параметрами C и sigma")
print("Лучшая C: ", new_C)
print("Лучшая Sigma: ", new_sigma)

new_C = 0
new_sigma = 0
new_error = len(yval)
new_model = None

for C in [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]:
    for sigma in [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]:
        gaussian = svm.partial(svm.gaussian_kernel, sigma=sigma)
        gaussian.__name__ = svm.gaussian_kernel.__name__
        model = svm.svm_train(Xval, yval, C, gaussian)
        # svm.visualize_boundary(X3, y3, model, "Модель с параметрами C и sigma")
        ypred = svm.svm_predict(model, X3)
        error = np.mean(ypred != y3.ravel())
        if error < new_error:
            new_C = C
            new_error = error
            new_sigma = sigma
            new_model = model

svm.visualize_boundary(Xval, yval, new_model, "Новая модель с параметрами C и sigma(тест)")

print("Лучшая C(тест): ", new_C)
print("Лучшая Sigma(тест): ", new_sigma)