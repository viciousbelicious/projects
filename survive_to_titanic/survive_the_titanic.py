# -*- coding: utf-8 -*-
"""survive the titanic

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_ueuIShkztI0Yo3wYI34kMNUe-OGQFmo
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import openpyxl

"""## Data Exploration

num data - charts and pivots to look for any survival %

categorical data - exploration

+

correlation 

"""

# fase di import datasets // per stampare print(' ') oppure ' '

training = pd.read_csv('/content/drive/MyDrive/py/titanic_comp/train.csv')
test = pd.read_csv('/content/drive/MyDrive/py/titanic_comp/test.csv')

training['train_test'] = 1 # aggiungo colonna 'train_test' valorizzate 1
test['train_test'] = 0 # aggiungo colonna 'train_test' valorizzate 0
test['Survived'] = np.NaN # aggiungo colonna 'Survived' valorizzate NaN
all_data = pd.concat([training, test]) # unione dei db

training.to_excel('/content/drive/MyDrive/py/carlo_vanzina.xlsx',index = False) 
# export dei dati in un file xlsx

training

test

training[training['Name'] == 'Leonardo, Di Caprio'] # cerco se Leonardo, Di Caprio è un passeggero

training[training['Name'] == 'Dooley, Mr. Patrick'] # ctrl + alt + freccia == selezione multiriga
training[training['Name'] == 'Dooley, Mr. Patrick'] # ctrl + d == selezione di tutte le parole uguali
training[training['Name'] == 'Dooley, Mr. Patrick']
training[training['Name'] == 'Dooley, Mr. Patrick']

# data exploration @.@ @.@ per carpire la qualità del db
training.info()

training.describe() # ripassa il quartile

training[training['Survived'] == 1] # cerco chi è sopravvissuto (38% dei passeggeri)

training['Survived'].value_counts() # conto quanti 1 e quanti 0

x = (342/891)*100
x = int(x)
print('la percentuale dei sopravvissuti è del', x, '%')

training['Pclass'].unique()

training['SibSp'].value_counts() # ripasso come ordinare le classi dei dati

training[training['SibSp'] == 5]

training['Parch'].value_counts()

training[(training['Ticket'] == 'CA 2144')]

training['Fare'].value_counts()

df_num = training[['Survived', 'Age', 'SibSp', 'Parch', 'Fare']]

df_cat = training[['Survived', 'Pclass', 'Sex', 'Ticket', 'Cabin', 'Embarked']]

# . :
for column in df_num.columns:
  plt.hist(df_num[column])
  plt.title(column)
  plt.show()

plt.hist(df_num['Fare'], range= (1, 100), bins=50) # incrementare il range dell'asse x
plt.title('Fare')
plt.xlim(0,50) # limito il range di x
plt.show()

print(training.iloc[0]) # printo la prima # riga
training.columns # printo l'intestazione delle colonne

print(df_num.corr())
sns.heatmap(df_num.corr()) # correlazione tra le variabili

pd.pivot_table(training, index='Survived', values=['Age', 'SibSp', 'Parch', 'Fare'])

survived_pclass_ticket = pd.pivot_table(training, index="Survived", columns="Pclass", values="Ticket", aggfunc="count") 
survived_sex_ticket = pd.pivot_table(training, index="Survived", columns="Sex", values="Ticket", aggfunc="count") 
survived_embarked_ticket = pd.pivot_table(training, index="Survived", columns="Embarked", values="Ticket", aggfunc="count") 
pclass_embarked_ticket = pd.pivot_table(training, index="Pclass", columns="Embarked", values="Ticket", aggfunc="count")
print("survived_pclass_ticket") 
print(survived_pclass_ticket) 
print("**") 
print("survived_sex_ticket") 
print(survived_sex_ticket) 
print("**") 
print("survived_embarked_ticket") 
print(survived_embarked_ticket)
print("**") 
print("pclass_embarked_ticket")
print(pclass_embarked_ticket)

training['Embarked'].value_counts()

training['Pclass'].value_counts()

x = (217/644)*100
x = int(x)
y = (30/77)*100
y = int(y)
z = (93/168)*100
z = int(z)

print('S - il', x, '% dei passeggeri imbarcati sono sopravvissuti')
print('Q - il', y, '% dei passeggeri imbarcati sono sopravvissuti')
print('C - il', z, '% dei passeggeri imbarcati sono sopravvissuti')

"""## Feature Engineering
Cabin - split the cabin column into cabin letter and cabin_multiple + pivot to evaluate the impact on the survival %

Tickets - same

Name - split the title of people and evaluate the degree of survival
"""

pd.set_option("display.max_rows", None) # come printo la colonna a sinitra in ordine alfabetico ?! così
df_cat.Cabin.value_counts()

len(df_cat.Cabin.unique())

training

891-147

es = ["parola magica"] # come splittare il contenuto objects
for letter in es:
  letter = letter.split(" ")
  print(letter)

training[training["Cabin"] == "B96 B98"] # i gruppi delle cabine potrebbero darci un'informazione più adeguata rispetto a quello dei parenti/figli

training['cabin_multiple'] = training.Cabin.apply(lambda x: 0 if pd.isna(x) else len(x.split(' '))) # splitto lettere e valori multipli dove trovo spazi nella colonna
training['cabin_multiple'].value_counts()

pd.pivot_table(training, index = 'Survived', columns = 'cabin_multiple', values = 'Ticket' ,aggfunc ='count')

training['cabin_adv'] = training.Cabin.apply(lambda x: str(x)[0]) # rendo le lettere delle cabine categorie n=NaN

print(training.cabin_adv.value_counts())
pd.pivot_table(training,index='Survived',columns='cabin_adv', values = 'Name', aggfunc='count')

# tickets
training['numeric_ticket'] = training.Ticket.apply(lambda x: 1 if x.isnumeric() else 0)
training['ticket_letters'] = training.Ticket.apply(lambda x: ''.join(x.split(' ')[:-1]).replace('.','').replace('/','').lower() if len(x.split(' ')[:-1]) >0 else 0)

training['numeric_ticket'].value_counts()

training['ticket_letters'].value_counts()

pd.pivot_table(training,index='Survived',columns='numeric_ticket', values = 'Ticket', aggfunc='count')

pd.pivot_table(training,index='Survived',columns='ticket_letters', values = 'Ticket', aggfunc='count')

# divido il titolo dal nome
training['name_title'] = training.Name.apply(lambda x: x.split(',')[1].split('.')[0].strip())

training['name_title'].value_counts()

pd.pivot_table(training,index='Survived',columns='name_title', values = 'Ticket', aggfunc='count')

"""## Data Preprocessing for Model

Embarked - drop

union of df in all_data

category change of numerical data int e float in df_all_data

Fare - fill empty row with approx (median)
Age -  fill empty row with approx (median)

Observation of logarithmic curves, in order to reduce the range of the datas
+
Data scaling

"""

all_data['cabin_multiple'] = all_data.Cabin.apply(lambda x: 0 if pd.isna(x) else len(x.split(' ')))
all_data['cabin_adv'] = all_data.Cabin.apply(lambda x: str(x)[0])
all_data['numeric_ticket'] = all_data.Ticket.apply(lambda x: 1 if x.isnumeric() else 0)
all_data['ticket_letters'] = all_data.Ticket.apply(lambda x: ''.join(x.split(' ')[:-1]).replace('.','').replace('/','').lower() if len(x.split(' ')[:-1]) >0 else 0)
all_data['name_title'] = all_data.Name.apply(lambda x: x.split(',')[1].split('.')[0].strip())
# applico tutta la feature engineering al dataframe train+test

all_data.Age = all_data.Age.fillna(training.Age.median()) # fillo le righe NaN con il valore mediano della colonna
all_data.Fare = all_data.Fare.fillna(training.Fare.median()) # fillo le righe NaN con il valore mediano della colonna

all_data.dropna(subset=['Embarked'],inplace = True) # drop della colonna di embarked

all_data['norm_sibsp'] = np.log(all_data.SibSp+1) # facciamo il logaritmo per ridurre la varianza e rendere i dati più comprensibili. 
all_data['norm_sibsp'].hist()

all_data['norm_fare'] = np.log(all_data.Fare + 1)
all_data['norm_fare'].hist()

all_data["Fare"].hist()

all_data.Pclass = all_data.Pclass.astype(str) # conversione dati della colonna Fare in categorici

# creazione di una variabile dummy contente tutte le categoriche
all_dummies = pd.get_dummies(all_data[['Pclass','Sex','Age','SibSp','Parch','norm_fare','Embarked','cabin_adv','cabin_multiple','numeric_ticket','name_title','train_test']])

X_train = all_dummies[all_dummies.train_test == 1].drop(['train_test'], axis =1) # slit dei df
X_test = all_dummies[all_dummies.train_test == 0].drop(['train_test'], axis =1)

y_train = all_data[all_data.train_test==1].Survived
y_train.shape

# Scale data IMPORT DELLA FUNZIONE
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()
all_dummies_scaled = all_dummies.copy()
all_dummies_scaled[['Age','SibSp','Parch','norm_fare']]= scale.fit_transform(all_dummies_scaled[['Age','SibSp','Parch','norm_fare']])

all_dummies_scaled.head()

all_dummies.Age.hist()

all_dummies_scaled.Age.hist()

X_train_scaled = all_dummies_scaled[all_dummies_scaled.train_test == 1].drop(['train_test'], axis =1)
X_test_scaled = all_dummies_scaled[all_dummies_scaled.train_test == 0].drop(['train_test'], axis =1)

y_train = all_data[all_data.train_test==1].Survived

"""## Model Building 

import of stats models

applys and values analisys

Naive Bayes (72.6%) Logistic Regression (82.1%) Decision Tree (77.6%) K Nearest Neighbor (80.5%) Random Forest (80.6%) Support Vector Classifier (83.2%) Xtreme Gradient Boosting (81.8%) Soft Voting Classifier - All Models (82.8%)
"""

# import dei modelli statistici

from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier

"""### GaussianNB"""

gnb = GaussianNB()
cv = cross_val_score(gnb,X_train_scaled,y_train,cv=5) # cross validation, addestra il modello in un modo particolare in questo caso per 5 volte
print(cv)
print(cv.mean())

"""### LogisticRegression"""

lr = LogisticRegression(max_iter = 2000)
cv = cross_val_score(lr,X_train,y_train,cv=5)
print(cv)
print(cv.mean())

lr = LogisticRegression(max_iter = 2000)
cv = cross_val_score(lr,X_train_scaled,y_train,cv=5)
print(cv)
print(cv.mean())

"""### DecisionTreeClassifier"""

dt = tree.DecisionTreeClassifier(random_state = 1)
cv = cross_val_score(dt,X_train,y_train,cv=5)
print(cv)
print(cv.mean())

dt = tree.DecisionTreeClassifier(random_state = 1)
cv = cross_val_score(dt,X_train_scaled,y_train,cv=5)
print(cv)
print(cv.mean())

"""### KNeighborsClassifier"""

knn = KNeighborsClassifier()
cv = cross_val_score(knn,X_train,y_train,cv=5)
print(cv)
print(cv.mean())

knn = KNeighborsClassifier()
cv = cross_val_score(knn,X_train_scaled,y_train,cv=5)
print(cv)
print(cv.mean())

"""### RandomForestClassifier"""

rf = RandomForestClassifier(random_state = 1)
cv = cross_val_score(rf,X_train,y_train,cv=5)
print(cv)
print(cv.mean())

rf = RandomForestClassifier(random_state = 1)
cv = cross_val_score(rf,X_train_scaled,y_train,cv=5)
print(cv)
print(cv.mean())

"""### SVC"""

svc = SVC(probability = True)
cv = cross_val_score(svc,X_train_scaled,y_train,cv=5)
print(cv)
print(cv.mean())

"""### XGBClassifier"""

xgb = XGBClassifier(random_state =1)
cv = cross_val_score(xgb,X_train_scaled,y_train,cv=5)
print(cv)
print(cv.mean())

"""###VotingClassifier"""

from sklearn.ensemble import VotingClassifier
voting_clf = VotingClassifier(estimators = [('lr',lr),('knn',knn),('rf',rf),('gnb',gnb),('svc',svc),('xgb',xgb)], voting = 'soft')

cv = cross_val_score(voting_clf,X_train_scaled,y_train,cv=5)
print(cv)
print(cv.mean())

voting_clf.fit(X_train_scaled,y_train)
y_hat_base_vc = voting_clf.predict(X_test_scaled).astype(int)
basic_submission = {'PassengerId': test.PassengerId, 'Survived': y_hat_base_vc}
base_submission = pd.DataFrame(data=basic_submission)
base_submission.to_csv('base_submission.csv', index=False)

"""##Model Tuned Performance
SVC selected

performance boosting of the selectced model
"""

from sklearn.model_selection import GridSearchCV 
from sklearn.model_selection import RandomizedSearchCV

def clf_performance(classifier, model_name):     
  print(model_name)
  print('Best Score: ' + str(classifier.best_score_))     
  print('Best Parameters: ' + str(classifier.best_params_))

svc = SVC(probability = True)
cv = cross_val_score(svc,X_train_scaled,y_train,cv=5)
print(cv)
print(cv.mean())

svc = SVC(probability = True)
param_grid = tuned_parameters = [{'kernel': ['rbf'], 'gamma': [.1,.5,1,2,5,10],
                                  'C': [.1, 1, 10, 100, 1000]},
                                 {'kernel': ['linear'], 'C': [.1, 1, 10, 100, 1000]},
                                 {'kernel': ['poly'], 'degree' : [2,3,4,5], 'C': [.1, 1, 10, 100, 1000]}]
clf_svc = GridSearchCV(svc, param_grid = param_grid, cv = 5, verbose = True, n_jobs = -1)
best_clf_svc = clf_svc.fit(X_train_scaled,y_train)
clf_performance(best_clf_svc,'SVC')

y_hat_base_vc = best_clf_svc.predict(X_test_scaled).astype(int)
basic_submission = {'PassengerId': test.PassengerId, 'Survived': y_hat_base_vc}
base_submission = pd.DataFrame(data=basic_submission)
base_submission.to_csv('svc_classifier.csv', index=False)

"""##Submission"""

base_submission.head()