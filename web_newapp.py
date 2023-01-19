import time
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import plotly.express as px
import plotly
from statsmodels.tsa.api import Holt


#タイトル
st.title("機械学習アプリ")
st.write("streamlitで実装")

# 以下をサイドバーに表示
st.sidebar.markdown("### 機械学習に用いるcsvファイルを入力してください")

#ファイルアップロード
uploaded_files = st.sidebar.file_uploader("Choose a CSV file", accept_multiple_files= False)

#ファイルがアップロードされたら以下が実行される
if uploaded_files:
    df = pd.read_csv(uploaded_files)
    df_columns = df.columns

    #データフレームを表示
    st.markdown("### 入力データ")
    st.dataframe(df.style.highlight_max(axis=0))

    #matplotlibで可視化。X軸,Y軸を選択できる
    st.markdown("### 可視化 単変量")

    #データフレームのカラムを選択オプションに設定する
    x = st.selectbox("X軸", df_columns)
    y = st.selectbox("Y軸", df_columns)

    #選択した変数を用いてmtplotlibで可視化
    fig = plt.figure(figsize= (12,8))
    plt.scatter(df[x],df[y])
    plt.xlabel(x,fontsize=18)
    plt.ylabel(y,fontsize=18)
    st.pyplot(fig)

    st.markdown("### モデリング")
    #説明変数は複数選択式
    ex = st.multiselect("日付の列を選択してください", df_columns)

    #目的変数は一つ
    ob = st.selectbox("目的変数を選択してください", df_columns)

    st.markdown("#### 機械学習を実行します")
    execute = st.button("実行")

    df["ex"]=pd.to_datetime(df.Date)
    df.set_index("Date",inplace=True)
    df.index.frep="MS"

    fit=Holt(df[:]).fit(smoothing_level=0.8,smoothing_slope=0.2,optimized=False)
    start, end =len(df)-24,len(df)
    predict2=fit.predict(start, end)

    predict2.plot()







