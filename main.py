from time import strftime

# from functions import get_todos,write_todos

import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action=user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]


        # file =open("files/todos.txt", "r")
        # todos = file.readlines()
        # file.close()

        # above code can be written as follows as
        # using with clause we do not need to close the file, the with clause will close it automatically
        todos = functions.get_todos()

        todos.append(todo +"\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos=functions.get_todos()

        # comprehensive list
        new_todos= [item.strip("\n") for item in todos]


        for index, item in enumerate(new_todos):
            print(f"{index+1}.{item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5])
            number = number -1

            todos=functions.get_todos()

            new_todo = input("Enter new ToDo:")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos=functions.get_todos()

            index = number -1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)
            print(f"Todo {todo_to_remove} was removed from the list.")
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Not valid command.")



