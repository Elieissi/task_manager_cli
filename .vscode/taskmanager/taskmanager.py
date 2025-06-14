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
from pathlib import Path

class TaskManager:  # no underscore in class name

    def __init__(self):
        self.tasks = []  # list of Task objects

    def add_task(self, title, due_date, priority):
        # create new Task(title, due_date, priority)
        # append it to self.tasks
        self.tasks.append(Task(title,due_date, priority))


    def delete_task(self, index):
        # delete Task at given index from self.tasks
        del self.tasks[index]

    def list_tasks(self):
        # loop over self.tasks
        # print each Task with index
        n = 0
        for task in self.tasks:
            n += 1
            print(f"Task {n}: {task.title}")
            
    def list_pending_tasks(self):
        # loop over self.tasks
        # if status == "Pending", print the Task
        for task in self.tasks:
            if task.status == "Pending":
                print(task.title)

    def list_done_tasks(self):
        # loop over self.tasks
        # if status == "Done", print the Task
        for task in self.tasks:
            if task.status == "Done":
                print(task.title)


    def save_tasks(self):
        # for each Task in self.tasks:
        #     call to_dict() → get dict
        # build list of dicts
        # open cache.json in write mode
        # dump list of dicts to json
        with open("cache.json", "w") as file:
            for task in self.tasks:
                Task.to_dict()




    def load_tasks(self):
        # try to open cache.json
        # if file does not exist → set self.tasks to empty list
        # else:
        #     load json → gives list of dicts
        #     for each dict:
        #         call Task.from_dict(dict) → get Task object
        #         append Task object to self.tasks
        if Path("cache.json").exists():
            with open("cache.json", "r"):
                pass
        
        else:
            self.tasks = []
