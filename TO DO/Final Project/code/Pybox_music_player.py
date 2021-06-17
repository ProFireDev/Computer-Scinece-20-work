#importing modules
import os
import pickle
import tkinter as tk
from tkinter import  filedialog
from tkinter import PhotoImage
from pygame import mixer

# Defining the player class

class Player(tk.Frame):
	 # Defining Constructor
	def __init__(self, master=None):
		super().__init__(master) #initing everything the class
		self.master = master
		self.pack()
		mixer.init()

		if os.path.exists('songs.pickle'):
			with open('songs.pickle', 'rb') as f:
				self.playlist = pickle.load(f)
		else:
			self.playlist=[] #create the empty array to add the songs to -
			#only done if no path or no songs (so you have to add songs again)

		# sets some global values

		self.current = 0
		self.paused = True # makes it so the play eer plays nothing by defult
		self.played = False # sets the play value to false, to make sure that no sound is playing

		#calling all of the functions and UI componetents
		self.create_frames()
		self.track_widgets()
		self.control_widgets()
		self.tracklist_widgets()

		#creates the basic frame of the application

	def create_frames(self):
		#frame for the "main" ui comp, where the album covers show up
		self.track = tk.LabelFrame(self, text='Now playing', #lable for the now playing title
					font=("Frutiger",15,"bold"), #font, font type and size
					bg="#EE3EC9",fg="#4C0BD1",bd=5,relief=tk.GROOVE) #setting the background and forground colors 
					# bg = the pink outline and fg = the text color
		self.track.config(width=200,height=300)
		self.track.grid(row=0, column=0, padx=10) #sets the location in the application

		self.tracklist = tk.LabelFrame(self, text=f'PlayList - {str(len(self.playlist))} Songs', #the sting here gets the lenth of the song
							font=("Frutiger",13,"bold"),
							bg="#FF39AA",fg="#4C0BD1",bd=5,relief=tk.GROOVE) #mmore font and colourartion stuff
		self.tracklist.config(width=790,height=200) #thease values dont matter too much
		self.tracklist.grid(row=0, column=1, rowspan=4, pady=2)

		self.controls = tk.LabelFrame(self,
							font=("Frutiger",15,"bold"),
							bg="#121640",fg="#121640",bd=2,relief=tk.GROOVE)
		self.controls.config(width=410,height=80)
		self.controls.grid(row=2, column=0, pady=5, padx=10)

		#not really any error handeling needed here, as its so bare bones nothing can go wrong


####################################################################################################
#                                FUNCTIONS
####################################################################################################


# handels the track widget ( the pink box in the center)

	def track_widgets(self):
		self.canvas = tk.Label(self.track, image=img)
		self.canvas.configure(width=392, height=240) #configures the size of the pink box
		self.canvas.configure(bg='#4C0BD1') #configures the colour
		self.canvas.grid(row=0,column=0)

		self.songtrack = tk.Label(self.track, font=("Frutiger",16,"bold"),
						bg="#121642",fg="#00C4CC")
		self.songtrack['text'] = 'Press Load to start' #defult text when theres no track to play
		self.songtrack.config(width=30, height=1)
		self.songtrack.grid(row=1,column=0,padx=10)



# handels the track controls 

	def control_widgets(self): #             back ground color  #text color
		self.loadSongs = tk.Button(self.controls, bg='#00C4CC', fg='#121640', font=10)
		self.loadSongs['text'] = 'Load Songs' #load songs button
		self.loadSongs['command'] = self.get_songs #calls retreive songs to load in songs
		self.loadSongs.grid(row=0, column=0, padx=10)

		self.prev = tk.Button(self.controls, image=prev) #previous track button
		self.prev['command'] = self.prev_song #skips back a song
		self.prev.grid(row=0, column=1)
		self.configure(bg='#121640') #color for the button

		self.pause = tk.Button(self.controls, image=pause) #pause button
		self.pause['command'] = self.pause_song #stops song from playing
		self.pause.grid(row=0, column=2)

		self.next = tk.Button(self.controls, image=next_)
		self.next['command'] = self.next_song #skip song button
		self.next.grid(row=0, column=3)

		self.volume = tk.DoubleVar(self)
		#sets up the slider for volume
		self.slider = tk.Scale(self.controls, from_ = 0, to = 10, orient = tk.HORIZONTAL)
		self.slider.configure(bg='#FF39AA') #sets colour of the slider
		self.slider['variable'] = self.volume #sets volume of the slider baised on position
		self.slider.set(0.7) # max is 1, 0.7 is the defult positon so your ears dont die
		mixer.music.set_volume(7) # sets the corosponding defult level on the slider
		self.slider['command'] = self.change_volume #changes the volume
		self.slider.grid(row=0, column=4, padx=7)


# for the track list on the right

	def tracklist_widgets(self):
		self.scrollbar = tk.Scrollbar(self.tracklist, orient=tk.VERTICAL) #sets up the white scroll bar
		self.scrollbar.grid(row=0,column=1, rowspan=5, sticky='ns') # sets it to be locked to the right side of the screen
		self.scrollbar.configure(bg='purple') # value does not matter, this line does not get used

#this is the actual list for the tracks
		self.list = tk.Listbox(self.tracklist, selectmode=tk.SINGLE, # the list boxs sets up a list
					 yscrollcommand=self.scrollbar.set, selectbackground='sky blue') # sets the color of the track you have selected inside of the list
		self.add_songs() # makes call to the funcion below
		self.list.config(height=23) # sets the number of items on the list in one "page"
		self.list.bind('<Double-1>', self.play_song) #calls the function to play a song when you double click on it

		self.scrollbar.config(command=self.list.yview) # changes pos so you can scroll up and down the list
		self.list.grid(row=0, column=0, rowspan=5)



#the function to do the actual getting of the songs

	def get_songs(self):
		self.songlist = [] #empty array to put songs in
		directory = filedialog.askdirectory() #opens up a diolage to choose a folder of songs - to create a playlist you just need to have all the songs you want in one folder
		for root_, dirs, files in os.walk(directory):
				for file in files:
					if os.path.splitext(file)[1] == '.mp3': #splits the file name away to check if it ends in a .mp3 and if we can play it or not
						path = (root_ + '/' + file).replace('\\','/') #do some shuffleing around to remove parts of the file parth
						#the main goal here though is to get the root of the files location
						self.songlist.append(path) #appends the file path to the file, so we can find the file we are playing and its location
						#pickles great for helping data flow

		with open('songs.pickle', 'wb') as f:
			#dumps the contents of the file indexed into the song list
			pickle.dump(self.songlist, f) #dumnps out a list of .mp3 files
		self.playlist = self.songlist #setting thease values to be the same
		self.tracklist['text'] = f'PlayList - {str(len(self.playlist))}' # lables it and appends the number of tracks to it
		self.list.delete(0, tk.END) 
		self.add_songs() #calls the enumerate function to add the songs to the list


# funcrtion to add the songs to the list

	def add_songs(self):
		for index, song in enumerate(self.playlist):
			#gets the songs in a playlist (folder) then inserts them
			self.list.insert(index, os.path.basename(song)) #this is also part of how the total number of tracks in the playlist are counted


# play songs for the play song button

	def play_song(self, event=None):
		if event is not None:
			self.current = self.list.curselection()[0]
			for i in range(len(self.playlist)):
				self.list.itemconfigure(i, bg="#00C4CC")

		print(self.playlist[self.current]) #logs the track being played to the console
		#for intenal debugging
		mixer.music.load(self.playlist[self.current]) #Loads the currently selcected track from the list
		self.songtrack['anchor'] = 'w' # positions text to the west side 
		self.songtrack['text'] = os.path.basename(self.playlist[self.current]) #gets text for the name of the track
		# gets the path of the file and where it is, the name of the file aswell.

		self.pause['image'] = play #sitchs the image, before resuming plahying
		self.paused = False
		self.played = True #thease 2 values swap for each to make sure nothing weird happens
		self.list.activate(self.current) #plays the item thats currently indexed
		self.list.itemconfigure(self.current, bg='#00C4CC') #configures the button on the canavas

		mixer.music.play() #play function from mixer



# pause the song

	def pause_song(self):
		if not self.paused: #if its not paused, make it paused
			self.paused = True
			mixer.music.pause() #stops the current track from playing
			self.pause['image'] = pause #changes the image on the button over
		else: 
			if self.played == False: #if the song is playing, then dont pause it
				self.play_song()
			self.paused = False
			mixer.music.unpause() #unpauses the song
			self.pause['image'] = play #changes the icon back to the play icon



# previous song

	def prev_song(self):
		if self.current > 0: #gets current song
			self.current -= 1 #moves back in the que by one
		else:
			self.current = 0 
		self.list.itemconfigure(self.current + 1, bg='#9A61D8') #when you move tracks back, it changes the shade so you can see how far back
		#you have went from where you where
		self.play_song() #plays the existing song




	def next_song(self):
		if self.current < len(self.playlist) - 1: #skips to the next track and moved up the playlist
			self.current += 1 # adds to move up the track
		else:
			self.current = 0
		self.list.itemconfigure(self.current - 1, bg='#CB88FF') #when you move to the next song, it changes the color to a darker shade, to show that
		#the song has already been played
		self.play_song()


#change  volume for the volume slider

	def change_volume(self, event=None):
		self.vol = self.volume.get() #gets the current volume
		mixer.music.set_volume(self.vol / 10) #divides the volume by the 10 for each level on the slider
	



############################################################################################
#                                 MAIN
############################################################################################

root = tk.Tk()
#sets the window size
root.geometry('680x405')
#configures the deufult background color
root.configure(bg='#121640')
#the title for the window
root.wm_title('pyBox Music Player')
#gets the various icons and ui assets needed
root.iconphoto(False, tk.PhotoImage(file='code/UI/icon.png'))
img = PhotoImage(file='code/UI/music.png')
next_ = PhotoImage(file = 'code/UI/next.png')
prev = PhotoImage(file='code/UI/previous.png')
play = PhotoImage(file='code/UI/play.png')
pause = PhotoImage(file='code/UI/pause.png')


Pybox_main = Player(master=root)
#initalizes the entire program
Pybox_main.mainloop()
#runs the whole program