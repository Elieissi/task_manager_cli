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
        # convert each Task object to a dictionary
        task_dicts = []
        for task in self.tasks:
            task_data = task.to_dict()
            task_dicts.append(task_data)

        # write the list of task dictionaries to the JSON file
        with open("cache.json", "w") as file:
            json.dump(task_dicts, file, indent=4)





    def load_tasks(self):

        #Use path to check if file exists.
        #Put json into variable and for each dict in the json translate it
        #Put newly translated object into list of tasks
        #Check edgecase if the file exists but empty then set to empty list
        if Path("cache.json").exists():
            try:
                with open("cache.json", "r") as file:
                    loaded = json.load(file)
                    for dic in loaded:
                        obj = Task.from_dict(dic)
                        self.tasks.append(obj)
            except json.JSONDecodeError:
                self.tasks = []
        else:
            self.tasks = []

    @staticmethod
    def valid_date_checker():
        while True:
            due_date = input("Enter due date of your task as DD/MM/YYYY\n")
            if len(due_date) == 10:

                if due_date[0:2] <= "31" and (due_date[0:2].isdigit()):
                            
                    if due_date[2] == "/" and (due_date[5] == "/"):

                        if due_date[3:5].isdigit() and 1 <= int(due_date[3:5]) <= 12: #is digit comes first because casted int

                            if due_date[6:10].isdigit() and int(due_date[6:10]) >= 2025:
                                return due_date
                    
            print("Invalid try again.")
