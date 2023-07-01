import tkinter as tk
from tkinter import filedialog as fd
import pygame
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk


root = tk.Tk()
root.title('MP3 Player')
root.geometry('500x350')

#Initialize Pygame Mixer
pygame.mixer.init()

# Slider Function
def slide(x):
    song = songBox.get(tk.ACTIVE)
    song = f'F:/Python - Tkinter/Sounds/{song}.mp3'

    # Play song with help of Pygame
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=mySlider.get())

def volume(x):
    pygame.mixer.music.set_volume(volumeSlider.get())

    curr_volume = pygame.mixer.music.get_volume()

    volumeFrame.config(text=f"Volume:{int(curr_volume*100)}")

# Grab Song Length
def playTime():
    # Check for Double timing
    if stopped:
        return 
    # Grab Song Elapsed Time
    currentTime = pygame.mixer.music.get_pos() / 1000

    # throw up temp label data
    # sliderLabel.config(text=f"Slider Time = {int(mySlider.get())} and Current Time = {int(currentTime)}")
    # Converted current time in time format
    convertedCurrentTime = time.strftime('%M:%S', time.gmtime(currentTime))

    # Get the song title
    song = songBox.get(tk.ACTIVE)

    # Add path to song name
    song = f'F:/Python - Tkinter/Sounds/{song}.mp3'

    # Get Song Length with Mutagen
    song_mut = MP3(song)
    # Get song Length
    global songLen
    songLen = song_mut.info.length

    # Convert to Time Format
    convertedSongLength = time.strftime('%M:%S', time.gmtime(songLen))
    
    # Increase current time by 1 sec
    currentTime += 1

    if int(mySlider.get()) == int(songLen):
        statusBar.config(text=f' Time Elapsed::{convertedSongLength}/{convertedSongLength}  ')

    elif Paused:
        pass

    elif int(mySlider.get()) == int(currentTime):
        # slider hasn't been moved
        # Update slider To Position
        sliderPos = int(songLen)
        mySlider.config(to=sliderPos, value=int(currentTime))
    

    else:
        # slider has been moved
        # Update slider To Position
        sliderPos = int(songLen)
        mySlider.config(to=sliderPos, value=int(mySlider.get()))

        convertedCurrentTime = time.strftime('%M:%S', time.gmtime(int(mySlider.get())))
        statusBar.config(text=f' Time Elapsed::{convertedCurrentTime}/{convertedSongLength}  ')

        # Move this thing along by one sec
        nextTime = mySlider.get() + 1
        mySlider.config(value=int(nextTime))


    # Output time to status bar
    # statusBar.config(text=f' Time Elapsed::{convertedCurrentTime}/{convertedSongLength}  ')

    # Update slider position value to current song time
    # mySlider.config(value=int(currentTime))

    

    # Play the function after every second
    statusBar.after(1000, playTime)

# Add One Song function
def addOneSong():
    song = fd.askopenfilename(initialdir='Sounds/', title="Choose a Song", filetypes=(("mp3 Files", "*.mp3"),))

    # Strip Out the path from the song name
    song = song.replace("F:/Python - Tkinter/Sounds/", "")
    song = song.replace(".mp3", "")

    # Add Song to ListBox
    songBox.insert(tk.END, song)

# Add Many Songs function
def addManySongs():
    songs = fd.askopenfilenames(initialdir='Sounds/', title="Choose a Song", filetypes=(("mp3 Files", "*.mp3"),))

    for song in songs:
        song = song.replace("F:/Python - Tkinter/Sounds/", "")
        song = song.replace(".mp3", "")
        # Add Song to ListBox
        songBox.insert(tk.END, song)

# Add Delete a Song Function
def delOneSong():
    stop()
    # Delete Currently Selected Song
    songBox.delete(tk.ANCHOR)
    # Stop Music If Playing
    pygame.mixer.music.stop()


# Add Delete Many song Function
def delManySongs():
    stop()
    # Delete All Songs
    songBox.delete(0, tk.END)
    # Stop Music If Playing
    pygame.mixer.music.stop()

# Play Selected Song
def play():

    # Reset slider and Status Bar
    statusBar.config(text="")
    mySlider.config(value=0)

    # Set stop variable to false so that music can play
    global stopped
    stopped = False 
    song = songBox.get(tk.ACTIVE)
    song = f'F:/Python - Tkinter/Sounds/{song}.mp3'

    # Play song with help of Pygame
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Call the song Length function 
    playTime()

    # # Update slider To Position
    # sliderPos = songLen
    # mySlider.config(to=sliderPos, value=0)
# Stop the running song
global stopped
stopped = False
def stop():
    # Reset slider and Status Bar
    statusBar.config(text="")
    mySlider.config(value=0)

    # Stop song from playing
    pygame.mixer.music.stop()
    songBox.selection_clear(tk.ACTIVE)

    # Clear the Status Bar
    statusBar.config(text="")

    # Set Stop Variable to true
    global stopped
    stopped = True

# Play Next Song in Playlist
def nextSong():
    # Reset slider and Status Bar
    statusBar.config(text="")
    mySlider.config(value=0)

    # Get the current song number from songBox
    nextOne = songBox.curselection()
    # Add one to currentSong to get NextSong number
    nextOne = nextOne[0] + 1
    # Get the song title of that NextSong number
    song = songBox.get(nextOne)

    # Add path to song name
    song = f'F:/Python - Tkinter/Sounds/{song}.mp3'

    # Play song with help of Pygame
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Move active bar in playlist
    songBox.selection_clear(0, tk.END)

    # Activate bar to the new song
    songBox.activate(nextOne)

    # Set activate bar to the next song
    songBox.select_set(nextOne, last=None)

# Play Previous Song in Playlist
def previousSong():
    # Reset slider and Status Bar
    statusBar.config(text="")
    mySlider.config(value=0)

    # Get the current song number from songBox
    prevOne = songBox.curselection()
    # Add one to currentSong to get NextSong number
    prevOne = prevOne[0] - 1
    # Get the song title of that NextSong number
    song = songBox.get(prevOne)

    # Add path to song name
    song = f'F:/Python - Tkinter/Sounds/{song}.mp3'

    # Play song with help of Pygame
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Move active bar in playlist
    songBox.selection_clear(0, tk.END)

    # Activate bar to the new song
    songBox.activate(prevOne)

    # Set activate bar to the next song
    songBox.select_set(prevOne, last=None)
# Create Global Pause Variable
global Paused
Paused = False
# Puase and Unpause the current Song
def Pause(is_paused):
    global Paused
    Paused = is_paused

    if Paused:
        # Unpause
        pygame.mixer.music.unpause()
        Paused=False
    else:
        # Pause
        pygame.mixer.music.pause()
        Paused=True

# Create Master Frame
masterFrame = tk.Frame(root)
masterFrame.pack(pady=20)
# Create a Playlist Box
songBox = tk.Listbox(masterFrame, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
songBox.grid(row=0, column=0)
# songBox.bind('<Button-1>', play)

# Define Player control Buttons
backButtonImg = tk.PhotoImage(file="Images/back50.png")
forwardButtonImg = tk.PhotoImage(file="Images/forward50.png")
playButtonImg = tk.PhotoImage(file="Images/play50.png")
pauseButtonImg = tk.PhotoImage(file="Images/pause50.png")
stopButtonImg = tk.PhotoImage(file="Images/stop50.png")

# Create Player Controls Frame
controlFrame = tk.Frame(masterFrame)
controlFrame.grid(row=1, column=0, pady=20)

# Create Volume Label Frame
volumeFrame = tk.LabelFrame(masterFrame, text="Volume:100")
volumeFrame.grid(row=0, column=1, padx=25)

# Create Player Controls Buttons
backButton = tk.Button(controlFrame, image=backButtonImg, borderwidth=0, command=previousSong)
forwardButton = tk.Button(controlFrame, image=forwardButtonImg, borderwidth=0, command=nextSong)
playButton = tk.Button(controlFrame, image=playButtonImg, borderwidth=0, command=play)
pauseButton = tk.Button(controlFrame, image=pauseButtonImg, borderwidth=0, command = lambda: Pause(Paused))
stopButton = tk.Button(controlFrame, image=stopButtonImg, borderwidth=0, command=stop)

backButton.grid(row=0, column=0, padx=10)
stopButton.grid(row=0, column=1, padx=10)
playButton.grid(row=0, column=2, padx=10)
pauseButton.grid(row=0, column=3, padx=10)
forwardButton.grid(row=0, column=4, padx=10)

# Create Menu
myMenu = tk.Menu(root)
root.config(menu=myMenu)

# Add Add Song Menu
addSongMenu = tk.Menu(myMenu)
myMenu.add_cascade(label="Add Songs", menu=addSongMenu)
# Add One Song
addSongMenu.add_command(label="Add One Songs to Play", command=addOneSong)
# Add Many songs
addSongMenu.add_command(label="Add Many Songs", command=addManySongs)

# Add Delete Song Menu
delSongMenu = tk.Menu(myMenu)
myMenu.add_cascade(label="Delete Songs", menu=delSongMenu)
# Delete One Song
delSongMenu.add_command(label="Delete One Song", command=delOneSong)
# Delete Many Songs
delSongMenu.add_command(label="Delete Many Songs", command=delManySongs)

# Create Status Bar
statusBar = tk.Label(root, text="", bd=1, relief=tk.GROOVE, anchor=tk.E)
statusBar.pack(fill=tk.X, side=tk.BOTTOM, ipady=2)

# Create Music Position Slider
mySlider = ttk.Scale(masterFrame, from_=0, to=100, orient=tk.HORIZONTAL, value=0, command=slide, length=360)
mySlider.grid(row=2, column=0, pady=20)


# Create a Volume Slider
volumeSlider = ttk.Scale(volumeFrame, from_=0, to=1, orient=tk.VERTICAL, value=1, command=volume, length=125)
volumeSlider.pack(pady=10)

# Create Temporary Slide Label
# sliderLabel = tk.Label(root, text="0")
# sliderLabel.pack(pady=10)

root.mainloop()