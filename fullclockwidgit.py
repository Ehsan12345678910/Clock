import time
import tkinter as tk
import ctypes

# ---------------- Clock  ----------------
def tick():
    t = time.time()
    local_time = time.localtime(t)

    date_string = time.strftime("%Y-%m-%d", local_time)
    time_string = time.strftime("%H:%M:%S", local_time)
    milliseconds = int((t - int(t)) * 1000)

    full_string = f"{date_string}\n{time_string}.{milliseconds:03d}"

    clock.config(text=full_string)
    clock.after(1, tick)

# ---------------- Window setup ----------------
root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)
root.configure(bg="#00ffae")
root.geometry("220x100")

# ---------------- Drag ----------------
def start_move(event):
    root.x = event.x
    root.y = event.y

def do_move(event):
    x = event.x_root - root.x
    y = event.y_root - root.y
    root.geometry(f"+{x}+{y}")

root.bind("<Button-1>", start_move)
root.bind("<B1-Motion>", do_move)

# ---------------- Transparency ----------------
def set_opacity(value):
    root.attributes("-alpha", float(value))

opacity_slider = tk.Scale(
    root,
    from_=0.2,
    to=1.0,
    resolution=0.01,
    orient="horizontal",
    command=set_opacity,
    bg="#00ffae",
    highlightthickness=0,
    length=180
)
opacity_slider.set(1.0)
opacity_slider.pack_forget()

# ---------------- Hide (ghost mode) ----------------
hidden = False

def hide_window(event=None):
    global hidden
    hidden = True
    opacity_slider.pack_forget()
    root.geometry("5x5")
    root.attributes("-alpha", 0.2)

def show_window(event=None):
    global hidden
    if hidden:
        root.geometry("220x100")
        root.attributes("-alpha", float(opacity_slider.get()))
        hidden = False

# ---------------- Hover ----------------
def on_enter(event):
    show_window()
    opacity_slider.pack(side="bottom", pady=2)

def on_leave(event):
    if not hidden:
        opacity_slider.pack_forget()

root.bind("<Enter>", on_enter)
root.bind("<Leave>", on_leave)

root.bind("<Double-Button-1>", hide_window)

# ---------------- CLICK-THROUGH ----------------
GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x80000
WS_EX_TRANSPARENT = 0x20

click_through = False

def set_clickthrough(enable):
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    styles = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)

    if enable:
        styles |= WS_EX_LAYERED | WS_EX_TRANSPARENT
    else:
        styles &= ~WS_EX_TRANSPARENT

    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, styles)

def toggle_clickthrough(event=None):
    global click_through
    click_through = not click_through
    set_clickthrough(click_through)

# Right-click to toggle
root.bind("<Button-3>", toggle_clickthrough)

# ---------------- Clock label ----------------
clock = tk.Label(
    root,
    font=("times", 16, "bold"),
    bg="#00ffae",
    fg="black",
)
clock.pack(expand=True, fill="both")

tick()
root.mainloop()