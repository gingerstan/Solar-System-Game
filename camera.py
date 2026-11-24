from math import isclose
import sys
from enum import Enum

from configs import *
from pygame import MOUSEWHEEL, SRCALPHA, Event, Surface, Vector2
import pygame as py
from pygame.sprite import Group, Sprite
from load_assets import assets
from physics import Body


class Camera(Group):
	def __init__(self,screen,keys):
		super().__init__()

		self.screen = screen
		self.keys = keys

		self.offset = py.math.Vector2()
		self.half_width = self.screen.get_size()[0] // 2
		self.half_height = self.screen.get_size()[1] // 2

		self.bg_surf = assets["space_BG"].convert_alpha()
		self.bg_rect = self.bg_surf.get_rect(topleft=(0,0))

		self.zoom_scale = DEFAULT_ZOOM
		self.camera_surf_size = (2000,2000)
		self.camera_surf = py.surface.Surface(self.camera_surf_size,py.SRCALPHA)
		self.camera_rect = self.camera_surf.get_rect(center = (self.half_width,self.half_height))
		self.camera_surf_vector = py.math.Vector2(self.camera_surf_size)
		self.camera_offset = py.math.Vector2()
		self.camera_offset.x = self.camera_surf_size[0] // 2 - self.half_width
		self.camera_offset.y = self.camera_surf_size[1] // 2 - self.half_height

		self.keyboard_speed = KEYBOARD_SPEED
		self.screen_moved = False

	def controls(self):
		if self.keys["mouse_up"]:
			self.zoom_scale += (SCROLL_SPEED if self.zoom_scale + SCROLL_SPEED < MAX_ZOOM else 0)
		if self.keys["mouse_down"]:
			self.zoom_scale -= (SCROLL_SPEED if self.zoom_scale - SCROLL_SPEED > MIN_ZOOM else 0)
		if self.keys["w"]:
			self.offset.y -= KEYBOARD_SPEED
			self.screen_moved = True
		if self.keys["a"]:
			self.offset.x -= KEYBOARD_SPEED
			self.screen_moved = True
		if self.keys["s"]:
			self.offset.y += KEYBOARD_SPEED
			self.screen_moved = True
		if self.keys["d"]:
			self.offset.x += KEYBOARD_SPEED
			self.screen_moved = True

	def draw(self,scale):
		self.controls()

		self.camera_surf.fill((0,0,0))

		bg_offset = self.bg_rect.topleft - self.offset + self.camera_offset
		self.camera_surf.blit(self.bg_surf,bg_offset)

		for sprite in self.sprites():
			offset_pos = sprite.draw() - self.offset + self.camera_offset

			screen_x = int(3 * offset_pos.x) + 5000
			screen_y = int(3 * offset_pos.y) + 5000

			rect = py.transform.scale_by(sprite.image,scale)
			self.camera_surf.blit(sprite.image,(screen_x,screen_y))

			if not self.screen_moved:
				sprite.trail.append((screen_x,screen_y))
			else:
				sprite.trail.clear()
		
			if len(sprite.trail) > 200:
				sprite.trail.pop(0)

			if len(sprite.trail) > 1:
				py.draw.lines(self.camera_surf,sprite.color,False,sprite.trail, 5)

		scaled_surf = py.transform.scale(self.camera_surf,(self.camera_surf_vector * self.zoom_scale))
		scaled_rect = scaled_surf.get_rect(center=(self.half_width,self.half_height))

		self.screen.blit(scaled_surf,scaled_rect)
		self.screen_moved = False




class MapLayer(str, Enum):
	STARS_BG = "stars"
	PLANETS_SUN = "system"

