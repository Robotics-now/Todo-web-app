def show_numbered_list(todos):
    ''' Print a nubered list of to-do items from a list '''
    # new_todos = [item.strip('\n') for item in todos]. Could be also used to strip \n

    for index, i in enumerate(todos):
        i = i.strip('\n')
        print(f"{index + 1}. {i.capitalize()}")

def r_wFromFile(mode = "r", todos=[]):
    '''Reads from or writes to ToDo.txt file based on mode parameter
    mode: "r" for read, "w" for write'''

    with open("ToDo.txt", mode) as file_local:
        match mode:
            case "r":
                todos = file_local.readlines()
                return todos
            case "w":
                file_local.writelines(todos)
                return todos

if __name__ == "__main__":
    pr = "No Error\n run cli.py or gui.py to\
    use the To-Do application.".replace('    ', ' ')
    print(pr)