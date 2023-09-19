import streamlit as st
from functions import read_todos_in_file, write_todos_in_file

#streamlit run web.py - для запуска приложения

todos = read_todos_in_file()

st.title("My Todo App")
st.subheader("Моё приложение")
st.write("Это приложение для повышения вашей продуктивности")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos_in_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos_in_file(todos)

st.text_input(label="Нажмите Enter, чтобы добавить дело", placeholder="Введите дело...",
              on_change=add_todo, key="new_todo")