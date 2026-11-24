import pygame as py
import math

from configs import SCREEN_WIDTH, SCREEN_HEIGHT

G = 6.67430e-11  # Gravitational constant
SCALE = 6e-11 
ZOOM_SCALE = 1e-9 
DT = 86400

zoomed = False


class Body(py.sprite.Sprite):
	def __init__(self, x, y, vx, vy, mass, radius, color):
		super().__init__()
		
		self.x, self.y = x, y
		self.vx, self.vy = vx, vy
		self.mass = mass
		self.radius = radius
		self.color = color
		self.trail = []

		self.image = py.surface.Surface((radius*2,radius*2)).convert_alpha()
		self.image.set_colorkey((0,0,0))
		self.rect = self.image.get_rect()
		py.draw.circle(self.image,self.color,(radius,radius),radius)

	def update_position(self, bodies):
		fx = fy = 0
		for other in bodies:
			if other != self:
				dx = other.x - self.x
				dy = other.y - self.y
				r = math.sqrt(dx*dx + dy*dy)
				if r > 0:
					# Formula: F = G * (m1 * m2) / r^2
					f = G * self.mass * other.mass / (r*r)
					fx += f * dx / r
					fy += f * dy / r
		
		# Formula: a = F / m  (based on F = ma)
		ax = fx / self.mass
		ay = fy / self.mass
		self.vx += ax * DT
		self.vy += ay * DT
		self.x += self.vx * DT
		self.y += self.vy * DT
		
		current_scale = ZOOM_SCALE if zoomed else SCALE

		self.trail.append((int(self.x * current_scale + SCREEN_WIDTH//2), int(self.y * current_scale + SCREEN_HEIGHT//2)))
		if len(self.trail) > 200:
			self.trail.pop(0)

	def draw(self, screen):
		# if len(self.trail) > 1:
		# 	py.draw.lines(screen, (50, 50, 50), False, self.trail, 1)
		
		current_scale = ZOOM_SCALE if zoomed else SCALE

		screen_x = int(self.x * current_scale)
		screen_y = int(self.y * current_scale)

		# screen_x = int(self.x)
		# screen_y = int(self.y)
		self.rect.topleft = (screen_x,screen_y)

		return self.rect.topleft

	def set_scale(scale):
		return ZOOM_SCALE if scale else SCALE
		






bodies = [
	Body(0, 0, 0, 0, 1.989e30, 14, (255, 255, 0)),  # Sun  (1.989e30 kg, 8 pixel radius (not used in calculations, just visual))
	Body(5.79e10, 0, 0, 47360, 3.301e23, 4, (169, 169, 169)),  # Mercury
	Body(1.082e11, 0, 0, 35020, 4.867e24, 6, (255, 165, 0)),  # Venus
	Body(1.496e11, 0, 0, 29780, 5.972e24, 8, (0, 100, 255)),  # Earth
	Body(2.79e11, 0, 0, 24077, 6.39e23, 6, (255, 100, 0)),  # Mars
	Body(7.786e11, 0, 0, 13070, 1.898e27, 10, (200, 150, 100)),  # Jupiter
	Body(1.432e12, 0, 0, 9680, 5.683e26, 9, (250, 200, 100)),  # Saturn
	Body(2.867e12, 0, 0, 6810, 8.681e25, 8, (100, 200, 255)),  # Uranus
	Body(4.515e12, 0, 0, 5430, 1.024e26, 8, (0, 0, 255)),  # Neptune
	Body(5.906e12, 0, 0, 4670, 1.309e22, 4, (150, 100, 50)),  # Pluto
]
