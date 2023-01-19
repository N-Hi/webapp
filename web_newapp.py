import streamlit as st
import networkx as nx
from mypulp import GRB, Model, quicksum, multidict, tuplelist


model=Model("lo1")

#ユーザーからの入力を取得
formula1 = st.text_input("数式1")
formula2 = st.text_input("数式2")
formula3 = st.text_input("数式3")
formula4 = st.text_input("数式4")

formulaX = st.text_input("求めたいもの（式でも可）")

#最大、最少を求め、結果出す
model.addConstr(formula1)
model.addConstr(formula2)
model.addConstr(formula3)
model.addConstr(formula4)

#最大値
model.setObjective(formulaX,GRB.MAXIMIZE)

model.optimize()

result_MAX = model.ObjVal
st.write("最大値:")
st.write("result_MAX")

#最小値
model.setObjective(formulaX,GRB.MINIMIZE)

model.optimize()

result_MIN = model.ObjVal
st.write("最小値:")
st.write("result_MIN")





