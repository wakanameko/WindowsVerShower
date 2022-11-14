# coding: UTF-8
import tkinter as tk
import platform
import os
from tkinter import messagebox
if os.name == 'posix':messagebox.showerror('Attention','Windows以外のOSでの実行は想定されていません。エラーが発生しても自己責任でお願いします。')
if os.name == 'linux':messagebox.showerror('Attention','Windows以外のOSでの実行は想定されていません。エラーが発生しても自己責任でお願いします。')
if os.name == 'darwin':messagebox.showerror('Attention','Windows以外のOSでの実行は想定されていません。エラーが発生しても自己責任でお願いします。')

print('WindowsVerShower_V1.0')
print('Developer @wakanameko2')

baseGround = tk.Tk()
baseGround.withdraw()

if os.name == 'nt':messagebox.showinfo('WindowsVerShower', platform.platform())