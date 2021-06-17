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
		super().__init__(master)
		self.master = master
		self.pack()
		mixer.init()

		if os.path.exists('songs.pickle'):
			with open('songs.pickle', 'rb') as f:
				self.playlist = pickle.load(f)
		else:
			self.playlist=[]

		self.current = 0
		self.paused = True
		self.played = False

		self.create_frames()
		self.track_widgets()
		self.control_widgets()
		self.tracklist_widgets()


	def create_frames(self):
		self.track = tk.LabelFrame(self, text='Now playing', 
					font=("Frutiger",15,"bold"),
					bg="#EE3EC9",fg="#4C0BD1",bd=5,relief=tk.GROOVE)
		self.track.config(width=200,height=300)
		self.track.grid(row=0, column=0, padx=10)

		self.tracklist = tk.LabelFrame(self, text=f'PlayList - {str(len(self.playlist))} Songs',
							font=("Frutiger",13,"bold"),
							bg="#FF39AA",fg="#4C0BD1",bd=5,relief=tk.GROOVE)
		self.tracklist.config(width=790,height=200)
		self.tracklist.grid(row=0, column=1, rowspan=4, pady=2)

		self.controls = tk.LabelFrame(self,
							font=("Frutiger",15,"bold"),
							bg="#121640",fg="#121640",bd=2,relief=tk.GROOVE)
		self.controls.config(width=410,height=80)
		self.controls.grid(row=2, column=0, pady=5, padx=10)

		#not really any error handeling needed here, as its so bare bones nothing can go wrong
 

	def track_widgets(self):
		self.canvas = tk.Label(self.track, image=img)
		self.canvas.configure(width=392, height=240)
		self.canvas.configure(bg='#4C0BD1')
		self.canvas.grid(row=0,column=0)

		self.songtrack = tk.Label(self.track, font=("Frutiger",16,"bold"),
						bg="#121642",fg="#00C4CC")
		self.songtrack['text'] = 'PyBox Music Player'
		self.songtrack.config(width=30, height=1)
		self.songtrack.grid(row=1,column=0,padx=10)




	def control_widgets(self):
		self.loadSongs = tk.Button(self.controls, bg='#00C4CC', fg='#121640', font=10)
		self.loadSongs['text'] = 'Load Songs'
		self.loadSongs['command'] = self.retrieve_songs
		self.loadSongs.grid(row=0, column=0, padx=10)

		self.prev = tk.Button(self.controls, image=prev)
		self.prev['command'] = self.prev_song
		self.prev.grid(row=0, column=1)
		self.configure(bg='#121640')

		self.pause = tk.Button(self.controls, image=pause)
		self.pause['command'] = self.pause_song
		self.pause.grid(row=0, column=2)

		self.next = tk.Button(self.controls, image=next_)
		self.next['command'] = self.next_song
		self.next.grid(row=0, column=3)

		self.volume = tk.DoubleVar(self)
		self.slider = tk.Scale(self.controls, from_ = 0, to = 10, orient = tk.HORIZONTAL)
		self.slider.configure(bg='#FF39AA')
		self.slider.configure(fg='black')
		self.slider['variable'] = self.volume
		self.slider.set(0.7)
		mixer.music.set_volume(7)
		self.slider['command'] = self.change_volume
		self.slider.grid(row=0, column=4, padx=7)




	def tracklist_widgets(self):
		self.scrollbar = tk.Scrollbar(self.tracklist, orient=tk.VERTICAL)
		self.scrollbar.grid(row=0,column=1, rowspan=5, sticky='ns')
		self.scrollbar.configure(bg='purple')

		self.list = tk.Listbox(self.tracklist, selectmode=tk.SINGLE,
					 yscrollcommand=self.scrollbar.set, selectbackground='sky blue')
		self.enumerate_songs()
		self.list.config(height=22)
		self.list.bind('<Double-1>', self.play_song) 

		self.scrollbar.config(command=self.list.yview)
		self.list.grid(row=0, column=0, rowspan=5)





	def retrieve_songs(self):
		self.songlist = []
		directory = filedialog.askdirectory()
		for root_, dirs, files in os.walk(directory):
				for file in files:
					if os.path.splitext(file)[1] == '.mp3':
						path = (root_ + '/' + file).replace('\\','/')
						self.songlist.append(path)

		with open('songs.pickle', 'wb') as f:
			pickle.dump(self.songlist, f)
		self.playlist = self.songlist
		self.tracklist['text'] = f'PlayList - {str(len(self.playlist))}'
		self.list.delete(0, tk.END)
		self.enumerate_songs()




	def enumerate_songs(self):
		for index, song in enumerate(self.playlist):
			self.list.insert(index, os.path.basename(song))





	def play_song(self, event=None):
		if event is not None:
			self.current = self.list.curselection()[0]
			for i in range(len(self.playlist)):
				self.list.itemconfigure(i, bg="#00C4CC")

		print(self.playlist[self.current])
		#for intenal debugging
		mixer.music.load(self.playlist[self.current])
		self.songtrack['anchor'] = 'w' 
		self.songtrack['text'] = os.path.basename(self.playlist[self.current])

		self.pause['image'] = play
		self.paused = False
		self.played = True
		self.list.activate(self.current) 
		self.list.itemconfigure(self.current, bg='#00C4CC')

		mixer.music.play()





	def pause_song(self):
		if not self.paused:
			self.paused = True
			mixer.music.pause()
			self.pause['image'] = pause
		else:
			if self.played == False:
				self.play_song()
			self.paused = False
			mixer.music.unpause()
			self.pause['image'] = play





	def prev_song(self):
		if self.current > 0:
			self.current -= 1
		else:
			self.current = 0
		self.list.itemconfigure(self.current + 1, bg='#9A61D8')
		self.play_song()




	def next_song(self):
		if self.current < len(self.playlist) - 1:
			self.current += 1
		else:
			self.current = 0
		self.list.itemconfigure(self.current - 1, bg='#CB88FF')
		self.play_song()



	def change_volume(self, event=None):
		self.v = self.volume.get()
		mixer.music.set_volume(self.v / 10)
	



############################################################################################
#                                 MAIN
############################################################################################

root = tk.Tk()
root.geometry('680x400')
root.configure(bg='#121640')
root.wm_title('pyBox Music Player')
root.iconphoto(False, tk.PhotoImage(file='code/UI/icon.png'))
img = PhotoImage(file='code/UI/music.png')
next_ = PhotoImage(file = 'code/UI/next.png')
prev = PhotoImage(file='code/UI/previous.png')
play = PhotoImage(file='code/UI/play.png')
pause = PhotoImage(file='code/UI/pause.png')


app = Player(master=root)
app.mainloop()