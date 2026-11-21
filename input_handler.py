import pygame as py, sys
from pygame.locals import QUIT
from event_bus import bus

class InputHandler:
	def __init__(self):
		self.left_mouse = False
		self.left_mouse_prev = False

		self.right_mouse = False
		self.right_mouse_prev = False

		self.space = False
		self.space_prev = False

		self.shift = False
		self.shift_prev = False

		self.mouse_pos = (0,0)

		self.keys = {}


	def get_keys(self):
		for event in py.event.get():
			if event.type == QUIT:
				py.quit()
				sys.exit()

			if event.type == py.KEYDOWN:
				if event.key == py.K_SPACE:
					self.space = True
				if event.key == py.K_LSHIFT:
					self.shift = True
		
			if event.type == py.KEYUP:
				if event.key == py.K_SPACE:
					self.space = False
				if event.key == py.K_LSHIFT:
					self.shift = False

			# if event.type == py.KEYDOWN:
			# 	if event.key == py.K_w:

		
			# if event.type == py.KEYUP:
			# 	if event.key == py.K_w:


			if event.type == py.MOUSEBUTTONDOWN:
				if py.mouse.get_pressed()[0]:
					self.left_mouse = True
				if py.mouse.get_pressed()[2]:
					self.right_mouse = True

			if event.type == py.MOUSEBUTTONUP:
				if not py.mouse.get_pressed()[0]:
					self.left_mouse = False
				if not py.mouse.get_pressed()[2]:
					self.right_mouse = False

		self.mouse_pos = py.mouse.get_pos()

		if not self.left_mouse and self.left_mouse_prev:
			bus.call("left_click")

		if not self.right_mouse and self.right_mouse_prev:
			bus.call("right_click")

		if not self.space and self.space_prev:
			bus.call("space_click")

		if not self.shift and self.shift_prev:
			bus.call("shift_click")

	def left_click(self):
		return not self.left_mouse and self.left_mouse_prev 

	def right_click(self):
		return not self.right_mouse and self.right_mouse_prev

	def space_bar_click(self):
		return not self.space and self.space_prev

	def update(self):
		self.left_mouse_prev = self.left_mouse
		self.right_mouse_prev = self.right_mouse
		self.space_prev = self.space
		self.shift_prev = self.shift