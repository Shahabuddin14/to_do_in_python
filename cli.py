from support_functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input('Enter Add, Show Edit, Complete or Exit : ')
    user_action = user_action.strip().capitalize()

    if user_action.startswith('Add'):
        to_do = user_action[4:]

        ## Call the function
        to_dos = get_todos()

        to_dos.append(to_do + '\n')

        write_todos(to_dos)

    elif user_action.startswith('Show'):
        ## Call the function
        to_dos = get_todos()

        for index, item in enumerate(to_dos):
            item = item.strip('\n')
            row = f'{index+1} --> {item}'
            print(row)

    elif user_action.startswith('Edit'):
        try:
            num = int(user_action[5:])
            num = num - 1

            ## Call the function
            to_dos = get_todos()

            if num < 0 or num >= len(to_dos):
                print('Invalid todo number')
                continue

            new_todo = input('Enter new todo : ')
            to_dos[num] = new_todo + '\n'

            write_todos(to_dos)

        except ValueError:
            print('Invalid input')
            continue

    elif user_action.startswith('Complete'):
        try:
            num = int(user_action[9:])

            ## Call the function
            to_dos = get_todos()

            index = num - 1

            if index < 0 or index >= len(to_dos):
                print('Invalid todo number')
                continue

            todo_to_complete = to_dos[index].strip('\n')
            to_dos.pop(index)

            write_todos(to_dos)

            message = f"This todo was {todo_to_complete} completed successfully"
            print(message)
        except IndexError:
            print('Invalid input')
            continue
        except ValueError:
            print('Invalid input')
            continue

    elif user_action.startswith('Exit'):
        break

    else:
        print('Invalid input')
