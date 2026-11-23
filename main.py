import pygame as py
import math as m
import logging
import matplotlib.pyplot as plt
import numpy as np
import time

from event_bus import bus
from input_handler import InputHandler
from game_states import GameStates as GS
from load_assets import assets, screen
from physics import *

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

		objects = [Physics("Sun",0, 0, 0, 0, 1.989e30, 8, (255, 255, 0)),  # Sun  (1.989e30 kg, 8 pixel radius (not used in calculations, just visual))
				    Physics("Mercury",5.79e10, 0, 0, 47360, 3.301e23, 2, (169, 169, 169)),  # Mercury
				    Physics("Venus",1.082e11, 0, 0, 35020, 4.867e24, 3, (255, 165, 0)),  # Venus
				    Physics("Earth",1.496e11, 0, 0, 29780, 5.972e24, 4, (0, 100, 255)),  # Earth
				    Physics("Mars",2.79e11, 0, 0, 24077, 6.39e23, 3, (255, 10, 10)),  # Mars
				    Physics("Jupiter",7.786e11, 0, 0, 13070, 1.898e27, 6, (200, 150, 100)),  # Jupiter
				    Physics("Saturn",1.432e12, 0, 0, 9680, 5.683e26, 5, (250, 200, 100)),  # Saturn
				    Physics("Uranus",2.867e12, 0, 0, 6810, 8.681e25, 4, (100, 200, 255)),  # Uranus
				    Physics("Neptune",4.515e12, 0, 0, 5430, 1.024e26, 4, (0, 0, 255)),  # Neptune
				    Physics("Pluto",5.906e12, 0, 0, 4670, 1.309e22, 2, (150, 100, 50)),  # Pluto
				    Physics("Planet X",1e13, 1e13, -1000, -12, 5e28, 6, (255,0,255))
				]

		factor = 1

		debug = 0
		while self.GS is GS.IN_GAME:
			self.screen.fill((0,0,0))
			self.IH.get_keys()

			if self.IH.left_mouse:
				factor *= 1.02
				for obj in objects:
					obj.trail.clear()

			if self.IH.right_mouse:
				factor /= 1.02
				for obj in objects:
					obj.trail.clear()

			if self.IH.space_bar_click():
				Physics.increase_dt()

			for obj in objects:
				obj.update(objects,factor)
				obj.draw(screen,factor)

				if debug < 100:
					debug += 1
				else:
					debug = 0



			self.IH.update()
			py.display.update()
			self.clock.tick(100)


	def main_menu(self):	
		self.GS = GS.START_MENU

	def end_screen(self):
		pass













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