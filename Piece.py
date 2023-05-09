import pygame

class Piece:
	def __init__(self, x, y, color, board):
		self.x = x
		self.y = y
		self.pos = (x, y)
		self.board = board
		self.color = color

	def _move(self, tile):
		# Next prob: empyting jumped tile
		for i in self.board.tile_list:
			i.highlight = False

		if tile in self.valid_moves() and not self.board.is_jump:
			prev_tile = self.board.get_tile_from_pos(self.pos)
			self.pos, self.x, self.y = tile.pos, tile.x, tile.y

			prev_tile.occupying_piece = None
			tile.occupying_piece = self
			self.board.selected_piece = None
			self.has_moved = True

			# Pawn promotion
			if self.notation == 'p':
				if self.y == 0 or self.y == 7:
					from King import King
					tile.occupying_piece = King(
						self.x, self.y, self.color, self.board
					)

			return True
		elif tile in self.valid_jumps():
			prev_tile = self.board.get_tile_from_pos(self.pos)
			self.pos, self.x, self.y = tile.pos, tile.x, tile.y

			prev_tile.occupying_piece = None
			tile.occupying_piece = self
			self.board.selected_piece = None
			self.has_moved = True

			# Pawn promotion
			if self.notation == 'p':
				if self.y == 0 or self.y == 7:
					from King import King
					tile.occupying_piece = King(
						self.x, self.y, self.color, self.board
					)

			return True
		else:
			self.board.selected_piece = None
			return False