# coding: UTF-8
from distutils.cmd import Command
from email.mime import base
import tkinter as tk
from turtle import goto
import webbrowser
import platform
import os
import sys
from tkinter import messagebox
if os.name == 'posix':messagebox.showerror('Attention','Windows以外のOSでの実行は想定されていません。エラーが発生しても自己責任でお願いします。')
if os.name == 'linux':messagebox.showerror('Attention','Windows以外のOSでの実行は想定されていません。エラーが発生しても自己責任でお願いします。')
if os.name == 'darwin':messagebox.showerror('Attention','Windows以外のOSでの実行は想定されていません。エラーが発生しても自己責任でお願いします。')
ur = platform.uname()
print(os.name)
print(ur.system)
print(ur.release)
print(ur.version)
print(ur.processor)

print('WindowsVerShower_V1.0')
print('Developer @wakanameko2')

baseGround = tk.Tk()
baseGround.withdraw()

S = ur.system
R = ur.release
V = ur.version
P = platform.platform()
if os.name == 'nt':messagebox.showinfo('WindowsVerShower', P)