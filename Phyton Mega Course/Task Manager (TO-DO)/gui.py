import functions
import FreeSimpleGUI as sg
import emoji

label = sg.Text(f"Type an TO-DO {emoji.emojize(':thinking_face:')}")
input_box = sg.InputText(tooltip='Enter todo', key="todo")
add_button = sg.Button('Add')

window = sg.Window(f'TO-DO {emoji.emojize(':memo:')} App',
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read() #Mostra tudo o que foi executado pelo usuário no gui.
    # Ex: event: Add pois o usuário clicou em add,
    # values = {'todo': 'clean bathroom'} pois o usuario digitou clean bathroom
    match event:
        case "Add":
            todos = functions.read_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            '''fecha o GUI prevenindo que tenha erro na GUI'''
            break

window.close()