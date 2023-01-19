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
st.sidebar.header('Input Features')

sepalValue = st.sidebar.slider('sepal length (cm)', min_value=0.0, max_value=10.0, step=0.1)
petalValue = st.sidebar.slider('petal length (cm)', min_value=0.0, max_value=10.0, step=0.1)

## メインパネル
st.title("Iris Classifier")

st.write("## Input value")

### インプットデータ（1行のデータフレーム）
value_df = pd.DataFrame([],columns=['data','sepal length (cm)','petal length (cm)'])
record = pd.Series(['data',sepalValue, petalValue], index=value_df.columns)
value_df = value_df.append(record, ignore_index=True)
value_df.set_index("data",inplace=True)

### 予測
pred_probs = clf.predict_proba(value_df)
pred_df = pd.DataFrame(pred_probs,columns=['setosa','versicolor','virginica'],index=['probability'])

### 結果出力
st.write(value_df)
st.write("## Output probability")
st.write(pred_df)
name = pred_df.idxmax(axis=1).tolist()
st.write("## 結果")
st.write('このアイリスはおそらく',str(name[0]),"です")

