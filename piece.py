import pygame

class Piece:
	def __init__(self, pos, color, board):
		self.pos = pos
		self.x = pos[0]
		self.y = pos[1]
		self.color = color
		self.has_moved = False


	def move(self, board, tile, force=False):			
		for i in board.tiles:
			i.highlight = False

		if tile in self.get_valid_moves(board) or force:
			prev_tile = board.get_tile_from_pos(self.pos)
			self.pos, self.x, self.y = tile.pos, tile.x, tile.y

			prev_tile.occupying_piece = None
			tile.occupying_piece = self
			board.selected_piece = None
			self.has_moved = True

			# Pawn promotion
			if self.notation == ' ':
				if self.y == 0 or self.y == 7:
					from king import King
					tile.occupying_piece = King(
						(self.x, self.y), self.color, board
					)

			return True
		else:
			board.selected_piece = None
			return False

	# can be removed in future versions
	def get_moves(self, board):
		output = []
		for direction in self.get_possible_moves(board):
			for tile in direction:
				if tile.occupying_piece is not None:
					if tile.occupying_piece.color == self.color:
						break
					else:
						output.append(tile)
						break
				else:
					output.append(tile)
		return output

	def get_valid_moves(self, board):
		output = []
		for tile in self.get_moves(board):
			# if not board.is_in_check(self.color, board_change=[self.pos, tile.pos]):
			output.append(tile)

		return output

	# True for all pieces except pawn
	# Can be removed in later versions
	def attacking_tiles(self, board):
		return self.get_moves(board)
