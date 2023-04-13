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




# ~~~~~~~~~~~~~~~~~~~~~~~
"""
	def is_in_check(self, color, board_change=None): # board_change = [(x1, y1), (x2, y2)]
		output = False
		king_pos = None

		changing_piece = None
		old_square = None
		new_square = None
		new_square_old_piece = None

		if board_change is not None:
			for square in self.squares:
				if square.pos == board_change[0]:
					changing_piece = square.occupying_piece
					old_square = square
					old_square.occupying_piece = None
			for square in self.squares:
				if square.pos == board_change[1]:
					new_square = square
					new_square_old_piece = new_square.occupying_piece
					new_square.occupying_piece = changing_piece

		pieces = [
			i.occupying_piece for i in self.squares if i.occupying_piece is not None
		]

		if changing_piece is not None:
			if changing_piece.notation == 'K':
				king_pos = new_square.pos
		if king_pos == None:
			for piece in pieces:
				if piece.notation == 'K' and piece.color == color:
						king_pos = piece.pos
		for piece in pieces:
			if piece.color != color:
				for square in piece.attacking_squares(self):
					if square.pos == king_pos:
						output = True

		if board_change is not None:
			old_square.occupying_piece = changing_piece
			new_square.occupying_piece = new_square_old_piece
						
		return output


	def is_in_checkmate(self, color):
		output = False

		for piece in [i.occupying_piece for i in self.squares]:
			if piece != None:
				if piece.notation == 'K' and piece.color == color:
					king = piece

		if king.get_valid_moves(self) == []:
			if self.is_in_check(color):
				output = True

		return output

"""