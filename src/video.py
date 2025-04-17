import vlc
import platform

from customtkinter import *


class VideoFrame(CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		self.rowconfigure(0, weight=1)

		self.canvas = CTkCanvas(self, width=640, height=360, bg="black")
		self.canvas.grid(row=0, column=0, padx=0, pady=0, columnspan=2)

		self.time_label = CTkLabel(self, text="00:00 / 00:00")
		self.time_label.grid(row=1, column=0, padx=10, pady=10)

		self.playback_control_button = CTkButton(self, text="Pause", command=self.pause_play)
		self.playback_control_button.grid(row=1, column=1, padx=10, pady=10)

		self.instance = vlc.Instance("--no-video-title-show", "--no-sub-autodetect-file")
		self.player = self.instance.media_player_new()


	def load(self, video_path):
		media = self.instance.media_new(video_path)
		self.player.set_media(media)

		if platform.system() == 'Windows':
			self.player.set_hwnd(self.canvas.winfo_id())
		elif platform.system() == 'Linux':
			self.player.set_xwindow(self.canvas.winfo_id())
		elif platform.system() == 'Darwin':
			self.player.set_nsobject(self.canvas.winfo_id())

		self.player.play()


	def pause_play(self):
		self.player.pause()

		if self.player.is_playing():
			self.playback_control_button.configure(text="Play")
		else:
			self.playback_control_button.configure(text="Pause")

