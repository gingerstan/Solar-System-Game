import pygame as py
import math as m
import logging

from event_bus import bus
from input_handler import InputHandler
from game_states import GameStates as GS
from load_assets import assets

logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s - %(levelname)s - %(message)s",
	datefmt="%Y-%m-%d %H:%M",
	filename="debug.log",  # Omit to print to the console instead
	encoding="utf-8",
)
debug_logger = logging.getLogger(__name__)


class Game:

	def __init__(self):
		py.init()
		py.display.set_caption("solar system something")
		self.screen = py.display.set_mode((1000,1000), 0, 32)
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
		
		while self.GS is GS.IN_GAME:
			self.screen.fill((0,0,0))
			self.IH.get_keys()




			self.IH.update()
			py.display.update()
			self.clock.tick(120)


	def main_menu(self):	
		self.GS = GS.START_MENU

	def end_screen(self):
		pass













if __name__ == "__main__":
	g = Game()
	g.main_loop()