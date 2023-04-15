import pygame
from piece import Piece

class Pawn(Piece):
	def __init__(self, pos, color, board):
		super().__init__(pos, color, board)
		img_path = f"images/{color}-pawn.png"
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height))
		self.notation = ''

	def get_possible_moves(self, board):
		output = []
		moves = []

		# move forward
		if self.color == 'red':
			moves.append((1, -1))
			moves.append((-1, -1))

		elif self.color == 'black':
			moves.append((1, 1))
			moves.append((-1, 1))

		for move in moves:
			new_pos = (self.x + move[0], self.y + move[1])
			if board.is_valid_pos(new_pos):
				tile = board.get_tile_from_pos(new_pos)
				if tile.occupying_piece == None:
					output.append(tile)

		return output

	def get_moves(self, board):
		output = []
		for tile in self.get_possible_moves(board):
			if tile.occupying_piece == None:
				output.append(tile)
			else:
				# check if there is an enemy piece that can be captured
				capture_tile = board.get_tile_from_pos((2*tile.x-self.x, 2*tile.y-self.y))
				if capture_tile is not None and capture_tile.occupying_piece is None:
					output.append(capture_tile)

		# add capturing moves
		for dx, dy in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
			new_pos = (self.x + dx, self.y + dy)
			if not board.is_valid_pos(new_pos):
				continue
			tile = board.get_tile_from_pos(new_pos)
			if tile.occupying_piece == None:
				continue
			if tile.occupying_piece.color == self.color:
				continue
			# try to jump over the piece
			new_pos = (self.x + 2 * dx, self.y + 2 * dy)
			if not board.is_valid_pos(new_pos):
				continue
			tile = board.get_tile_from_pos(new_pos)
			if tile.occupying_piece == None:
				output.append(tile)

		return output