"""TaskManager class:
- Properties:
    - tasks (list of Task objects)

- Methods:
    - add_task(title, due_date, priority)
    - delete_task(index or id)
    - list_tasks()
    - list_pending_tasks()
    - list_done_tasks()
    - find_task(index or id)
    - save_tasks() → write tasks to tasks.json
    - load_tasks() → load tasks from tasks.json"""

from task import Task

class Task_manager:
    pass