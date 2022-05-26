import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def run_data():
    df = pd.read_csv('data/egg.csv', index_col= 0)
    

    if st.checkbox('전체데이터'):
        st.dataframe(df)
    else :
        st.text('상위 5개')
        st.dataframe(df.head())

    
    column_list = df.columns
    
    choice_list = st.multiselect('보고싶은 데이터 선택', column_list)

    st.dataframe(df[choice_list])


    col_list = df.columns[[2,3,4,6,7,8,9] ]

    selected_list = st.multiselect('데이터별 상관계수',col_list)
    

    if len(selected_list) > 1 :
        

        st.text('선택하신 컬럼끼리의 상관계수 입니다.')
        st.dataframe(df[selected_list].corr())


        fig2 = plt.figure()
        sb.heatmap(data = df[selected_list].corr(), annot=True, fmt='.2f',
                vmin = -1, vmax = 1, cmap = 'coolwarm', linewidths=0.5)
        st.pyplot(fig2)

