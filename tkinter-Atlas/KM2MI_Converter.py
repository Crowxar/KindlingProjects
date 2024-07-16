import tkinter as tk
from tkinter import ttk

def convert():
    selected_value = conversion.get()
    dist_input = entry_Int.get()
    if selected_value == "miles_to_km":
        output = dist_input * 1.61
        output_string.set(f"{output:.2f} km")
    else:
        output = dist_input / 1.61
        output_string.set(f"{output:.2f} mi")

# Window Attributes
window = tk.Tk()
window.title("Demo")
window.geometry("+480+270")
window.resizable(False, False)

# Title Attributes and Pack
title_label = ttk.Label(
    master=window, text="Miles to Kilometers", font="Calibri 24 bold"
)
title_label.pack(padx=10)

# input field
input_frame = ttk.Frame(master=window)
entry_Int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_Int)
button = ttk.Button(master=input_frame, text="Convert", command=convert)

input_frame.pack(pady=10)
entry.pack(side="left", padx=10)
button.pack(side="left")

# Radio Button
selection_frame = ttk.Frame(window)
selection_frame.pack()

conversion = tk.StringVar(value="km_to_miles")
km_to_miles = ttk.Radiobutton(
    selection_frame, text="km to miles", variable=conversion, value="km_to_miles"
)
miles_to_km = ttk.Radiobutton(
    selection_frame, text="miles to km", variable=conversion, value="miles_to_km"
)
km_to_miles.pack(side="left")
miles_to_km.pack(side="left")

# Output Label
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window, text=output_string, font="Calibri 24", textvariable=output_string
)
output_label.pack(pady=10, expand=True)

window.mainloop()
