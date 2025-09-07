import tkinter as tk
import GPUtil





def show_gpu():
    try:
        gpus = GPUtil.getGPUs()

        if gpus:
            gpu=gpus[0]
            gpu_load= f"{gpu.load*100: .1f}%"
            v_ram=f"{gpu.memoryUsed}/{gpu.memoryTotal} MB"

            gpu_label.config(text=f"GPU : {gpu_load}")
            gpu_label2.config(text=f'VRAM : {v_ram}')
            root.after(1000,stats)
        else:
            return "N/A"


    except Exception:
        return "N/A"


def start_drag(event):
    root.x = event.x
    root.y =event.y

def do_drag(event):
    x= root.winfo_pointerx()-root.x
    y= root.winfo_pointery()-root.y
    root.geometry(f"+{x}+{y}")

def close(event):
    root.destroy()

root=tk.Tk()
root.overrideredirect(True)

root.configure(bg="black")
root.wm_attributes("-transparentcolor","black")
root.geometry("170x150+100+100")
root.resizable(False, False)

handle = tk.Label(root, text="GPU", bg="grey", fg="white")  # small grip
handle.pack(fill="x", ipady=5)

gpu_label= tk.Label(root, font=("Arial",12), fg="white", bg="black")
gpu_label.pack(pady=5)

gpu_label2 = tk.Label(root, font=("Arial",12), fg="white", bg="black")
gpu_label2.pack(pady=5)


handle.bind("<Button-1>",start_drag)
handle.bind("<B1-Motion>", do_drag)
root.bind("<Button-3>", close)

show_gpu()
root.mainloop()

