import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

text_contents = dict()


def create_file(content="", title="Untitled"):
    container = ttk.Frame(notebook)
    container.pack()

    # Entry field are one-liners, Text are multi-liners
    text_area = tk.Text(container)
    text_area.insert("end", content)
    text_area.pack(side="left", fill="both", expand=True)

    notebook.add(container, text=title)
    notebook.select(container)

    # Hashing is essentially turning a piece of data of arbitrary length into a piece of data of specific length.
    text_contents[str(text_area)] = hash(content)
    # print(str(text_area))

    text_scroll = ttk.Scrollbar(container, orient="vertical", command=text_area.yview)
    text_scroll.pack(side="right", fill="y")
    text_area["yscrollcommand"] = text_scroll.set


def check_for_changes():
    current = get_current_widget()
    content = current.get("1.0", "end-1c")
    name = notebook.tab("current")["text"]

    if hash(content) != text_contents[str(current)]:
        if name[-1] != "*":
            notebook.tab("current", text=name + "*")
    elif name[-1] == "*":
        notebook.tab("current", text_contents=name[:-1])


def get_current_widget():
    tab_widget = root.nametowidget(notebook.select())
    text_widget = tab_widget.winfo_childern()[0]
    return text_widget


def close_current_tab():
    current = get_current_widget()
    if current_tab_unsaved() and not confirm_close():
        return

    if len(notebook.tabs()) == 1:
        create_file()

    notebook.forget(current)


def current_tab_unsaved():
    text_widget = get_current_widget()
    content = text_widget.get("1.0", "end-1c")
    return hash(content) != text_contents[str(text_widget)]


def confirm_close():
    return messagebox.askyesno(
        message="You have unsaved changes. Are you sure you want to quit?",
        icon="question",
        title="Confirm changes"
    )


def confirm_quit():
    # Starts with saying all files currently open are saved, no changes to save.
    unsaved = False

    # cycle through all the tabs, getting the text widget and contents
    for tab in notebook.tabs():
        tab_widget = root.nametowidget(tab)
        text_widget = tab_widget.winfo_childern()[0]
        content = text_widget.get("1.0", "end-1c")

        # and checking it against our text contents dictionary
        if hash(content) != text_contents[str(text_widget)]:
            # if at least one don't match, i.e at-least one file not saved, set unsaved to true and break
            unsaved = True
            break

    # if unsaved is true, ask user to confirm
    if unsaved and not confirm_close():
        return

    root.destroy()


def save_file():
    file_path = filedialog.asksaveasfilename()

    try:
        filename = os.path.basename(file_path)
        # turn name to widget
        text_widget = get_current_widget()
        content = text_widget.get("1.0", "end-1c")
        # "1.0" -> 1 - First line, 0 - Oth char; end-1c: till end except the \n line character

        with open(file_path, "w") as file:
            file.write(content)

    except  (AttributeError, FileNotFoundError):
        print("Save operation cancelled")
        return

    # Rename tab to the name we saved it with.
    notebook.tab('current', text=filename)
    text_contents[str(text_widget)] = hash(content)


def open_file():
    file_path = filedialog.askopenfilename()

    try:
        filename = os.path.basename(file_path)

        with open(file_path, "r") as file:
            content = file.read()

    except (AttributeError, FileNotFoundError):
        print("Open operation cancelled")
        return

    create_file(content, filename)


def show_about_info():
    messagebox.showinfo(
        title="About",
        message="The Peaceful Text Editor is a simple tabbed text editor designed using Tkinter."
    )


root = tk.Tk()
root.title("Peaceful Text Editor")
root.option_add("*tearOff", False)  # prevent tearing off of menu

main = ttk.Frame(root)
main.pack(fill='both', expand=True, padx=1, pady=(4, 0))
# padx : padding on left, right; pady: padding on top and bottom

menubar = tk.Menu()
root.config(menu=menubar)

# add dropdown
file_menu = tk.Menu(menubar)
help_menu = tk.Menu(menubar)

menubar.add_cascade(menu=file_menu, label="File")
menubar.add_cascade(menu=help_menu, label="Help")

file_menu.add_command(label="New", command=create_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open...", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Close Tab", command=close_current_tab, accelerator="Ctrl+Q")
file_menu.add_command(label="Exit", command=confirm_quit)

help_menu.add_command(label="About", command=show_about_info)

notebook = ttk.Notebook(main)
notebook.pack(fill='both', expand=True)
create_file()

root.bind("<KeyPress>", lambda event: check_for_changes())
root.bind("<Control-n>", lambda event: create_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())
root.bind("<Control-q>", lambda event: close_current_tab())

root.mainloop()
