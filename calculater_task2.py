import tkinter as tk
from math import sqrt, cos, tan, sin

# Function to update the display
def update_display(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + value)

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Function to delete the last character in the display
def delete_last():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current[:-1])

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Function to handle special operations
def special_operation(op):
    try:
        if op == "√":
            result = sqrt(float(display.get()))
        elif op == "Cos":
            result = cos(float(display.get()))
        elif op == "Tan":
            result = tan(float(display.get()))
        elif op == "Sin":
            result = sin(float(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Main application window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x500")
root.resizable(0, 0)
root.config(bg="#e0ffff")

# Display
display = tk.Entry(root, font=("Helvetica", 20), borderwidth=5, relief="sunken", justify='right', bg="#C0D9D9")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons configuration
buttons = [
    ('←', 1, 0), ('C', 1, 1), ('CE', 1, 2), ('±', 1, 3),
    ('√', 2, 0), ('Cos', 2, 1), ('Tan', 2, 2), ('Sin', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('+', 3, 3),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
    ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('*', 5, 3),
    ('0', 6, 0), ('.', 6, 1), ('=', 6, 2), ('/', 6, 3)
]

button_colors = {
    "default": "#87AFC7",  # Blue
    "operations": "#728FCE",  # Light Blue
    "clear": "#FF6347",  # Tomato
    "equal": "#C0D9D9"  # Light Cyan
}

for (text, row, col) in buttons:
    if text == "=":
        color = button_colors["equal"]
        action = evaluate
    elif text in {"C", "CE", "←"}:
        color = button_colors["clear"]
        action = clear_display if text == "C" else (delete_last if text == "←" else clear_display)
    elif text in {"√", "Cos", "Tan", "Sin"}:
        color = button_colors["operations"]
        action = lambda t=text: special_operation(t)
    else:
        color = button_colors["default"]
        action = lambda t=text: update_display(t)
    
    button = tk.Button(root, text=text, command=action, font=("Helvetica", 14), bg=color, fg="#000000", width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)

# Start the main event loop
root.mainloop()
