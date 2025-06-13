from taskmanager import TaskManager
from task import Task

"""Main CLI loop:
1. Initialize TaskManager
2. Load tasks from tasks.json
3. Display menu:
    - Add task
    - List tasks
    - List pending tasks
    - List done tasks
    - Mark task as done
    - Delete task
    - Save tasks
    - Exit
4. Loop and call TaskManager methods based on user input
5. Save tasks on exit"""
manager = TaskManager()


manager.load_tasks()
print("Welcome to Task Manager program.\n")

while True:
    command = input(    
        "Commands:\n"
        "1: Add task\n"
        "2: List tasks\n"
        "3: List pending tasks\n"
        "4: List done tasks\n"
        "5: Mark task as done\n"
        "6: Delete task\n"
        "7: Save tasks\n"
        "8: Exit\n"
        "Enter choice: "
    )

    if command not in {"1", "2", "3", "4", "5", "6", "7", "8"}:
        print("Invalid command.")
    else:
        match command:
            case "1":
                # prompt user for task info → call add_task
                title = input("\nWhat is the title of your task?\n").strip()
                while True:
                    due_date = input("Enter due date of your task as DD/MM/YYYY\n")
                    if len(due_date) == 10:

                        if due_date[0:2] <= "31" and (due_date[0:2].isdigit()):
                            
                            if due_date[2] == "/" and (due_date[5] == "/"):

                                if due_date[3:5].isdigit() and 1 <= int(due_date[3:5]) <= 12: #is digit comes first because casted int

                                    if due_date[6:10].isdigit() and int(due_date[6:10]) >= 2025:
                                        break
                    
                    print("Invalid try again.")
                while True:
                    priority = input("\n What is the priority?\n 1: High priority \n 2: Medium Priority \n 3: Low Priority ")
                    if priority in {"1", "2", "3"}:
                        break
                    else:
                        print("Invalid selection")

                manager.add_task(title, due_date, priority)
                print("\nTask Successfully added.")


            case "2":
                # call list_tasks
                manager.list_tasks()
            case "3":
                # call list_pending_tasks
                manager.list_pending_tasks()
            case "4":
                # call list_done_tasks
                manager.list_done_tasks()
            case "5":
                # prompt for index → call mark_done on that task
                try:
                    index = int(input("Enter the index of the task to mark done.") - 1)
                    task = manager.find_task(index)
                    task.mark_done()
                except ValueError:
                    print("Invalid input, enter a number.")

            case "6":
                # prompt for index → call delete_task
                try:
                    index = int(input("Enter the index of the task to delete.") - 1)
                    manager.delete_task(index)
                except ValueError:
                    print("Invalid input, enter a number.")
            case "7":
                # call save_tasks
                manager.save_tasks()
            case "8":
                manager.save_tasks()
                break  # exit app