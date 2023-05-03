class Game:

	def __init__(self, board):
		self.board = board
		self.game_over = False
		self.winner = None

	def check_piece(self):
		red_piece = 0
		black_piece = 0
		for y in range(self.board.board_size):
			for x in range(self.board.board_size):
				tile = self.board.get_tile_from_pos((x, y))
				if tile.occupying_piece != None:
					if tile.occupying_piece.color == "red":
						red_piece += 1
					else:
						black_piece += 1
		if red_piece == 0 or black_piece == 0:
			self.winner = "red" if red_piece > black_piece else "black"
			self.game_over = True
		return self.game_over

	def check_jump(self):
		pass
		"""
		requirements:
		pieces for each tile in the board.
		- is_jump == False
		"""

	def message(self):
		print(self.winner)
		"""
		requirements:
		"""