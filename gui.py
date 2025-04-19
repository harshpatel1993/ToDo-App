
import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("files/todos.txt"):
    with open ("files/todos.txt","w") as file:
        pass

sg.theme("black")

clock_label = sg.Text("", key ="clock")
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip = "Enter ToDo", key="input_todo")
add_button = sg.Button(size = 2, image_source="add.png", mouseover_colors="LightBlue2",
                       tooltip = "Add Todo",  key = "Add")
list_box = sg.Listbox(values = functions.get_todos(),
                      key ="todos",
                      enable_events=True,
                      size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button(size = 2, image_source="complete.png", mouseover_colors="LightBlue2",
                       tooltip = "Complete Todo",  key = "Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock_label],
                           [label],
                           [input_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=("Helvetica",15))
while True:
    event,values = window.read(timeout=1000)
    window["clock"].update(value = time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            if values["input_todo"] == "":
                sg.popup("No ToDo to Enter.",font=("Helvetica",15))
            else:
                todos = functions.get_todos()
                new_todo = values["input_todo"] +"\n"
                todos.append(new_todo)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["input_todo"].update("")

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["input_todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo +"\n"
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.",font=("Helvetica",20))
        case "Complete":
            try:
                todo_to_complete=values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["input_todo"].update("")
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Exit":
            break
        case "todos":
            window["input_todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break


window.close()