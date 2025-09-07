import tkinter as tk
import psutil


def stats():
    cpu_usage =psutil.cpu_percent(interval=0)
    ram_usage = psutil.virtual_memory().percent

    cpu_label.config(text=f"CPU: {cpu_usage}%")
    ram_label.config(text=f"RAM:{ram_usage}%")
    root.after(1000,stats)



def start_drag(event):
    root.x = event.x
    root.y =event.y

def do_drag(event):
    x= root.winfo_pointerx()-root.x
    y= root.winfo_pointery()-root.y
    root.geometry(f"+{x}+{y}")

def close(event):
    root.destroy()



root = tk.Tk()
root.overrideredirect(True)

root.geometry("170x200+100+100")
root.resizable(False,False)


handle = tk.Label(root, text="Performance", bg="grey", fg="white")  # small grip
handle.pack(fill="x", ipady=5)

root.configure(bg="black")
root.wm_attributes("-transparentcolor","black")

cpu_label =  tk.Label(root,text="CPU: --%" ,font=("Arial",14),fg="white", bg="black")
cpu_label.pack(pady=5)

ram_label = tk.Label(root, text="RAM: --%", font=("Arial",14),fg="white", bg="black")
ram_label.pack(pady=5)


handle.bind("<Button-1>",start_drag)
handle.bind("<B1-Motion>", do_drag)
root.bind("<Button-3>", close)

stats()
root.mainloop()