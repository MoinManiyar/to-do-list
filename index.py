tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def remove_task(index):
    if 1 <= index <= len(tasks):
        del tasks[index - 1]

while True:
    print("Choose an option:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        index = int(input("Enter the task number to remove: "))
        remove_task(index)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")