import streamlit as st
import functions

todos = functions.read_todos()

def add_todo():
    '''adiciona uma nova tarefa'''

    todo = st.session_state['new_todo'] + "\n" #st.session_state é um library, nesse caso tudo o que for
    # digitado no input,entrará na library e retornar ao todos.txt para que seja acrescentado na lista
    todos.append(todo.capitalize())
    functions.write_todos(todos)

st.title('Task Manager')
st.subheader('This is my todo app.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index) #caso o usuário faz o check na caixinha, a tarefa sera removida tanto no txt
        # quanto na interface
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Enter a todo: ", on_change=add_todo,key='new_todo')