## Function for read data from file
def get_todos():
    ## Read current file
    with open('todos.txt', 'r') as file_frm_fun:
        to_dos_frm_fun = file_frm_fun.readlines()
    return to_dos_frm_fun

## Function for write data in file
def write_todos(todos_fun):
    ## Write in file
    with open('todos.txt', 'w') as file_for_write:
        file_for_write.writelines(todos_fun)

if __name__ == "__main__":
    print("hello world")
    print(get_todos())