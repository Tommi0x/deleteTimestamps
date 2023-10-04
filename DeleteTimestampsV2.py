import os
import re
import tkinter as tk
from tkinter import ttk,filedialog

def remove_timestamps(text):
    # Regular expression pattern to match timestamps in the format hh:mm
    pattern = r'\b\d{1,2}:\d{2}\b'
    # Use re.sub() to replace matched timestamps with an empty string
    result = re.sub(pattern, '', text)
    return result

def remove_empty_lines(text):
    # Remove empty lines using regex
    cleaned_text = re.sub(r'\n\s*\n', '\n', text)
    return cleaned_text.strip()  # Strip leading/trailing whitespace

selected_file_path = ""

def select_file():
    global selected_file_path
    selected_file_path = filedialog.askopenfilename()
    if selected_file_path:
        # Extract the file name from the path
        file_name = os.path.basename(selected_file_path)
        # Update the label text with the selected file name
        file_path_label.config(text="Selected file: " + file_name)

def save_file():
    global selected_file_path
    if selected_file_path:
        # Create a save file dialog
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if save_path:
            with open(selected_file_path, 'r') as file:
                text = remove_empty_lines(remove_timestamps(file.read()))
            with open(save_path, 'w') as file:
                file.write(text)
            # Update the label text after saving the file
            file_path_label.config(text="Done😁!")

# Create a Tkinter root window
root = tk.Tk()
root.title("DeleteTimestamps")
root.geometry('300x200')
root.resizable(False, False)
root.configure(bg="#FFC0CB")
button_style = ttk.Style()
button_style.configure('TButton', font=('Arial', 14, 'bold'), background='#FF69B4')

# Create a button for selecting a file
select_button = tk.Button(root, text="Select File", command=select_file)
select_button.pack(pady=20)  # Add some padding around the button

# Create a button for saving a file
save_button = tk.Button(root, text="Save File", command=save_file)
save_button.pack(pady=20)  # Add some padding around the button

# Set pink background for the label and make it invisible by setting borderwidth and highlightthickness
file_path_label = tk.Label(root, text="", bg="#FFC0CB", fg="black")
file_path_label.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()