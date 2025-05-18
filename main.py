# add items
def add_task(item):
    with open("items.txt", "a") as file:
        file.write(item + "\n")
        print("Task added successfully!")

# view items
def view_all_tasks():
    try:
        with open("items.txt", "r") as file:
            lines = file.readlines()
            if len(lines):
                for line in lines:
                    print(line.strip())
            else:
                print("No tasks added yet")
    except FileNotFoundError:
        print("Tasks file not found!")

# update items
def update_task(row, task):
    try:
        with open("items.txt", "r+") as file:
            lines = file.readlines()
            if 1 <= row <= len(lines):
                lines[row - 1] = task + "\n"
                file.seek(0)
                file.writelines(lines)
                file.truncate()
                print("Updated successfully!")
            else:
                print("Invalid task number")
    except FileNotFoundError:
        print("Tasks file not found!")

# delete items
def delete_task(index):
    try:
        with open("items.txt", "r+") as file:
            lines = file.readlines()
            if 1 <= index <= len(lines):
                del lines[index - 1]
                file.seek(0)
                file.writelines(lines)
                file.truncate()
                print("Task deleted successfully!")
            else:
                print("Invalid task number!")
    except FileNotFoundError:
        print("Tasks file not found!")

# display default instructions
def print_default_instructions():
    print("=================CLI To-DO App==================")
    print("1 -> Create a new task")
    print("2 -> View all tasks")
    print("3 -> Update a task")
    print("4 -> Delete a task")
    print("5 -> Quit")

# main method
if __name__ == '__main__':
    while True:
        print_default_instructions()
        try:
            selected_option = int(input("Select an option from above: "))
            if selected_option == 1:
                new_item = input("Enter the new item: ")
                add_task(new_item)
            elif selected_option == 2:
                view_all_tasks()
            elif selected_option == 3:
                task_no = int(input("Enter the task number which should be updated: "))
                new_task = input("Enter the new task: ")
                update_task(task_no, new_task)
            elif selected_option == 4:
                task_id = int(input("Enter the task number to delete: "))
                delete_task(task_id)
            elif selected_option == 5:
                print("Thanks for using the CLI To-Do App!")
                exit()
            else:
                print("Invalid option! please enter the correct option number(1-5).")
        except ValueError:
            print("Invalid input! Please enter a number")