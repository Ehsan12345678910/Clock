import sys
from tkinter import *
import time

def tick():
    # Full timestamp with milliseconds
    t = time.time()
    local_time = time.localtime(t)

    date_string = time.strftime("%Y-%m-%d", local_time)
    time_string = time.strftime("%H:%M:%S", local_time)

    milliseconds = int((t - int(t)) * 1000)

    full_string = f"{date_string}\n{time_string}.{milliseconds:03d}"

    clock.config(text=full_string)

    # Update faster for smooth milliseconds
    clock.after(1, tick)

root = Tk()
root.title("Clock")

clock = Label(root,
              font=("times", 80, "bold"),
              bg="#00ffae",
              fg="black",
              justify="center")
clock.grid(row=0, column=0)

tick()
root.mainloop()