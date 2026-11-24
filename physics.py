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
		self.image = img_path
		self.trail = []

		self.image = py.surface.Surface((radius*2,radius*2)).convert_alpha()
		self.image.set_colorkey((0,0,0))
		self.rect = self.image.get_rect()
		py.draw.circle(self.image,self.color,(radius,radius),radius)
		# self.image.fill((255,0,255))

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
		

	def draw(self):	
		current_scale = ZOOM_SCALE if zoomed else SCALE

		screen_x = int(self.x * current_scale)
		screen_y = int(self.y * current_scale)

		self.rect.topleft = (screen_x,screen_y)

		return self.rect.topleft

	def set_scale(scale):
		return ZOOM_SCALE if scale else SCALE

	def to_dict(self):
		return {
			"x" : self.x,
			"y" : self.y,
			"vx" : self.dx,
			"vy" : self.vy,
			"mass" : self.mass,
			"radius" : self.radius,
			"color" : self.color,
			"img_path" : self.img_path
		}

	def from_dict(self):
		pass






bodies = [
	Body(0, 0, 0, 0, 1.9e31, 18, (255, 255, 0)),  # Sun  (1.989e30 kg, 8 pixel radius (not used in calculations, just visual))
	Body(5.79e11, 0, 0, 47360, 3.301e23, 6, (169, 169, 169)),  # Mercury
	Body(1.082e12, 0, 0, 35020, 4.867e24, 9, (255, 165, 0)),  # Venus
	Body(1.496e12, 0, 0, 29780, 5.972e24, 10, (0, 100, 255)),  # Earth
	Body(2.79e12, 0, 0, 24077, 6.39e23, 7, (255, 100, 0)),  # Mars
	Body(4.786e12, 0, 0, 13070, 1.898e27, 16, (200, 150, 100)),  # Jupiter
	Body(5.832e12, 0, 0, 9680, 5.683e26, 15, (250, 200, 100)),  # Saturn
	Body(8.567e12, 0, 0, 6810, 8.681e25, 14, (100, 200, 255)),  # Uranus
	Body(9.5e12, 0, 0, 5430, 1.024e26, 13, (0, 0, 255)),  # Neptune
	Body(1.1e13, 0, 0, 4670, 1.309e22, 6, (150, 100, 50)),  # Pluto
]
