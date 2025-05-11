# To-Do List App in Python

# This list will hold our tasks
todo_list = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print(f"Added task: {task}")

def view_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for index, item in enumerate(todo_list):
            status = "Done" if item["completed"] else "Not Done"
            print(f"{index + 1}. {item['task']} - [{status}]")

def mark_task_completed():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= task_num < len(todo_list):
            todo_list[task_num]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(todo_list):
            removed = todo_list.pop(task_num)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# This is the main loop of the app
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_task_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
