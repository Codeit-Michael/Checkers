class Board:
	"""
	vars:
	tile width
	tile height
	board size
	selected piece
	turn
	winner
	tile list
	
	funcs:
	generate squares
	setup board
	get tile
	get piece
	handle click
	"""
	pass

class Tile:
	"""
	vars:
	pos
	abs pos
	tile height
	tile width
	color
	piece
	highlight
	rect for repr

	funcs:
	draw
	"""
	pass

class Piece:
	"""
	vars:
	color
	pos

	funcs:
	"""
	pass

class Pawn(Piece):
	"""
	vars:
	super().__init__(color, pos)
	notation
	image

	funcs:
	valid moves
	attack moves
	"""
	pass

class King(Piece):
	"""
	vars:
	super().__init__(color, pos)
	notation
	image

	funcs:
	valid moves
	attack moves
	"""
	pass

class Game:
	"""
	funcs:
	check tiles
	check piece
	message
	"""
	pass

class Main:
	pass