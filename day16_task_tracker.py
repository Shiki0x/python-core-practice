import json

FILENAME = "tasks.json"
MENU_OPTIONS = {
    "1": "Add task",
    "2": "List tasks",
    "3": "Toggle task",
    "4": "Delete task",
    "5": "Save & Exit"
}

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter a task: ").strip()

    if not title:
        print("Task cannot be empty.")
        return

    tasks.append({
        "title": title,
        "done": False
    })

def list_tasks(tasks):
    if not tasks:
        print("You have no tasks.")
        return
    
    for i, task in enumerate(tasks, start=1):
        status = '[x]' if task["done"] else '[ ]'
        print(f"{i}. {status} {task['title']}")

def toggle_task(tasks):
    if not tasks:
        print("No tasks to toggle.")
        return
    
    list_tasks(tasks)

    try:
        choice = int(input("Choose task number: "))
        index = choice - 1
    except ValueError:
        print("Please enter a number.")
        return
    
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return
    
    tasks[index]["done"] = not tasks[index]["done"]
    print("Task updated.")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    
    list_tasks(tasks)

    try:
        choice = int(input("Choose task number: "))
        index = choice - 1
    except ValueError:
        print("Please enter a number.")
        return
    
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return
        
    removed_task = tasks.pop(index)
    print(f"Removed task: {removed_task['title']}")

def print_menu():
    print("\n--- Task Manager ---")
    for key, label in MENU_OPTIONS.items():
        print(f"{key}. {label}")

def main():
    tasks = load_tasks()

    while True:
        print_menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            toggle_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

main()
