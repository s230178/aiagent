# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('')

# 2. 모델 설명
st.title('친구야 잠은 자고 다니니?')
st.subheader('카페인 섭취와 공부 시간으로 수면시간 예측하기')
st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
st.write(' - 훈련    데이터 : 350')
st.write(' - 테스트 데이터 : 150')
st.write(' - 인공지능 모델 정확도 : -0.01')
 

# 3. 데이터시각화
col1, col2 = st.columns(2)  
with col1:
      st.subheader('데이터시각화1')
      st.image('시각화1.png' )   # 이미지 불러오기
with col2:
      st.subheader('데이터시각화2')
      st.image('시각화2.png' )   # 이미지 불러오기

# 4. 모델 활용
st.subheader('모델 활용')
st.write('**** 다음을 입력하세요.. 인공지능이 당신의 수면 가능 시간을 알려드립니다! ')

a = st.number_input(' 몇시간 공부하니? ', value=0)     
b = st.number_input('  카페인 몇잔 마시니? ', value=0.0 )     

                                                           

if st.button('너 얼마나 자니?'):            
        input_data = [[a,b,]]   
        p = model.predict(input_data)         # model이 예측한 값을 p에 저장한다
        st.write('너의 코코넨네 시간', p)
