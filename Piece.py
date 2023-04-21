import pygame
class Piece:
	def __init__(self, x, y, color, board):
		self.x = x
		self.y = y
		self.pos = (x, y)
		self.color = color
		self.board = board
		self.is_king = False
		self.img = self.load_image()

	def load_image(self):
		# Load image based on color and type of piece
		if self.color == 'black':
			img_path = 'images/black-pawn.png'
		else:
			img_path = 'images/red-pawn.png'
		return pygame.image.load(img_path).convert_alpha()
	
	def get_valid_moves(self):
		valid_moves = []
		# Logic for getting valid moves for a normal piece
		if not self.is_king:
			if self.color == 'black':
				# Check for potential moves diagonally down left and right
				if self.board.get_piece_from_pos((self.x - 1, self.y + 1)) is None:
					valid_moves.append((self.x - 1, self.y + 1))
					if self.board.get_piece_from_pos((self.x + 1, self.y + 1)) is None:
						valid_moves.append((self.x + 1, self.y + 1))
			else:
				# Check for potential moves diagonally up left and right
				if self.board.get_piece_from_pos((self.x - 1, self.y - 1)) is None:
					valid_moves.append((self.x - 1, self.y - 1))
						if self.board.get_piece_from_pos((self.x + 1, self.y - 1)) is None:
							valid_moves.append((self.x + 1, self.y - 1))
