import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("散布図化アプリ")

st.sidebar.markdown("### csvファイルを入力してください")
#ファイルアップロード
uploaded_files = st.sidebar.file_uploader("Choose a CSV file", accept_multiple_files= False)

if uploaded_files:
    df = pd.read_csv(uploaded_files)
    df_columns = df.columns

    #データフレームを表示
    st.markdown("### 入力データ")
    st.dataframe(df.style.highlight_max(axis=0))
    #matplotlibで可視化。X軸,Y軸を選択できる
    st.markdown("### グラフ")
    #データフレームのカラムを選択オプションに設定する
    x = st.selectbox("X軸", df_columns)
    y = st.selectbox("Y軸", df_columns)
    #選択した変数を用いてmtplotlibで可視化
    fig = plt.figure(figsize= (12,8))
    plt.scatter(df[x],df[y])
    plt.xlabel(x,fontsize=18)
    plt.ylabel(y,fontsize=18)
    st.pyplot(fig)
