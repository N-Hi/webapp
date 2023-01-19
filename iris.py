# 基本ライブラリー
import numpy as np
import pandas as pd

# データセット
## データの読み込み
from sklearn.datasets import load_iris
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df.loc[df['target'] == 0, 'target'] = "setosa"
df.loc[df['target'] == 1, 'target'] = "versicolor"
df.loc[df['target'] == 2, 'target'] = "virginica"

# 予測モデル構築
X = iris.data[:, [0, 2]] 
y = iris.target

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
clf.fit(X, y)

# アプリ
import streamlit as st

## サイドパネル（インプット部）
st.sidebar.header('マーカーを移動させてください')

sepalValue = st.sidebar.slider('がく片の長さ (cm)', min_value=0.0, max_value=10.0, step=0.1)
petalValue = st.sidebar.slider('花弁の長さ  (cm)', min_value=0.0, max_value=10.0, step=0.1)

## メインパネル
st.title("## アヤメ分類アプリ")

st.write("## がく片、花弁の長さ")

### インプットデータ（1行のデータフレーム）
value_df = pd.DataFrame([],columns=['長さ','がく片の長さ (cm)','花弁の長さ (cm)'])
record = pd.Series(['長さ',sepalValue, petalValue], index=value_df.columns)
value_df = value_df.append(record, ignore_index=True)
value_df.set_index("長さ",inplace=True)

### 予測
pred_probs = clf.predict_proba(value_df)
pred_df = pd.DataFrame(pred_probs,columns=['setosa','versicolor','versinica'],index=['確率'])

### 結果出力
st.write(value_df)
st.write("## それぞれの確率")
st.write(pred_df)
name = pred_df.idxmax(axis=1).tolist()
st.write("## 結果")
st.write('このアヤメはおそらく',str(name[0]),"です")

