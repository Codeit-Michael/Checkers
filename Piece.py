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
		is_jump = False
		# Logic for getting valid moves for a normal piece
		if not self.is_king:
			# move for black
			if self.color == 'black':
				# left move
				if self.board.get_piece_from_pos((self.x - 1, self.y + 1)) is None:
					valid_moves.append((self.x - 1, self.y + 1), is_jump)
				
				# left jump
				elif self.board.get_piece_from_pos((self.x - 1, self.y + 1)) not None:
					# is_jump = True
					# tile_behind = -x, +y >> increase 2
					# while is_jump:
					# 	try:
					# 		if tile_behind == None:
					# 			valid_moves.append((tile_behind), is_jump)
					# 			tile_behind = -x, +y >> increase 2
					# 		else:
					# 			is_jump = False
					# 	except:
					# 		is_jump = False
					# 		continue
					pass

				# right move
				if self.board.get_piece_from_pos((self.x + 1, self.y + 1)) is None:
					valid_moves.append((self.x + 1, self.y + 1), is_jump)

				# right jump
				elif self.board.get_piece_from_pos((self.x + 1, self.y + 1)) not None:
					# is_jump = True
					# tile_behind = +x, +y >> increase 2
					# while is_jump:
					# 	try:
					# 		if tile_behind == None:
					# 			valid_moves.append((tile_behind), is_jump)
					# 			tile_behind = +x, +y >> increase 2
					# 		else:
					# 			is_jump = False
					# 	except:
					# 		is_jump = False
					# 		continue
					pass

			# move for red
			else:
				# left move
				if self.board.get_piece_from_pos((self.x - 1, self.y - 1)) is None:
					valid_moves.append((self.x - 1, self.y - 1), is_jump)
				# left jump
				elif self.board.get_piece_from_pos((self.x - 1, self.y - 1)) not None:
					# is_jump = True
					# tile_behind = -x, -y >> increase 2
					# while is_jump:
					# 	try:
					# 		if tile_behind == None:
					# 			valid_moves.append((tile_behind), is_jump)
					# 			tile_behind = -x, -y >> increase 2
					# 		else:
					# 			is_jump = False
					# 	except:
					# 		is_jump = False
					# 		continue
					pass

				if self.board.get_piece_from_pos((self.x + 1, self.y - 1)) is None:
					valid_moves.append((self.x + 1, self.y - 1)is_jump)
				# right jump
				elif self.board.get_piece_from_pos((self.x + 1, self.y - 1)) not None:
					# is_jump = True
					# tile_behind = +x, -y >> increase 2
					# while is_jump:
					# 	try:
					# 		if tile_behind == None:
					# 			valid_moves.append((tile_behind), is_jump)
					# 			tile_behind = +x, -y >> increase 2
					# 		else:
					# 			is_jump = False
					# 	except:
					# 		is_jump = False
					# 		continue
					pass

		return valid_moves