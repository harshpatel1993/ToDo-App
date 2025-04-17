
import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip = "Enter ToDo", key="input_todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values = functions.get_todos(),
                      key ="todos",
                      enable_events=True,
                      size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=("Helvetica",10))
while True:
    event,values = window.read()
    print(1,event)
    print(2,values)
    print(3,values["todos"])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["input_todo"] +"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["input_todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo +"\n"
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Complete":
            todo_to_complete=values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["input_todo"].update("")
        case "Exit":
            break
        case "todos":
            window["input_todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break


window.close()