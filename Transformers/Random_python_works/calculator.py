# Import the Tkinter library for creating graphical user interfaces
import tkinter as tk

# Define the function to handle button clicks
def on_click(btn_text):
    # If the button clicked is "=", evaluate the expression in the entry field
    if btn_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    # If the button clicked is "C", clear the entry field
    elif btn_text == "C":
        entry.delete(0, tk.END)
    # For any other button, insert its text into the entry field
    else:
        entry.insert(tk.END, btn_text)

# Create the main Tkinter window and set its title
root = tk.Tk()
root.title("My Simple Calculator - Adeli")

# Create an Entry widget for displaying input and output
entry = tk.Entry(root, width=20)
# Place the Entry widget at the top of the window using the grid geometry manager
entry.grid(row=0, column=0, columnspan=4)

# Define the button configurations as a list of tuples (text, row, column)
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
    ("C", 5, 0)
]

# Loop through the button configurations and create Button widgets
for (text, row, col) in buttons:
    # Create a Button widget with the specified text and on_click function
    button = tk.Button(root, text=text, width=5, height=2, command=lambda btn_text=text: on_click(btn_text))
    # Place the Button widget in the specified row and column using the grid geometry manager
    button.grid(row=row, column=col)

# Start the Tkinter main event loop
root.mainloop()
