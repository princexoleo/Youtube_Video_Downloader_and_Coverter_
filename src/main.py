from tkinter import *
from tkinter.ttk import *
from pytube import YouTube

'''
Create a class called MainApp,
 contains the main window, and the functions of the buttons, textboxes, etc.

'''
class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Youtube Video Downloader")
        self.master.geometry("500x200")
        self.master.resizable(False, False)
    
        # Defining the widgets
        self.url_label = Label(self.master, text="Enter the URL")
        self.url_entry = Entry(self.master, width=30)
        self.url_button = Button(self.master, text="Download", command=self.download)
        self.url_label.grid(row=0, column=0, padx=10, pady=10)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)
        self.url_button.grid(row=0, column=2, padx=10, pady=10)
    
        self.status_label = Label(self.master, text="Status:")
        self.status_label.grid(row=1, column=0, padx=10, pady=10)
    
        self.status_text = Text(self.master, width=30, height=1)
        self.status_text.grid(row=1, column=1, padx=10, pady=10)
    
        self.progress_label = Label(self.master, text="Progress:")
        self.progress_label.grid(row=2, column=0, padx=10, pady=10)
    
        self.progress_bar = Progressbar(self.master, orient=HORIZONTAL, length=200, mode='determinate')
        self.progress_bar.grid(row=2, column=1, padx=10, pady=10)
    
    def download(self):
        url = self.url_entry.get()
        try:
            yt = YouTube(url)
            self.status_text.delete(1.0, END)
            self.status_text.insert(END, "Downloading...")
            self.progress_bar['value'] = 0
            self.progress_bar.start()
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path='.', filename='video')
            self.status_text.delete(1.0, END)
            self.status_text.insert(END, "Downloaded")
            self.progress_bar['value'] = 100
            self.progress_bar.stop()
        except:
            self.status_text.delete(1.0, END)
            self.status_text.insert(END, "Error")
            self.progress_bar['value'] = 0
            self.progress_bar.stop()
            


if __name__ == "__main__":
    # version of the tkinter
    print(TkVersion)
    root = Tk()
    app = MainApp(root)
    root.mainloop()