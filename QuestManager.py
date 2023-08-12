import numpy as np

class QuestManager():

    def __init__(self):
        self.get_quests()

    def load_quests(self):
        self.quests = np.load('data/quests.npy', allow_pickle='TRUE').item()
        pass

    def save_quests(self):
        pass

    def create_quest(self):
        pass