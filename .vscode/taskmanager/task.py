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
        self.status = "Pending"  # always Pending on creation

    def mark_done(self):
        pass

    def set_due_date(self, new_due_date):
        pass

    def set_title(self, new_title):
        pass

    def set_priority(self, new_priority):
        pass

    def to_dict(self):
        pass

    @staticmethod
    def from_dict(data_dict):
        pass
