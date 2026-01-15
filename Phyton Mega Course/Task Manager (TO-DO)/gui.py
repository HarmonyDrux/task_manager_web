import functions
import FreeSimpleGUI as sg
import emoji

label = sg.Text(f"Type an TO-DO {emoji.emojize(':thinking_face:')}")
input_box = sg.InputText(tooltip='Enter todo')
add_button = sg.Button('Add')

window = sg.Window(f'TO-DO {emoji.emojize(':memo:')} App', layout=[[label], [input_box, add_button]])
window.read()
window.close()