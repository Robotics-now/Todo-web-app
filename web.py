import streamlit as st
from func import r_wFromFile
import json

with open("data.json", "r") as json_file:
    data = json.load(json_file)

todos = r_wFromFile()

def addwebtodo():
    todo = st.session_state['newtodo']
    todos.append(todo + '\n')
    r_wFromFile("w", todos)

st.title(data['app_name'])
st.subheader("Welcome to the Web Page")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        r_wFromFile("w", todos)
        del st.session_state[todo]
        st.rerun()
       
st.text_input(label=data['enter_str'], placeholder="Add new todo...", 
              on_change=addwebtodo, key='newtodo')