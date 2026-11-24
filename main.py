import pygame as py
import math as m
import logging
import time
from functools import partialmethod

from configs import (FRAMERATE, INIT_SCREEN_POS, SCREEN_RATIO,
					SCREEN_WIDTH, SCREEN_HEIGHT)
from camera import Camera
from event_bus import bus
from input_handler import InputHandler
from game_states import GameStates as GS
from load_assets import assets, screen
from physics import bodies, Body

class Game:
	g = None
	def __init__(self):
		Game.g = self
		
		self.screen = screen
		self.clock = py.time.Clock()
		self.GS = None

		self.IH = InputHandler()


	def main_loop(self):
		while True:
			self.main_menu()  # menu before game, choose duration
			self.game_loop()  # playing the game
			self.end_screen() # reset game object, show score

	def game_loop(self):
		self.GS = GS.IN_GAME

		cam = Camera(self.screen,self.IH.keys)
		cam.add(bodies)

		debug = 0
		while self.GS is GS.IN_GAME:
			self.screen.fill((0,0,0))
			self.IH.get_keys()
			mouse = self.IH.mouse_pos


			# if self.IH.space_bar_click():
			# 	Physics.increase_dt()

			if self.IH.shift_click():
				s = Body.set_scale(True)
			else:
				s = Body.set_scale(False)

			for body in bodies:
				body.update_position(bodies)
				# body.draw(self.screen)

			cam.controls()
			cam.draw(s)
				
			
			self.IH.update()
			py.display.update()
			dt = self.clock.tick(FRAMERATE) / 1000
			# object.x += FRAMERATE*dt


	def main_menu(self):	
		self.GS = GS.START_MENU

	def end_screen(self):
		pass

	def make_circle_surf(diameter,color):
		r = py.surface.Surface((diameter,diameter))
		py.draw.circle(r,color,(diameter/2,diameter/2),diameter/2)
		return r














if __name__ == "__main__":
	g = Game()
	g.main_loop()



# logging.basicConfig(
# 	level=logging.DEBUG,
# 	format="%(asctime)s - %(levelname)s - %(message)s",
# 	datefmt="%Y-%m-%d %H:%M",
# 	filename="debug.log",  # Omit to print to the console instead
# 	encoding="utf-8",
# )
# debug_logger = logging.getLogger(__name__)