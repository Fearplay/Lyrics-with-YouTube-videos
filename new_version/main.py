from tkinter import Label, Tk, Entry, Button, Text, Scrollbar, Checkbutton, BooleanVar
from bs4 import BeautifulSoup
import requests
import pywhatkit

LABEL_FONT = ("arial", 15, "bold")
ENTRY_FONT = ("arial", 15)

main_window = Tk()
is_featured_artist_checked = BooleanVar()


def get_lyrics_url():
    """Play YouTube video and returns the url based on if the featured artist checkbox is checked or not"""
    artist = str(artist_entry.get()).lower().replace(" ", "-")
    song = str(song_entry.get()).lower().replace(" ", "-")
    feature = str(featured_artist_entry.get()).lower().replace(" ", "-")
    pywhatkit.playonyt(f"{artist, song}")
    if has_featured_artist():
        url = f"https://www.songlyrics.com/{artist}-feat-{feature}/{song}-lyrics/"

    else:
        url = f"https://www.songlyrics.com/{artist}/{song}-lyrics/"

    return url


def get_song_lyrics():
    """Returns the lyrics of the song"""
    response = requests.get(get_lyrics_url())

    soup = BeautifulSoup(response.text, 'html.parser')

    lyrics_div = soup.find('p', id="songLyricsDiv")

    lyrics = lyrics_div.text

    return lyrics


def display_lyrics_window():
    """Shows window with lyrics and scrollbar"""
    lyrics_window = Tk()
    lyrics_window.title("Lyrics")

    lyrics = get_song_lyrics()

    lyrics_window.focus_force()
    lyrics_window.title("Lyrics")

    text = Text(lyrics_window, wrap="word", font=("Helvetica", 15))
    scrollbar = Scrollbar(lyrics_window, command=text.yview)
    text.configure(yscrollcommand=scrollbar.set)

    text.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    text.insert("1.0", lyrics)

    lyrics_window.eval('tk::PlaceWindow . center')
    main_window.destroy()
    lyrics_window.mainloop()


def has_featured_artist():
    """Determines if the featured artist box is checked and if the entry box is filled in"""
    if is_featured_artist_checked.get() and len(featured_artist_entry.get()) != 0:
        return True
    return False


def toggle_featured_artist_entry():
    """Shows the featured artist entry if the checkbox is checked. Otherwise, it removes"""
    if is_featured_artist_checked.get():
        featured_artist_label.grid(row=5, column=0, sticky="W")
        featured_artist_entry.grid(row=5, column=1)
    else:
        featured_artist_label.grid_remove()
        featured_artist_entry.grid_remove()


def configure_gui_layout():
    """Grids of labels, entries, buttons and checkboxes"""
    artist_label.grid(row=1, column=0, sticky="W")
    artist_entry.grid(row=1, column=1)
    song_label.grid(row=2, column=0, sticky="W")
    song_entry.grid(row=2, column=1)
    search_button.grid(row=3, columnspan=2)
    featured_artist_check_button.grid(row=4, columnspan=2)


if __name__ == "__main__":
    """Starts main when you can enter the name of the song where you want to see their lyrics"""
    main_window.title("Search")
    main_window.resizable(False, False)

    artist_label = Label(main_window, text="Enter the name of the artist :", font=LABEL_FONT)
    song_label = Label(main_window, text="Enter the name of the song :", font=LABEL_FONT)
    featured_artist_label = Label(main_window, text="Enter the name of the artist :", font=LABEL_FONT)

    artist_entry = Entry(main_window, font=ENTRY_FONT)
    song_entry = Entry(main_window, font=ENTRY_FONT)
    featured_artist_entry = Entry(main_window, font=ENTRY_FONT)

    search_button = Button(main_window, text="SEARCH", fg="black", bg="white", command=display_lyrics_window)

    featured_artist_check_button = Checkbutton(main_window,
                                               text="Featured artist",
                                               font=LABEL_FONT,
                                               command=toggle_featured_artist_entry,
                                               variable=is_featured_artist_checked,
                                               offvalue=0,
                                               onvalue=1)

    configure_gui_layout()
    main_window.eval('tk::PlaceWindow . center')
    main_window.mainloop()
