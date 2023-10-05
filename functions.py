def get_todos(filepath="todos.txt"):
    with open(filepath, 'r') as file:
        todos_store = file.readlines()  # puts the file's contents to todos
    return todos_store


def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
    return

