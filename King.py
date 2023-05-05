import pygame
from Piece import Piece

class King(Piece):
	def __init__(self, x, y, color, board):
		super().__init__(x, y, color, board)
		img_path = f'images/{color}-king.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height))
		self.notation = 'k'

	def possible_moves(self):
		pass

	def valid_moves(self):
		pass

	def valid_jumps(self):
		pass