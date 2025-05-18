import streamlit as st
import functions

st.title("My Todo App")
st.subheader("This is my tood app")
st.write("This app is to increase your productivity")

todos = functions.get_todo()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todo(todos)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(placeholder="enter todo", label="",
              key="new_todo", on_change=add_todo)

st.session_state
