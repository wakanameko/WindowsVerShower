# coding: UTF-8
import tkinter as tk
import platform
from tkinter import messagebox
print('WindowsVerShower_V1.3\nDeveloper @wakanameko2')
baseGround = tk.Tk()
baseGround.withdraw()
if not platform.system() == 'Windows':messagebox.showerror('Attention','Windows以外のOSでの実行は想定されていません。エラーが発生しても自己責任でお願いします。')
if platform.system() == 'Windows':messagebox.showinfo('WindowsVerShower', platform.platform())