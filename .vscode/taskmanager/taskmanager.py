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
    - load_tasks() → load tasks from tasks.json
"""

from task import Task
import json

class TaskManager:  # no underscore in class name (correct Python style)

    def __init__(self):
        self.tasks = []  # list of Task objects

    def add_task(self, title, due_date, priority):
        pass

    def delete_task(self, index):
        pass

    def list_tasks(self):
        pass

    def list_pending_tasks(self):
        pass

    def list_done_tasks(self):
        pass

    def find_task(self, index):
        pass

    def save_tasks(self):
        pass

    def load_tasks(self):
        pass
