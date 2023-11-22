import os
import numpy as np
import tkinter as tk
from tkinter import ttk
from QuestManager import QuestManager

def checkbox_state():
    if check_var.get() == 1:
        label.config(text="Checkbox is checked")
    else:
        label.config(text="Checkbox is unchecked")

def process_form(qm):
    title = qname_entry.get()
    text = qtext_entry.get()
    print('Creating quest')
    qm.create_quest(title, text)

def show_q(qm):
    qm.show_quests()

def save_data(ap, xp, lvl):
    data = np.array(ap, xp, lvl)
    np.save('data/account.npy', data)

def calculate_geometry(root, percentage_width):
    screen_height = root.winfo_screenheight()
    screen_width = root.winfo_screenwidth()
    
    window_height = screen_height
    window_width = int(screen_width * (percentage_width / 100))
    
    window_geometry = f"{window_width}x{window_height}+0+0"
    return window_geometry

if __name__ == "__main__":

    ## Load Activity Points, EXP and Level
    ap, xp, lvl = np.load('data/account.npy') if os.path.exists('data/account.npy') else 0, 0, 0

    ## Initialize a QuestManager to keep track of quests
    qm = QuestManager()

    ## Initialize root frame
    root = tk.Tk()
    root.title("Example")

    ## Setting root frame height and width
    percentage_width = 15
    window_geometry = calculate_geometry(root, percentage_width)
    root.geometry(window_geometry)
    ## remove borders and exit button
    #root.overrideredirect(True)

    # Create a variable to store the checkbox state
    check_var = tk.IntVar()

    # Create a checkbox widget
    checkbox = ttk.Checkbutton(root, text="Check me", variable=check_var, command=checkbox_state)
    checkbox.pack()

    # Create a label to display the checkbox state
    label = ttk.Label(root, text="")
    label.pack()


    # Create labels and entry widgets for the form
    qname_label = tk.Label(root, text="Quest title:")
    qname_label.pack()

    qname_entry = tk.Entry(root)
    qname_entry.pack()

    qtext_label = tk.Label(root, text="Quest text:")
    qtext_label.pack()

    qtext_entry = tk.Entry(root)
    qtext_entry.pack()

    submit_button = tk.Button(root, text="Submit", command=lambda: process_form(qm))
    submit_button.pack()

    ## Show quests button
    showq_button = tk.Button(root, text="Show quests", command=lambda: show_q(qm))
    showq_button.pack()


    root.mainloop()