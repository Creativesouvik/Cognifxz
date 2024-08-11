class Task:
    def __init__(self, task_id, title, description):
        self.id = task_id
        self.title = title
        self.description = description

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Description: {self.description}"


def create_task(task_list, task_id, title, description):
    new_task = Task(task_id, title, description)
    task_list.append(new_task)
    print("Task created successfully!")


def read_tasks(task_list):
    if not task_list:
        print("No tasks available.")
    else:
        for task in task_list:
            print(task)


def update_task(task_list, task_id, new_title, new_description):
    for task in task_list:
        if task.id == task_id:
            task.title = new_title
            task.description = new_description
            print("Task updated successfully!")
            return
    print("Task not found.")


def delete_task(task_list, task_id):
    for task in task_list:
        if task.id == task_id:
            task_list.remove(task)
            print("Task deleted successfully!")
            return
    print("Task not found.")


def main():
    task_list = []
    task_id_counter = 1

    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            create_task(task_list, task_id_counter, title, description)
            task_id_counter += 1
        elif choice == "2":
            read_tasks(task_list)
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            new_title = input("Enter new task title: ")
            new_description = input("Enter new task description: ")
            update_task(task_list, task_id, new_title, new_description)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_list, task_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
