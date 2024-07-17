import tkinter as tk
import re

def validate_format():
    value = size_var.get().strip()
    pattern = r'^\d+\s*x\s*\d+$'
    if re.match(pattern, value):
        print("Pattern matched. Doing X.")
        # Replace `print("Pattern matched. Doing X.")` with your desired action X
    else:
        print("Pattern not matched. Doing Y.")
        # Replace `print("Pattern not matched. Doing Y.")` with your desired action Y

root = tk.Tk()
root.title("Regex Test")

size_var = tk.StringVar(value='500x500')  # Provide a default value for StringVar

entry_path = tk.Entry(root, width=50, textvariable=size_var)
entry_path.pack()

button_test = tk.Button(root, text="Test", command=validate_format)
button_test.pack(pady=10)

root.mainloop()
