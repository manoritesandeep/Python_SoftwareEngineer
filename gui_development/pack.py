import tkinter as tk

root = tk.Tk()

tk.Label(root, text="Label left", bg="green").pack(side="left", fill="both", expand=True)
tk.Label(root, text="Label left2", bg="pink").pack(side="left", fill="both", expand=False)
tk.Label(root, text="Label Right", bg="yellow").pack(side="right", fill="both", expand=True)
tk.Label(root, text="Label Top1", bg="red").pack(side="top", fill="both", expand=True)
tk.Label(root, text="Label Top2", bg="blue").pack(side="top", fill="both", expand=True)

root.mainloop()