import streamlit as st
import joblib
import numpy as np
import sklearn



def run_ml() :
    st.subheader('닭 조건에 따른 알의 무게')


    regressor = joblib.load('data/regressor1.pkl')
    scaler_X = joblib.load('data/scaler_X1.pkl')
    scaler_y =joblib.load('data/scaler_y1.pkl')

    variety = st.radio('품종을 선택하세요.',['Marans','Ameraucana'])
    if variety == 'Marans' :
        variety = 0
    else :
        variety = 1

    age = st.number_input('닭 나이',0,5000)
    weigth = st.number_input('닭 무게',0,10000)
    Feed   = st.number_input('사료 양',0,1000)

    PerDay = st.radio('하루에 알을 낳는가?.',['Yes','No'])
    if PerDay == 'Marans' :
        PerDay = 0
    else :
        PerDay = 1

    SunLight = st.number_input('햇빛 노출 시간',0,24)

    if st.button('달걀 무게 예측'):

        new_data = np.array([variety,age,weigth,Feed,PerDay,SunLight])

        new_data = new_data.reshape(1, 6)
        new_data = scaler_X.transform(new_data)

        y_pred = regressor.predict(new_data)
        y_pred = scaler_y.inverse_transform(y_pred)

        st.write('이 달걀 무게는'  + str(y_pred) + 'gram 입니다.')
