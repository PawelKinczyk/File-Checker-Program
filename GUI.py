import tkinter as tk
from PIL import ImageTk, Image
from FUNCTION import check_files
from tkinter import filedialog as fd
import webbrowser
import os as os
import sys

dir = os.path.dirname(__file__)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def browse_button_folder():

    global folder_path
    filename = fd.askdirectory()
    folder_path.set(filename)


def browse_button_file():

    global file_path
    filename = fd.askopenfilename(filetypes=(
        ("excel file", "*.xlsx"), ("All files", "*.*"),))
    file_path.set(filename)


def web_open_button():
    webbrowser.open_new("https://produktywnyprojektant.com/en/about-me/")


def instruction_open_button():
    webbrowser.open_new("https://github.com/PawelKinczyk/File-Checker-Program")


def bug_report_button():
    webbrowser.open_new("https://github.com/PawelKinczyk/File-Checker-Program/issues")

root = tk.Tk()
root.title("File Checker")
root.maxsize(900,  600)
icon_path = resource_path("assets\icon.ico")
root.wm_iconbitmap(icon_path)
root.resizable(False, True)


left_frame = tk.Frame(root,  width=200,  height=400,
                      bg='#d3d3db', relief="groove", borderwidth=6)
left_frame.grid(row=0,  column=0,  padx=10,  pady=5)

right_frame = tk.Frame(root,  width=300,  height=400,
                       bg='#d3d3db', relief="groove", borderwidth=6)
right_frame.grid(row=0,  column=1,  padx=10,  pady=5)

# Left
logo_path = resource_path("assets\Image_Logo.png")
logo = Image.open(logo_path)
logo = logo.resize((200, 240))
logo = ImageTk.PhotoImage(logo)

label_logo = tk.Label(master=left_frame, image=logo)
label_logo_text = tk.Label(
    master=left_frame, text="Created by Paweł Kińczyk (c)", wraplength=300, justify="center")

button_web = tk.Button(left_frame, text="My blog",
                       command=lambda: web_open_button(), bg="gray")
button_instr = tk.Button(left_frame, text="Instruction",
                         command=lambda: instruction_open_button(), bg="gray")
button_bug = tk.Button(left_frame, text="Bug report",
                       command=lambda: bug_report_button(), bg="gray")

label_logo.grid(row=0, column=0, padx=10, pady=20)
label_logo_text.grid(row=1, column=0, padx=10, pady=20)
button_web.grid(row=2,  column=0,  padx=5,  pady=5)
button_instr.grid(row=3,  column=0,  padx=5,  pady=5)
button_bug.grid(row=4,  column=0,  padx=5,  pady=5)

# Right
right_frame1 = tk.Frame(right_frame,  width=300,  height=120,  bg='#091839')
right_frame1.grid(row=0,  column=0,  padx=10,  pady=15)
right_frame1.grid_propagate(0)

right_frame2 = tk.Frame(right_frame,  width=300,  height=120,  bg='#091839')
right_frame2.grid(row=1,  column=0,  padx=10,  pady=5)
right_frame2.grid_propagate(0)

right_frame3 = tk.Frame(right_frame,  width=300,  height=50,  bg='#091839')
right_frame3.grid(row=2,  column=0,  padx=10,  pady=5)
right_frame3.grid_propagate(0)

right_frame4 = tk.Frame(right_frame,  width=300,  height=110,  bg='#091839')
right_frame4.grid(row=3,  column=0,  padx=10,  pady=5)
right_frame4.grid_propagate(0)

# Right1
label_path = tk.Label(
    right_frame1, text="Pick path to folder in which you want to check files")
folder_path = tk.StringVar()
folder_path.set("***No folder Path***")
label_path_picked = tk.Label(
    right_frame1, wraplength=300, textvariable=folder_path)
button_path = tk.Button(right_frame1, text="Browse",
                        command=browse_button_folder, relief="raised", bg="gray")

label_path.grid(row=0,  column=0,  padx=5,  pady=5)
label_path_picked.grid(row=1,  column=0,  padx=5,  pady=5)
button_path.grid(row=2,  column=0,  padx=5,  pady=5)
right_frame1.grid_columnconfigure(0, weight=1)  # center all in window


# Right2
label_excel = tk.Label(master=right_frame2,
                       text="Insert excel path which you want to check")
file_path = tk.StringVar()
file_path.set("***No file Path***")
label_file_picked = tk.Label(
    master=right_frame2, wraplength=300, textvariable=file_path)
button_file = tk.Button(master=right_frame2, text="Browse",
                        command=browse_button_file, bg="gray")

label_excel.grid(row=0,  column=0,  padx=5,  pady=5)
label_file_picked.grid(row=1,  column=0,  padx=5,  pady=5)
button_file.grid(row=2,  column=0,  padx=5,  pady=5)
right_frame2.grid_columnconfigure(0, weight=1)

# Right3
file_extension = tk.BooleanVar()
file_extension_check = tk.Checkbutton(right_frame3, text="Check file extension", variable=file_extension,
                                      onvalue=True, offvalue=False, height=1, width=14)
button_run = tk.Button(master=right_frame3, text="Run program", command=lambda: check_files(
    str(folder_path.get()), str(file_path.get()), status_var, file_extension.get()), bg="gray")

button_run.grid(row=0,  column=0,  padx=5,  pady=5)
file_extension_check.grid(row=0,  column=1,  padx=2,  pady=2)
right_frame3.grid_columnconfigure(0, weight=1)
right_frame3.grid_rowconfigure(0, weight=1)

# Right4
status_var = tk.StringVar()
status_var.set("***Status***")
status_var_label = tk.Label(
    master=right_frame4, wraplength=300, textvariable=status_var)

status_var_label.grid(row=0,  column=0,  padx=5,  pady=5)
right_frame4.grid_columnconfigure(0, weight=1)
right_frame4.grid_rowconfigure(0, weight=1)

root.mainloop()
