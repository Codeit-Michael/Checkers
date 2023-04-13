import pygame

from piece import Piece

class Pawn(Piece):
	def __init__(self, pos, color, board):
		super().__init__(pos, color, board)

		img_path = f"images/{color}-pawn.png"
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height))

		self.notation = ' '


	def get_possible_moves(self, board):
		output = []
		moves = []

		# move forward
		if self.color == 'red':
			moves.append((0, -1))

		elif self.color == 'black':
			moves.append((0, 1))

		for move in moves:
			new_pos = (self.x, self.y + move[1])
			if new_pos[1] < 8 and new_pos[1] >= 0:
				output.append(
					board.get_tile_from_pos(new_pos)
				)

		return output


	def get_moves(self, board):
		output = []
		for tile in self.get_possible_moves(board):
			if tile.occupying_piece != None:
				break
			else:
				output.append(tile)

		if self.color == 'red':
			if self.x + 1 < 8 and self.y - 1 >= 0:
				tile = board.get_tile_from_pos(
					(self.x + 1, self.y - 1)
				)
				if tile.occupying_piece != None:
					if tile.occupying_piece.color != self.color:
						output.append(tile)
			if self.x - 1 >= 0 and self.y - 1 >= 0:
				tile = board.get_tile_from_pos(
					(self.x - 1, self.y - 1)
				)
				if tile.occupying_piece != None:
					if tile.occupying_piece.color != self.color:
						output.append(tile)

		elif self.color == 'black':
			if self.x + 1 < 8 and self.y + 1 < 8:
				tile = board.get_tile_from_pos(
					(self.x + 1, self.y + 1)
				)
				if tile.occupying_piece != None:
					if tile.occupying_piece.color != self.color:
						output.append(tile)
			if self.x - 1 >= 0 and self.y + 1 < 8:
				tile = board.get_tile_from_pos(
					(self.x - 1, self.y + 1)
				)
				if tile.occupying_piece != None:
					if tile.occupying_piece.color != self.color:
						output.append(tile)

		return output

	def attacking_tiles(self, board):
		moves = self.get_moves(board)
		# return the diagonal moves 
		return [i for i in moves if i.x != self.x]