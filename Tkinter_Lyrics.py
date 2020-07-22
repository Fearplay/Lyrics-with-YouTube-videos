from tkinter import *
from PyLyrics import *
import pywhatkit
import time

win = Tk()

win.title("Tkinter_Lyric")
win.geometry("360x80")

def search():
    artist = entry_artist.get()
    song = entry_song.get()
    result = PyLyrics.getLyrics(f'{artist}', f'{song}')
    print(result)
    time.sleep(2)
    pywhatkit.playonyt(f"{artist,song}")

label_artist = Label(win, text = "Enter name of artist :",font = ("arial",10,"bold"))
label_artist.grid(row = 1, column = 0, sticky = "W")

entry_artist = Entry(win,font = ("arial",10,"bold"))
entry_artist.grid(row = 1, column = 1)

label_song = Label(win, text = "Enter name of song :",font = ("arial",10,"bold"))
label_song.grid(row = 2, column = 0, sticky = "W")

entry_song = Entry(win,font = ("arial",10,"bold"))
entry_song.grid(row = 2, column = 1)

button = Button(win,text ="START", fg = "black",bg = "white", command = search)
button.grid(row = 3, columnspan = 2)

win.mainloop()
