import pygame
from tile import Tile
from pawn import Pawn

class Board:
	def __init__(self, screen_height, screen_width):
		self.tile_height = screen_height // 8
		self.tile_width = screen_width // 8
		self.selected_piece = None
		self.turn = 'black'

		self.config = [
			['','bP','','bP','','bP','','bP'],
			['bP','','bP','','bP','','bP',''],
			['','bP','','bP','','bP','','bP'],
			['','','','','','','',''],
			['','','','','','','',''],
			['rP','','rP','','rP','','rP',''],
			['','rP','','rP','','rP','','rP'],
			['rP','','rP','','rP','','rP','']
		]

		self.tiles = self.generate_tiles()
		self.setup_board()


	def generate_tiles(self):
		output = []
		for row in range(8):
			for col in range(8):
				output.append(
					Tile(col, row, self.tile_width, self.tile_height)
				)
		return output


	def get_tile_from_pos(self, pos):
		for tile in self.tiles:
			if (tile.x, tile.y) == (pos[0], pos[1]):
				return tile


	def get_piece_from_pos(self, pos):
		return self.get_tile_from_pos(pos).occupying_piece


	def setup_board(self):
		# iterating 2d list
		for y, row in enumerate(self.config):
			for x, piece in enumerate(row):
				if piece != '':
					tile = self.get_tile_from_pos((x, y))
					tile.occupying_piece = Pawn(
						(x, y), 'red' if piece[0] == 'r' else 'black', self
					)


	def handle_click(self, mx, my):
		x = mx // self.tile_width
		y = my // self.tile_height
		clicked_tile = self.get_tile_from_pos((x, y))

		if self.selected_piece is None:
			if clicked_tile.occupying_piece is not None:
				if clicked_tile.occupying_piece.color == self.turn:
					self.selected_piece = clicked_tile.occupying_piece

		elif self.selected_piece.move(self, clicked_tile):
			self.turn = 'red' if self.turn == 'black' else 'black'

		elif clicked_tile.occupying_piece is not None:
			if clicked_tile.occupying_piece.color == self.turn:
				self.selected_piece = clicked_tile.occupying_piece


	def draw(self, display):
		if self.selected_piece is not None:
			self.get_tile_from_pos(self.selected_piece.pos).highlight = True
			for tile in self.selected_piece.get_valid_moves(self):
				tile.highlight = True
		for tile in self.tiles:
			tile.draw(display)


	def is_valid_pos(self, pos):
		"""Checks if a given position is a valid tile on a standard checker board."""
		x, y = pos[0], pos[1]
		if x < 0 or x > 7 or y < 0 or y > 7:
			return False
		if (x + y) % 2 == 0:
			return False
		return True
