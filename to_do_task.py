tasks = {}

def add_tasks():
    task_name = input("Enter task name: ")
    task_priority = input("Enter task priority (High, Medium, Low)")
    tasks[task_name] = task_priority
    print(f"Task '{task_name}' added with priority '{task_priority}'")

def view_tasks():
    if not tasks:
        print("No tasks avilable. ")
    else:
        print("Current Tasks: ")
        for task, priority, in tasks.items():
            print(f"- {task} (priority: {priority})")
            
        
def remove_task():
    if not tasks:
        print("No tasks avilable to remove")
        return
    
    tasks_to_remove = input("Enter the task name to remove: ")
    if tasks_to_remove in tasks:
        del tasks[tasks_to_remove]
        print(f"Task '{tasks_to_remove}' removed")
    else:
        print(f"Tasks '{tasks_to_remove}' not found. ")

while True:
    print("\nTask Management System:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1, 2, 3, or 4)")

    if choice == "1":
        add_tasks()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting the task management system. Goodbye!")
        break  

