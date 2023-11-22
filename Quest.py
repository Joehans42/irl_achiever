class Quest():

    '''
    text -> quest text
    type -> regular quest, daily, weekly
    '''
    def __init__(self, title, text, type, completed):
        self.title = title
        self.text = text
        self.type = type
        self.completed = completed
        self.streak = 0

    def complete(self):
        self.completed = True
