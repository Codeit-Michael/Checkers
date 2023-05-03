import pygame
class Piece:
	def __init__(self, x, y, color, board):
		self.x = x
		self.y = y
		self.pos = (x, y)
		self.color = color
		self.has_moved = False