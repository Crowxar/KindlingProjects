import tkinter as tk
from tkinter import ttk, scrolledtext
import os

#region ===Functions===


#endregion

#region ===Setup===
window = tk.Tk()
window.title('sliders_test')


#endregion

#region ===Widgets===
scale_float = tk.DoubleVar(value=15)
scale = ttk.Scale(
    window,
    command = lambda value: progress.stop(),
    from_=0,
    to = 25,
    length = 300,
    orient = 'horizontal',
    variable= scale_float,
    )
scale.pack()

progress = ttk.Progressbar(
    window,
    variable=scale_float,
    maximum=25,
    orient='horizontal',
    mode='indeterminate',
    length=400,
    )
progress.pack()

# progress.start(1000)
scrolledtext = scrolledtext.ScrolledText(
    window,
    width=100,
    height=5,
    )
scrolledtext.pack()


exercise_int = tk.IntVar()
exercise_progress = ttk.Progressbar(
    window,
    orient='vertical',
    variable=exercise_int
)
exercise_progress.pack()
exercise_progress.start()

label = ttk.Label(
    window,
    textvariable=exercise_int
    )
label.pack()

exercise_scale = ttk.Scale(
    window,
    variable=exercise_int,
    from_=0,
    to=100,
    )
exercise_scale.pack()
#endregion

#region ===Run===
window.focus_force()
window.wm_attributes('-topmost', 1)
window.mainloop()
os.system('cls')
#endregion
