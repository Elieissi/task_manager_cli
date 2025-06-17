from taskmanager import TaskManager

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
        "8: Edit tasks\n"
        "9: Exit\n"
        "Enter choice: "
    )

    if command not in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
        print("Invalid command.")
    else:
        match command:
            case "1":
                # prompt user for task info → call add_task
                title = input("\nWhat is the title of your task?\n").strip()
                manager.valid_date_checker()
                while True:
                    priority = input("\n What is the priority?\n 1: High priority \n 2: Medium Priority \n 3: Low Priority ")
                    if priority in {"1", "2", "3"}:
                        break
                    else:
                        print("Invalid selection")
                
                #change to words
                if priority == "1":
                    priority = "High"
                elif priority == "2":
                    priority = "Medium"
                else: priority = "Low"
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
                    index = int(input("Enter the index of the task to mark done.")) - 1
                    manager.tasks[index].mark_done()
                except ValueError:
                    print("Invalid input, enter a number.")
                except IndexError:
                    print("Invalid index.")

            case "6":
                # prompt for index → call delete_task
                try:
                    index = int(input("Enter the index of the task to delete.")) - 1
                    manager.delete_task(index)
                except ValueError:
                    print("Invalid input, enter a number.")
                except IndexError:
                    print("Invalid Index.")
            case "7":
                # call save_tasks
                manager.save_tasks()
            case "8":
                action = input("\nWhat is the Action?\n1: Edit due date\n2: Edit Title\n3: Edit Priority\n")
                
                if action in {"1", "2", "3"}:
                    try:
                        index = int(input("Enter the index of the task to edit: ")) - 1
                        task = manager.tasks[index]
                    except ValueError:
                        print("Invalid input, enter a number.")
                    except IndexError:
                        print("Invalid index.")
                    else:
                        if action == "1":
                            due_date = manager.valid_date_checker()
                            task.set_due_date(due_date)
                        elif action == "2":
                            new_title = input("Enter new title: ").strip()
                            task.set_title(new_title)
                        elif action == "3":
                            
                            while True:
                                new_priority = input("Enter new priority \n 1: High\n 2: Medium\n 3: Low ").strip()
                                if new_priority in {"1", "2", "3"}:
                                    task.set_priority(new_priority)
                                    break

                                else: 
                                    print("Invalid selection.")
                            
                else:   
                    print("Invalid selection")

                
            case "9":
                manager.save_tasks()
                break #exits