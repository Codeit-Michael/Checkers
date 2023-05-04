import pygame
class Piece:
	def __init__(self, x, y, color, board):
		self.x = x
		self.y = y
		self.pos = (x, y)
		self.board = board
		self.color = color
		self.has_moved = False

	def move(self, clicked_tile):
		pass
		# for i in board.squares:
		# 	i.highlight = False

		# if square in self.get_valid_moves(board) or force:
		# 	prev_square = board.get_square_from_pos(self.pos)
		# 	self.pos, self.x, self.y = square.pos, square.x, square.y

		# 	prev_square.occupying_piece = None
		# 	square.occupying_piece = self
		# 	board.selected_piece = None
		# 	self.has_moved = True

		# 	# Pawn promotion
		# 	if self.notation == ' ':
		# 		if self.y == 0 or self.y == 7:
		# 			from data.classes.pieces.Queen import Queen
		# 			square.occupying_piece = Queen(
		# 				(self.x, self.y),
		# 				self.color,
		# 				board
		# 			)

		# 	# Move rook if king castles
		# 	if self.notation == 'K':
		# 		if prev_square.x - self.x == 2:
		# 			rook = board.get_piece_from_pos((0, self.y))
		# 			rook.move(board, board.get_square_from_pos((3, self.y)), force=True)
		# 		elif prev_square.x - self.x == -2:
		# 			rook = board.get_piece_from_pos((7, self.y))
		# 			rook.move(board, board.get_square_from_pos((5, self.y)), force=True)

		# 	return True
		# else:
		# 	board.selected_piece = None
		# 	return False
