# ====================================================

# Project: To-Do Tasks Application
# Author: Muhammad Ahtsham Javed
# Language: Python
# version: 1.0

# ====================================================
separator = "-" * 50

#--------------Menu-----------------
def menu():
    print(separator)
    print("     Welcome to To-Do Tasks Application     ")
    print(separator)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Mark Task as Done")
    print("5. Delete Task")
    print("6. Exit")
    return input("Please select an option (1-6): ").strip()

#--------------View Tasks-----------------
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "[Done]" if task.startswith("[Done] ") else "[Pending]"
            print(f"{index}. {status} {task.replace('[Done] ', '')}")

#--------------Add Task-----------------
def add_task(tasks):
    task = input("Enter the task you want to add: ").strip()

    if not task:
        print("\nTask cannot be empty. Please enter a task.")
        return

    if task.lower() in [existing.lower() for existing in tasks]:
        print(f"\n'{task}' is already in your list. Try a different task.")
        return

    tasks.append(task)
    print(f"\nTask '{task}' added successfully.")

#--------------Edit Task-----------------
def edit_task(tasks):
    if not tasks:
        print("\nNo tasks available to edit.")
        return

    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to edit: ").strip())
        if 1 <= task_number <= len(tasks):
            old_task = tasks[task_number - 1]
            new_task = input("Enter the new task name: ").strip()
            if not new_task:
                print("\nTask cannot be empty. Please enter a task.")
                return
            if new_task.lower() in [task.lower() for task in tasks if task != old_task]:
                print(f"\n'{new_task}' is already in your list. Try a different task.")
                return
            tasks[task_number - 1] = new_task
            print(f"\nTask updated successfully.")
        else:
            print("\nInvalid task number. Please try again.")
    except ValueError:
        print("\nInvalid input. Please enter a valid task number.")

#--------------Mark Task as Done-----------------
def mark_done(tasks):
    if not tasks:
        print("\nNo tasks available to mark as done.")
        return

    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as done: ").strip())
        if 1 <= task_number <= len(tasks):
            task = tasks[task_number - 1]
            if task.startswith("[Done] "):
                print("\nThis task is already marked as done.")
            else:
                tasks[task_number - 1] = f"[Done] {task}"
                print(f"\nTask '{task}' marked as done.")
        else:
            print("\nInvalid task number. Please try again.")
    except ValueError:
        print("\nInvalid input. Please enter a valid task number.")

#--------------Delete Task-----------------
def delete_task(tasks):
    if not tasks:
        print("\nNo tasks available to delete.")
    else:
        view_tasks(tasks)
        try:
            task_number = int(input("Enter the task number to delete: ").strip())
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"\nTask '{removed_task}' deleted successfully.")
            else:
                print("\nInvalid task number. Please try again.")
        except ValueError:
            print("\nInvalid input. Please enter a valid task number.")


#--------------Main Program-----------------
def main():
    tasks = []
    while True:
        print()
        choice = menu()
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            mark_done(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            print("\nExiting the application. Goodbye!\n")
            break
        else:
            print("\nInvalid option. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
        