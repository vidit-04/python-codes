import os

TODO_FILE = "todo.txt"

def load_tasks():
    """Load tasks from the file."""
    if not os.path.isfile(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        tasks = [task.strip() for task in file.readlines()]
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("No tasks to display.")
    else:
        print("Your to-do list:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def delete_task(tasks):
    """Delete a task from the list."""
    display_tasks(tasks)
    task_number = int(input("Enter the number of the task to delete: "))
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' deleted.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
