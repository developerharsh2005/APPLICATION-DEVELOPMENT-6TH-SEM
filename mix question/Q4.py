from datetime import datetime

tasks = []

def add_task():
    title = input("Enter Title: ")
    priority = input("Enter Priority (High/Medium/Low): ")
    due_date = input("Enter Due Date (DD-MM-YYYY): ")
    status = "Pending"

    task = {
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "status": status
    }

    tasks.append(task)

    print("Task Added Successfully:")
    print("Title:", title)
    print("Priority:", priority)
    print("Due Date:", due_date)
    print("Status:", status)

def update_task_status():
    title = input("Enter task title to update status: ")
    for task in tasks:
        if task["title"] == title:
            task["status"] = input("Enter new status (Pending/Complete): ")
            print("Task status updated")
            return
    print("Task not found")

def display_by_priority():
    level = input("Enter priority level: ")
    print(level, "Priority Tasks:")
    count = 1
    for task in tasks:
        if task["priority"] == level:
            print(f"{count}. {task['title']} (Due: {task['due_date']})")
            print("Status:", task["status"])
            count += 1

def show_overdue_tasks():
    today = datetime.today()
    print("Overdue Tasks:")
    for task in tasks:
        due = datetime.strptime(task["due_date"], "%d-%m-%Y")
        if due < today and task["status"] == "Pending":
            print(task["title"], "(Due:", task["due_date"] + ")")

def delete_completed_tasks():
    global tasks
    tasks = [task for task in tasks if task["status"] != "Complete"]
    print("Completed tasks deleted")

while True:
    print("\n1. Add Task")
    print("2. Update Task Status")
    print("3. Display by Priority")
    print("4. Show Overdue Tasks")
    print("5. Delete Completed Tasks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        update_task_status()
    elif choice == "3":
        display_by_priority()
    elif choice == "4":
        show_overdue_tasks()
    elif choice == "5":
        delete_completed_tasks()
    elif choice == "6":
        break
    else:
        print("Invalid choice")
