import streamlit as st
from PIL import Image
import pandas as pd


def run_home():
    st.subheader('닭의 종류')

    ogol = Image.open('data/ogol.jpg')
    jong_mi = Image.open('data/jong_mi.jpg')
    tojong = Image.open('data/tojong.jpg')
    marans = Image.open('data/marans.jpg')
    chbo_jpg = Image.open('data/chbo.jpg')
    amerau = Image.open('data/ameraucana.jpg')

    menu = ['오골계','긴꼬리닭','토종닭','마란','차보','아메라우카나']
    my_choice = st.selectbox('정보를 보고싶은 닭을 선택', menu)


    if my_choice == menu[0]:
        st.image(ogol)
        st.write('오골계는 닭의 한 품종으로, 살·가죽·뼈가 모두 검은 것이 특징이다. 중국에서 기원된 코친의 체형을 가진 닭의 한 품종으로 영어권 국가에서는 털이 부드러워 흔히 실키라고 부른다. 현재 국내에서 사육되고 있는 오골계는 대부분 혼합종이다')
    elif my_choice == menu[1]:
        st.image(jong_mi)
        st.write('긴꼬리닭은 일본과 한국에서 기르는 애완용 닭 품종이다. 보통 장미계라고 하는데 꽁무니의 깃털이 사람의 키보다 길다.')
    elif my_choice == menu[2]:
        st.image(tojong)
        st.write('하나는 한우와 같이 예로부터 우리나라에서 사육되어 다른 품종과 섞이지 않고 순수 혈통을 유지한 재래종 토종닭입니다. 다른 하나는 외국에서 품종이 개발되었지만 국내에 순계가 도입되고 7세대 이상 사육되어 우리나라 기후와 풍토에 완전히 적응한 개량종을 토착종 토종닭이라 부릅니다.')
    elif my_choice == menu[3]:
        st.image(marans)
        st.write('프랑스 남서부의 누벨-아키텐 (Nuvelle-Aquitaine) 지역에있는 샤 랑트-마리 팀 (Charcharente-Maritime) 구역의 항구 도시 마란에서 생산 된 닭입니다')
    elif my_choice == menu[4]:
        st.image(chbo_jpg)
        st.write('원산지는 베트남이나 일본에서 개량되었다.깃털의 색깔과 체형에 따라 25종을 나뉘며 그 중 흰색차보,우즈라차보,가쓰라차보가 유명하다. 흰색차보는 온몸이 희고 꼬리가 곧게 서며 다섯 갈래로 갈라진 홑볏을 하고 있다. 가장 널리 사육되는 품종이며 성질이 온순해서 꿩이나 금계의 어미 노릇을 하기에 좋다. 우즈라차보는 돌연변이종으로서 꽁지깃과 꼬리뼈가 없는 것이 큰 특징이다. 가쓰라차보는 흰색차보와 비슷한데, 날개와 꽁지의 긴 깃털만이 검정색이고 그 밖의 깃털은 흰색이며 날개깃을 길어서 땅에 끌린다. 겉모습이 아름다워 흔히 애완용으로 기른다.')
    elif my_choice == menu[5]:
        st.image(amerau)
        st.write('Ameraucana는 미국산 닭고기입니다. 1970 년대 미국에서 개발되었으며 칠레에서 가져온 Araucana 닭에서 유래합니다. 청계 유전자를 유지하지만 모종의 치명적인 대립 유전자를 제거하기 위해 사육되었습니다')
    


    

   

