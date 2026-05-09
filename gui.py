import support_functions as sf
import FreeSimpleGUI as Fsg

label = Fsg.Text("Type in a to do")
input_box = Fsg.InputText(tooltip="Enter to do", key="todo")
add_button = Fsg.Button("Add")
list_box =  Fsg.Listbox(values=sf.get_todos(),
                        key="todos",
                        enable_events=True,
                        size=[45, 10]
                        )
edit_button = Fsg.Button("Edit")

window = Fsg.Window('To-Do-App',
                    layout=[[label],[input_box, add_button],
                            [list_box, edit_button]],
                    font=("Helvetica", 20)
                    )
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = sf.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            sf.write_todos(todos)
            window["todos"].Update(values=todos)

        case "Edit":
            edit_todo = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = sf.get_todos()
            index = todos.index(edit_todo)
            todos[index] = new_todo
            sf.write_todos(todos)
            window["todos"].Update(values=todos)

        case "todos":
            window['todo'].update(value=values['todos'][0])
        case Fsg.WIN_CLOSED:
            break
window.close()