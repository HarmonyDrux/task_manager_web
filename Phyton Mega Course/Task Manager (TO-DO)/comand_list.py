from datetime import datetime

from functions import read_todos, write_todos
import time

now = time.strftime("%d/%m/%Y %H:%M")
print(now)
while True:
    user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit': ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = read_todos()

        todos.append(todo.capitalize() + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):
      todos = read_todos()

      for index, item in enumerate(todos):
        item = item.strip("\n")
        row = f"{index + 1}- {item}"
        print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = read_todos()

            new_todo = input("Enter a new to-do: ")
            todos[number] = new_todo.capitalize()

            write_todos(todos)
        except ValueError:
            print("Your command is not valid. Please try again.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = read_todos()

            index = number - 1
            todo_complete = todos[index]
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            todos.pop(number-1)

            write_todos(todos)

            print(f"Todo complete: {todo_complete}")
        except IndexError:
            print("That's no item with that number. Please try again.")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Command not recognised")

print("Bye!!")