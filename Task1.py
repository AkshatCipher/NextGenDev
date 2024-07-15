tasks = []
n=1
def add_task(task_name):
    tasks.append({"task_name": task_name, "completed": False})
    print("Task ",task_name," added.")

def remove_task(task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task at index ",task_index," removed.")
    else:
        print("Invalid task index.")

def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task at index ",task_index," marked as completed.")
    else:
        print("Invalid task index.")

def update_task(task_index, new_task_name):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["task_name"] = new_task_name
        print("Task at index ",task_index," updated to ",new_task_name,".")
    else:
        print("Invalid task index.")

def display_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            print("Index:",index,", Task:",task['task_name'],", Status: ",status)

while n!=0:
    print(" To-Do List ")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. View All Tasks")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        task_name = input("Enter task name: ")
        add_task(task_name)
    elif choice == '2':
        display_tasks()
        task_index = int(input("Enter index of task to remove: "))
        remove_task(task_index)
    elif choice == '3':
        display_tasks()
        task_index = int(input("Enter index of task to mark as completed: "))
        complete_task(task_index)
    elif choice == '4':
        display_tasks()
        task_index = int(input("Enter index of task to update: "))
        new_task_name = input("Enter new task name: ")
        update_task(task_index, new_task_name)
    elif choice == '5':
        display_tasks()
    elif choice == '6':
        print("Exiting program.")
        n=0
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")