# import tkinter lib
import tkinter as tk

# create a window GUI
window = tk.Tk()

# change GUI window title
window.title("Tkinter App")

# instancing a label
window = tk.Label(text="Tkinter is cool.", width=80, height=25)
window.pack()
window.mainloop()