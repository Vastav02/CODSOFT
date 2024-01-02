import os
def display_menu():
    print("To-Do List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Quit")
def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        if not tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
def add_task():
    task = input("Enter the task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")
def mark_completed():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 0 <= task_index < len(tasks):
            tasks[task_index] = "[Completed] " + tasks[task_index]
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
    
    input("Press Enter to continue...")
    os.system('clear' if os.name == 'posix' else 'cls')  
