import streamlit as st
from app_eda import run_data

from app_main import run_home
from app_ml import run_ml


def main():
    st.title('닭의 조건에 따라 확인하는 앱입니다.')


    menu = ['MAIN','EDA','ML']


    choice = st.sidebar.selectbox('메뉴 선택', menu)

    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_data()
    elif choice == menu[2]:
        run_ml()



if __name__ == '__main__':
    main()

