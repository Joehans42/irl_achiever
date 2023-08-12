from datetime import date

class Achievement():

    def __init__(self, id, completed, date, total_criteria, num_fulfilled, category):
        self.completed = completed
        self.id = id
        self.date = date
        self.total_criteria = total_criteria
        self.num_fulfilled = num_fulfilled
        self.category = category

    def update(self, num_increase):
        self.num_fulfilled += num_increase
        if self.num_fulfilled >= self.total_criteria:
            self.complete()

    def complete(self):
        self.completed = True
        self.date = date.today()
        