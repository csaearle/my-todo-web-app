import streamlit as st
import functions

def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my my my todo App")
st.write("This app is to improve your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        print(todo, checkbox)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo",
              placeholder="Add a new todo item to list here......",
              on_change=add_todo, key='new_todo')
