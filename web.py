import streamlit as st
import support_functions as sf

todos = sf.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    sf.write_todos(todos)


st.title("My TO-DO App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        sf.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter todo", placeholder='Complete python', on_change=add_todo, key='new_todo')