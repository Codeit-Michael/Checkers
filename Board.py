import pygame
from Tile import Tile

class Board:
	def __init__(self,tile_width, tile_height, board_size):
		self.tile_width = tile_width
		self.tile_height = tile_height
		self.board_size = board_size
		self.selected_piece = None

		self.turn = "black"
		self.winner = None

		self.config = [
			['', 'bp', '', 'bp', '', 'bp', '', 'bp'],
			['bp', '', 'bp', '', 'bp', '', 'bp', ''],
			['', 'bp', '', 'bp', '', 'bp', '', 'bp'],
			['', '', '', '', '', '', '', ''],
			['', '', '', '', '', '', '', ''],
			['rp', '', 'rp', '', 'rp', '', 'rp', ''],
			['', 'rp', '', 'rp', '', 'rp', '', 'rp'],
			['rp', '', 'rp', '', 'rp', '', 'rp', '']
		]

		self. tile_list = self.generate_tiles()
		# self.setup()

	def generate_tiles(self):
		output = []
		for y in range(8):
			for x in range(8):
				output.append(
					Tile(x,  y, self.tile_width, self.tile_height)
				)
		return output

	def get_tile_from_pos(self, pos):
		for tile in self.tile_list:
			if (tile.x, tile.y) == (pos[0], pos[1]):
				return tile

	def handle_click(self, pos):
		if self.selected_piece is None:
			piece = self.get_piece_from_pos(pos)
			if piece is not None and piece.color == self.turn:
				self.selected_piece = piece
		else:
			tile = self.get_tile_from_pos(pos)
			if tile in self.selected_piece.get_valid_moves():
				self.move_piece(self.selected_piece, tile)
			self.selected_piece = None

		def move_piece(self, piece, tile):
			# Update piece position and occupying tile
			piece.x, piece.y = tile.x, tile.y
			piece.pos = (piece.x, piece.y)
			tile.occupying_piece = piece

			# Clear selected piece and update turn
			self.selected_piece = None
			self.turn = 'black' if self.turn == 'red' else 'red'

	def get_piece_from_pos(self, pos):
		return self.get_tile_from_pos(pos).occupying_piece

	def setup(self):
		# iterating 2d list
		for y, row in enumerate(self.config):
			for x, piece in enumerate(row):
				if piece != '':
					square = self.get_square_from_pos(x, y)
					square.occupying_piece = Piece(x, y, 'red' if piece[0] == 'r' else 'black', self)

	def handle_click(self):
		pass

	def draw(self, display):
		if self.selected_piece is not None:
			self.get_tile_from_pos(self.selected_piece.pos).highlight = True
			for tile in self.selected_piece.get_valid_moves(self):
				tile.highlight = True

		for square in self.tile_list:
			square.draw(display)