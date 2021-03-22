from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from pandas_profiling import ProfileReport


def result(request):
    df=pd.read_csv(r'C:\Users\hp\Downloads\diabetes.csv')
    profile = ProfileReport(df)
    profile.to_file(output_file='report.html')

    X=df.drop('Outcome',axis=1)
    Y=df['Outcome']

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train,Y_train)
    
    val1=float(request.GET['n1'])
    val2=float(request.GET['n2'])
    val3=float(request.GET['n3'])
    val4=float(request.GET['n4'])
    val5=float(request.GET['n5'])
    val6=float(request.GET['n6'])
    val7=float(request.GET['n7'])
    val8=float(request.GET['n8'])

    pred=model.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])
    result1=''

    if pred==[1]:
        result1='Positive'
    else:
        result1='Negative'

    return render(request,'predict.html', {'result2':result1})



def predict(request):
    return render(request,'predict.html')


def about(request):
    
    

    return render(request,'test.html', context={'job':5})

    