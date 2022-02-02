'''
Project Name: Youtube video downloader
Author:       Mazharul Islam Leon
Created on:   2022-02-02

'''

# Importing libraries
import tkinter as tk
from pytube import YouTube

# Test the tkinter version
# print(tk.TkVersion)

# 2. Creating a window
window = tk.Tk()
window.title("Youtube Video Downloader")
window.geometry("500x500")
window.resizable(0,0)
