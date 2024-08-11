import json
import os

TASKS_FILE = 'tasks.txt'

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as file:
                for line in file:
                    tasks.append(json.loads(line.strip()))
        except Exception as e:
            print(f"Error loading tasks: {e}")
    return tasks

def save_tasks(tasks):
    try:
        with open(TASKS_FILE, 'w') as file:
            for task in tasks:
                file.write(json.dumps(task) + '\n')
    except Exception as e:
        print(f"Error saving tasks: {e}")

def create_task(tasks, title, description):
    task = {'id': len(tasks) + 1, 'title': title, 'description': description}
    tasks.append(task)
    save_tasks(tasks)
    return task

def read_task(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

def update_task(tasks, task_id, title=None, description=None):
    for task in tasks:
        if task['id'] == task_id:
            if title:
                task['title'] = title
            if description:
                task['description'] = description
            save_tasks(tasks)
            return task
    return None

def delete_task(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return True
    return False

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Create Task\n2. Read Task\n3. Update Task\n4. Delete Task\n5. List Tasks\n6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = create_task(tasks, title, description)
            print(f"Task created: {task}")

        elif choice == '2':
            task_id = int(input("Enter task ID: "))
            task = read_task(tasks, task_id)
            if task:
                print(f"Task: {task}")
            else:
                print("Task not found.")

        elif choice == '3':
            task_id = int(input("Enter task ID: "))
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            task = update_task(tasks, task_id, title, description)
            if task:
                print(f"Task updated: {task}")
            else:
                print("Task not found.")

        elif choice == '4':
            task_id = int(input("Enter task ID: "))
            if delete_task(tasks, task_id):
                print("Task deleted.")
            else:
                print("Task not found.")

        elif choice == '5':
            for task in tasks:
                print(f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}")

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
