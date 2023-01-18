import streamlit as st
import networkx as nx

# 空のグラフを作成
G = nx.Graph()

st.title("経路最適化アプリ")

# ユーザーからの入力を取得
start = st.text_input("出発地を入力してください:")
destinations = st.text_input("目的地を入力してください(カンマ区切り):").split(",")

# グラフにエッジを追加
for destination in destinations:
    G.add_edge(start, destination)

# 最短経路を探す
shortest_route = nx.shortest_path(G, start, destinations[-1])

st.write("最短経路:")
st.write(shortest_route)




