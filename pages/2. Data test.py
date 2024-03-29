import streamlit as st
from PIL import Image

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris


st.set_page_config(page_title="Data table", page_icon="🌍")

st.markdown("# Data table")
st.sidebar.header("Data table")
st.write(
    """This demo shows how to use
[`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
to display geospatial data."""
)


#웹사용자 input 받기
iris_dataset = load_iris()

df= pd.DataFrame(data=iris_dataset.data,columns= iris_dataset.feature_names)
df.columns= [ col_name.split(' (cm)')[0] for col_name in df.columns] # 컬럼명을 뒤에 cm 제거하였습니다
df['species']= iris_dataset.target 

species_dict = {0 :'setosa', 1 :'versicolor', 2 :'virginica'} 
def mapp_species(x):
    return species_dict[x]

df['species'] = df['species'].apply(mapp_species)

# st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')

#multi select
select_multi_species = st.sidebar.multiselect(
    "확인하고자 하는 종을 선택해 주세요.\n\n(복수선택가능)",
    ['-','setosa','versicolor','virginica']
)

#select with condition
# 라디오에 선택한 내용을 radio select변수에 담습니다
radio_select =st.sidebar.radio(
    "what is key column?",
    ['sepal length', 'sepal width', 'petal length','petal width'],
    horizontal=True
    )
# 선택한 컬럼의 값의 범위를 지정할 수 있는 slider를 만듭니다. 
slider_range = st.sidebar.slider(
    "choose range of key column",
    0.0, #시작 값 
    10.0, #끝 값  
    (2.5, 7.5) # 기본값, 앞 뒤로 2개 설정 /  하나만 하는 경우 value=2.5 이런 식으로 설정가능
)

# 필터 적용버튼 생성 
start_button = st.sidebar.button(
    "filter apply 📊 "#"버튼에 표시될 내용"
)

tab1, tab2= st.tabs(['Apple' , 'Banana'])
tab1.subheader('[Selected data table]')
# tab1.table(df.head())

tab2.subheader('[Raw data table]')
tab2.dataframe(df)

test_img = Image.open('C:/Users/hsshi/Downloads/fluffy.jpg')
tab2.image(test_img)


if start_button:
    tmp_df = df[df['species'].isin(select_multi_species)]
    #slider input으로 받은 값에 해당하는 값을 기준으로 데이터를 필터링합니다.
    tmp_df= tmp_df[ (tmp_df[radio_select] >= slider_range[0]) & (tmp_df[radio_select] <= slider_range[1])]
    tab1.dataframe(tmp_df)
    # 성공문구
    if not tmp_df.empty:
        st.sidebar.success("Filter Applied!")
    else:
        st.sidebar.error("Filter Failed")


