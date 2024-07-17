import tkinter as tk
from tkinter import ttk
import json
import os

# Function to handle keypress events
def key_pressed(location, event):
    # Construct dictionary with location and event details
    data = {
        "location": location,
        "event": {
            "char": event.char,
        }
    }

    with open('keypress_events.json', 'a') as file:
        json.dump(data, file)
        file.write('\n')

# Setup tkinter window
window = tk.Tk()
window.title('jsonkeylog')
window.geometry('300x200')

# Widgets
title_label = ttk.Label(window, text="Totally not a keylogger", font=("bold, 12"))
title_label.pack()

user_label = ttk.Label(window, text="Username")
pass_label = ttk.Label(window, text="Password")

user_entry = ttk.Entry(window)
pass_entry = ttk.Entry(window, show='*')  # Mask password entry

user_label.pack()
user_entry.pack()
pass_label.pack()
pass_entry.pack()

# Bind keypress events to entries
user_entry.bind('<KeyPress>', lambda event: key_pressed("username", event))
pass_entry.bind('<KeyPress>', lambda event: key_pressed("password", event))

# Run tkinter main loop
window.mainloop()
os.system('cls')

# Read and process the logged events
try:
    with open('keypress_events.json', 'r') as file:
        data = [json.loads(line) for line in file if line.strip()]  # Read each valid JSON line

    # Extract characters from events
    username_events = ""
    password_events = ""
    for entry in data:
        if entry["location"] == "username":
            username_events += entry["event"]["char"]
        if entry["location"] == "password":
            password_events += entry["event"]["char"]

    print("Username:", username_events)
    print("Password:", password_events)

except FileNotFoundError:
    print("No keypress_events.json found.")
except json.JSONDecodeError:
    print("Error decoding JSON from keypress_events.json.")
