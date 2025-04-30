import tkinter as tk
from tkinter import messagebox

# List to store tasks
tasks = []

def add_task():
    """Adds a task to the list and updates the display."""
    task = task_entry.get()
    if task:
        tasks.append(task)  # Add task to list
        task_entry.delete(0, tk.END)  # Clear entry field
        update_task_list()  # Refresh the displayed task list
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")

def update_task_list():
    """Refreshes the task list in the Listbox."""
    task_list.delete(0, tk.END)  # Clear the current list
    for task in tasks:
        task_list.insert(tk.END, task)  # Insert tasks from the list

def remove_task():
    """Removes the selected task from the list."""
    selected_task_index = task_list.curselection()  # Get selected item index
    if selected_task_index:
        task_list.delete(selected_task_index)  # Remove from Listbox
        tasks.pop(selected_task_index[0])  # Remove from tasks list
    else:
        messagebox.showwarning("Warning", "Please select a task to remove")

# Creating the main application window
app = tk.Tk()
app.title("To-Do List")

# Entry field for tasks
task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=10)

# Buttons to add and remove tasks
add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(app, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

# Listbox to display tasks
task_list = tk.Listbox(app, width=40, height=10)
task_list.pack(pady=10)

# Run the Tkinter event loop
app.mainloop()
