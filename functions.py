def read_todos_in_file():
    with open("todos.txt", "r", encoding="utf-8") as file:
        local_todos = file.readlines()
    return local_todos

def write_todos_in_file(todos):
    with open("todos.txt", "w", encoding="utf-8") as file:
        for todo in todos:
            file.write(todo)