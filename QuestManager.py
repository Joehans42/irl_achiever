import os
import numpy as np
from Quest import Quest

class QuestManager():

    def __init__(self):
        self.directory = 'data'
        self.load_quests()

    def load_quests(self):
        if os.path.isfile('data/quests.npy'):
            self.quests = np.load('data/quests.npy', allow_pickle='TRUE')#.item()
        else:
            self.quests = np.array([])

    def save_quests(self):
        # Check if the directory exists
        if not os.path.exists(self.directory):
            # If it doesn't exist, create it
            os.makedirs(self.directory)

        np.save('data/quests.npy', self.quests, allow_pickle=True)

    def create_quest(self, title, text, type=None, completed=False):
        q = Quest(title, text, type, completed)
        self.quests = np.append(self.quests, q)
        print(f'Quest, {title}, created.')
        print(f'Category: {type}, Text: {text}, Completed: {completed}')
        self.save_quests()

    def show_quests(self):
        print('List of quests:\n')
        for i, q in enumerate(self.quests):
            print(f'Quest {i+1}: {q.title}')