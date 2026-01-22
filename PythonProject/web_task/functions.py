FILEPATH = "todos.txt"


def read_todos(filepath=FILEPATH):
    '''quando colocado na função, nao precisa repetir no código abaixo.
    Só precisa alterar caso o txt tenha mudado de nome ou local armazenado.'''
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


#caso queira que algo nao apareça no import
#precisa ter uma condição if, por exemplo:

if __name__ == "__main__":
    print(read_todos())