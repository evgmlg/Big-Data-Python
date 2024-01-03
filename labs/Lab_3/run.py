import pandas as pd
import re
import scipy

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import Ridge

#Задание 1: загрузика данных об описаниях вакансий и соответствующих годовых зарплатах из файла 
csv_data = pd.read_csv('salary-train.csv')

#Задание 2.1: приведение текста к нижнему регистру
csv_data['FullDescription'] = csv_data['FullDescription'].str.lower()

#Задание 2.2: замена всего, кроме букв и цифр, на пробелы
csv_data['FullDescription'] = csv_data['FullDescription'].apply(lambda x: re.sub('[^a-zA-Z0-9]', ' ', x))

#Задание 2.3: применение TfdifVectorizer для преобразования текстов в векторы признаков
tfidf_vect = TfidfVectorizer(min_df = 5)
text_vect = tfidf_vect.fit_transform(csv_data['FullDescription'])

#Задание 2.4: замена пропусков в столбцах LocationNormalized и ContractTime на специальную строку ‘nan’
csv_data['LocationNormalized'].fillna('nan', inplace = True)
csv_data['ContractTime'].fillna('nan', inplace = True)

#Задание 2.5: применение DictVectorizer для получения one-hot-кодирования признаков LocationNormalized и ContractTime.
enc = DictVectorizer()
X_train_categ = enc.fit_transform(csv_data[['LocationNormalized','ContractTime']].to_dict('records'))

#Задание 2.6: объединение всех полученных признаков в одну матрицу “объекты-признаки”
o_s = scipy.sparse.hstack([text_vect, X_train_categ])

#Задание 3: обучение гребневой регрессии с параметром alpha=1
s = csv_data['SalaryNormalized']
ridge_train = Ridge(alpha=1)
ridge_train.fit(o_s, s)

#Задание 4: построение прогнозов для двух примеров из файла salary-test-mini.csv

csv_data_test = pd.read_csv('salary-test-mini.csv')

csv_data_test['FullDescription'] = csv_data_test['FullDescription'].str.lower()

csv_data_test['FullDescription'] = csv_data_test['FullDescription'].apply(lambda x: re.sub('[^a-zA-Z0-9]', ' ', x))

text_vect_test = tfidf_vect.transform(csv_data_test['FullDescription'])

csv_data_test['LocationNormalized'].fillna('nan', inplace = True)
csv_data_test['ContractTime'].fillna('nan', inplace = True)


X_test_categ = enc.transform(csv_data_test[['LocationNormalized','ContractTime']].to_dict('records'))

o_s_test = scipy.sparse.hstack([text_vect_test, X_test_categ])

s_pred = ridge_train.predict(o_s_test)

print(s_pred)



