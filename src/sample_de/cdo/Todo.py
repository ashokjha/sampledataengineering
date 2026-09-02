

class Todo:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False
        

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Title: {self.title}, Description: {self.description}, Status: {status}"