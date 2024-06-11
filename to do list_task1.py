import tkinter as tk
from tkinter import messagebox

# Function to add a task to the listbox
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete the selected task from the listbox
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task.")

# Function to clear all tasks from the listbox
def clear_tasks():
    task_listbox.delete(0, tk.END)

# Main application window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x450")
root.config(bg="#ffffff")  # Background color set to white

# Title label
title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="#ffffff", fg="#4682b4")
title_label.pack(pady=10)

# Frame for the task entry and buttons
frame = tk.Frame(root, bg="#ffffff")
frame.pack(pady=10)

# Task entry widget
task_entry = tk.Entry(frame, width=30, font=("Helvetica", 12), bd=2)
task_entry.grid(row=0, column=0, padx=10)

# Add task button
add_button = tk.Button(frame, text="Add Task", command=add_task, font=("Helvetica", 12), bg="#FFD700", fg="#000000", bd=0, padx=10, pady=5)  # Dark yellow color
add_button.grid(row=0, column=1, padx=10)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=45, height=15, font=("Helvetica", 12), bd=2, selectbackground="#add8e6", selectforeground="#000000")
task_listbox.pack(pady=10)

# Frame for the delete and clear buttons
button_frame = tk.Frame(root, bg="#ffffff")
button_frame.pack(pady=10)

# Delete task button
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, font=("Helvetica", 12), bg="#FFD700", fg="#000000", bd=0, padx=10, pady=5)  # Dark yellow color
delete_button.grid(row=0, column=0, padx=10)

# Clear tasks button
clear_button = tk.Button(button_frame, text="Clear Tasks", command=clear_tasks, font=("Helvetica", 12), bg="#FFD700", fg="#000000", bd=0, padx=10, pady=5)  # Dark yellow color
clear_button.grid(row=0, column=1, padx=10)

# Start the main event loop
root.mainloop()
