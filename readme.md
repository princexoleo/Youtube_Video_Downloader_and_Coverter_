# Youtube video downloader and converter 

# Project Prerequisites
To implement this project I use the basic concept of `python`, `Tkinter` and `pytube` libraries.
    * Tkinter is a standard GUI library and it is one of the easiest way to build GUI application
    * Pytube used for download the videos from `Youtube`

# Design of the code
The structure of the main code is given below
* import libraries
* Create display window
* Create field to enter link
* Create function to start downloading

# Description of the code

1. Import the libraries:
    Start project by importing the below required modules

    ```
    import tkinter as tk
    from pytube import YouTube
    ```
2. `Tkinter` information
 
    * `TK()` : is used to initialized the tkinter to create a display
    * `geometry` : is used to set the window width and height
    * `resizable` : set the fix size of window.
    * `title` : used to give the tile of the window.
<br>
    ```
    Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
    ```
    * `Label()` widget use to display text that users can’t able to modify.
    * `root` is the name of the window
    * `text` which we display the title of the label
    * `font` in which our text is written
    * `pack` organized widget in block

# Run
To run this project, go to `src` folder and run below command,
```
python main.py
```
it will shows picture like below
![Image](https://github.com/princexoleo/Youtube_Video_Downloader_and_Coverter_/blob/main/img/home.png)
