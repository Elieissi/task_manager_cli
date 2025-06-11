from taskmanager import Task_manager
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