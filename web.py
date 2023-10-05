import streamlit as st
import functions

if 'key' not in st.session_state:
    st.session_state['key'] = 'value'
todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    print(todo)
    functions.write_todos(todos)

    


st.title("My Todo App")
st.subheader("Welcome!")
st.write("Increase your productivity!")

st.text_input(label = "Enter your todo:", placeholder="Add a new todo....", 
              on_change=add_todo, key='new_todo')


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo) #
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

# for index,todo in enumerate(todos):
#     col1, col2 = st.columns([2, 8])
    
#     with col2: 
#         st.markdown(todo)
#     with col1:
#         delete = st.button(f":wastebasket: {index+1}.)", key= todo) # 
#     if delete:
#         todos.pop(index)
#         functions.write_todos(todos)
#         del st.session_state[todo]
#         st.rerun()

