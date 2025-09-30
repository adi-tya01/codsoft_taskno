# To-Do List Program in Python

tasks = []

def show_menu():
    print("\n====== TO-DO LIST ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "status": "Pending"})
    print("✅ Task added!")

def view_tasks():
    if not tasks:
        print("📭 No tasks available!")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t['task']} [{t['status']}]")

def update_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_no = int(input("Enter task number to update: "))
        if 1 <= task_no <= len(tasks):
            new_task = input("Enter new task description: ")
            tasks[task_no - 1]["task"] = new_task
            print("🔄 Task updated!")
        else:
            print("❌ Invalid task number")
    except ValueError:
        print("❌ Please enter a valid number")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
            print("🗑️ Task deleted!")
        else:
            print("❌ Invalid task number")
    except ValueError:
        print("❌ Please enter a valid number")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice, try again!")
