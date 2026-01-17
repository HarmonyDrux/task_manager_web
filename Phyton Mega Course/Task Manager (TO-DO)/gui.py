import functions
import FreeSimpleGUI as sg
import emoji

label = sg.Text(f"Type an TO-DO {emoji.emojize(':thinking_face:')}")
input_box = sg.InputText(tooltip='Enter todo', key="todo")
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.read_todos(), key="todos",
                      enable_events=True, size=(45,10))
edit_button = sg.Button('Edit')

window = sg.Window(f'TO-DO {emoji.emojize(':memo:')} App',
                   layout=[[label], [input_box, add_button],[list_box, edit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read() #Mostra tudo o que foi executado pelo usuário no gui.
    # Ex: event: Add pois o usuário clicou em add,
    # values = {'todo': 'clean bathroom'} pois o usuario digitou clean bathroom
    match event:
        case "Add":
            todos = functions.read_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo.capitalize())
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = functions.read_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo.capitalize()
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            '''fecha o GUI prevenindo que tenha erro na GUI'''
            break

window.close()