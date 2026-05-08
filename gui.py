import support_functions as sf
import FreeSimpleGUI as Fsg

label = Fsg.Text("Type in a to do")
input_box = Fsg.InputText(tooltip="Enter to do", key="todo")
add_button = Fsg.Button("Add")

window = Fsg.Window('To-Do-App',
                    layout=[[label],[input_box, add_button]],
                    font=("Helvetica", 12)
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
        case Fsg.Win_Close:
            break
window.close()