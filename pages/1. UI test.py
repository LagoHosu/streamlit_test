import streamlit as st
from PIL import Image

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
# from sklearn import load_iris



st.set_page_config(page_title="UI setting", page_icon="📈")

st.markdown("# UI setting")
st.sidebar.header("UI setting")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)


# select_species 변수에 사용자가 선택한 값이 지정됩니다
# single select
# select_species = st.sidebar.selectbox(
#     '확인하고 싶은 종을 선택하세요',
#     ['setosa','versicolor','virginica']
# )

# if not tmp_df.empty:
#   st.sidebar.success("Filter Applied!")
# else:
#   st.sidebar.error("Filter Failed")

st.sidebar.title('this is sidebar title')
st.sidebar.checkbox('Text here')
st.sidebar.write("- bullet here \n- another line")

# st.title('Hello Streamlit')
st.header('this is header')
# st.subheader('this is subheader')
st.write('Hello!')


col1,col2 = st.columns([2,3])

# col1.color = red
with col1 :
  # column 1 에 담을 내용
  st.subheader('here is column1')

with col2 :
  # column 2 에 담을 내용
  st.subheader('here is column2')
  st.checkbox('this is checkbox1 in col2 ')









##사이드바로 페이지 선택하고 싶으면,,,
# #사이드바 탭(페이지) 추가
# page_names_to_funcs = {
#     "-": intro,
#     "testing tap": testing_taps,
# }

# demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
# page_names_to_funcs[demo_name]()
