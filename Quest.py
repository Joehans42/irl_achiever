class Quest():

    '''
    text -> quest text
    type -> regular quest, daily, weekly
    '''
    def __init__(self, text, type, completed):
        self.text = text
        self.type = type
        self.completed = completed

    def complete(self):
        self.completed = True
