from tkinter import *


def create_title_label(root, text=""):
    font = ('Tahoma', '12', 'bold')
    return Label(root, text=text, width=47, height=2, bg='#00939A', fg='white', font=font)


def create_subtitle_label(root, text=""):
    font = ('Tahoma', '10', 'bold')
    return Label(root, text=text, width=30, bg='white', fg='#00939A',
                 justify=LEFT, anchor='w', padx=10, font=font)


def create_app_version_label(root, text=""):
    font = ('Tahoma', '9')
    return Label(root, text=text, font=font, bg='white', fg='#6F787B', justify=RIGHT, anchor='e')
