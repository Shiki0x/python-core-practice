import json

FILENAME = "categorized_tasks.json"

def load_data():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    
    if not isinstance(data, dict):
        return {}
    
    cleaned = {}

    for category, tasks in data.items():
        if not isinstance(category, str):
            continue

        if not isinstance(tasks, list):
            cleaned[category] = []
            continue
        
        cleaned[category] = [
            task for task in tasks if is_valid_task(task)
        ]

        return cleaned

def save_data(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

def add_category(data):
    category = input("Create a category: ").strip()

    if not category:
        print("Category name cannot be empty.")
        return
    
    if category in data:
        print("Category already exists.")
        return

    data[category] = []
    print(f"Category '{category}' created.")

def choose_category(data):
    if not data:
        print("No categories created.")
        return None
    
    categories = list(data.keys())

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    try:
        choice = int(input("Choose category number: "))
        index = choice - 1
    except ValueError:
        print("Please enter a number.")
        return
    
    if index < 0 or index >= len(categories):
        print("Invalid category number.")
        return
    
    return categories[index]

def add_task(data):
    category = choose_category(data)
    if category is None:
        return

    title = input("Enter a task: ").strip()
    if not title:
        print("Task cannot be empty.")
        return
    
    new_task = {"title": title, "done": False}

    if not is_valid_task(new_task):
        print("Invalid task data.")

    data[category].append(new_task)
    print(f"Task added to '{category}'.")

def list_tasks(data):
    category = choose_category(data)
    if category is None:
        return
    
    tasks = data[category]

    if not tasks:
        print("You have no tasks in this category.")
        return
    
    for i, task in enumerate(tasks, start=1):
        status = '[x]' if task["done"] else '[ ]'
        print(f"{i}. {status} {task['title']}")

def toggle_task(data):
    category = choose_category(data)
    if category is None:
        return
    
    tasks = data[category]

    if not tasks:
        print("No tasks in this category.")
        return

    try:
        choice = int(input("Choose a task number: "))
        index = choice - 1
    except ValueError:
        print("Please enter a number.")
        return
    
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return
    
    tasks[index]["done"] = not tasks[index]["done"]
    print("Task updated.")

def delete_task(data):
    category = choose_category(data)
    if category is None:
        return
    
    tasks = data[category]

    if not tasks:
        print("No tasks to delete in this category.")
        return
    
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

def is_valid_task(task):
    if not isinstance(task, dict):
        return False
    
    if "title" not in task or "done" not in task:
        return False
    
    if not isinstance(task["title"], str) or not task["title"].strip():
        return False
    
    if not isinstance(task["done", bool]):
        return False
    
    return True

def main():
    data = load_data()

    while True:
        print("\n--- Category Task Manager ---")
        print("1. Add a category.")
        print("2. Choose a category.")
        print("3. Add a task.")
        print("4. List tasks.")
        print("5. Toggle task.")
        print("6. Delete task.")
        print("7. Save & Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_category(data)
        elif choice == "2":
            category = choose_category(data)
            if category is not None:
                print(f"You selected: {category}")
        elif choice == "3":
            add_task(data)
        elif choice == "4":
            list_tasks(data)
        elif choice == "5":
            toggle_task(data)
        elif choice == "6":
            delete_task(data)
        elif choice == "7":
            save_data(data)
            print("Categories saved!")
            break
        else:
            print("Invalid choice. Please select 1-7.")

main()