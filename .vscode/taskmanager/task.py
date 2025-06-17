"""Task class:
- Properties:
    - title
    - due_date
    - priority
    - status (Pending/Done)

- Methods:
    - mark_done()
    - set_due_date()
    - set_title()
    - set_priority()
    - to_dict() → convert Task to dict for saving
    - from_dict(dict) → create Task from saved dict
"""

class Task:
    def __init__(self, title, due_date, priority):
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.status = "Pending"  # always Pending on creation, one less thing to prompt user

    def mark_done(self):
        self.status = "Done"

    def set_due_date(self, due_date):
        # update due_date
        self.due_date = due_date

    def set_title(self, new_title):
        # update title
        self.title = new_title

    def set_priority(self, new_priority):
        # update priority
        if new_priority == "1":
            new_priority = "High"
        elif new_priority == "2":
            new_priority = "Medium"
        else: new_priority = "Low"
        self.priority = new_priority

    def to_dict(self):
        # build dict with title, due_date, priority, status
        # return the dict
        data_dict = {"title": self.title, "due_date": self.due_date, "priority": self.priority, "status": self.status}
        return data_dict

    @staticmethod
    def from_dict(dic):
        # extract title, due_date, priority, from the json
        # create new Task(title, due_date, priority)
        # set the status on the Task object
        # return the Task object
        
        title = dic["title"]
        due_date = dic["due_date"]
        priority = dic["priority"]
        status = dic["status"]

        task = Task(title, due_date, priority) #creates the new object
        task.status = status #sets it manually
        
        return task