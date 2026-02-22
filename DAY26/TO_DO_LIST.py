# ==============================
# TO-DO LIST PROJECT
# ==============================

import os

FILENAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append("[ ] " + task)
    save_tasks(tasks)
    print("Task added successfully!")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_no = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_no - 1)
        save_tasks(tasks)
        print(f"Removed: {removed}")
    except (ValueError, IndexError):
        print("Invalid task number!")

def mark_completed(tasks):
    show_tasks(tasks)
    try:
        task_no = int(input("Enter task number to mark completed: "))
        tasks[task_no - 1] = tasks[task_no - 1].replace("[ ]", "[✓]")
        save_tasks(tasks)
        print("Task marked as completed!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()