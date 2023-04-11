import pygame

from board import Board

pygame.init()

WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

def draw(display):
	display.fill('white')
	board.draw(display)
	pygame.display.update()


if __name__ == '__main__':
	running = True
	while running:
		mx, my = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					board.handle_click(mx, my)

		# if board.is_in_checkmate('black'):
		# 	print('White wins!')
		# 	running = False
		# elif board.is_in_checkmate('white'):
		# 	print('Black wins!')
		# 	running = False

		draw(screen)


# import pygame
# from board import Board

# pygame.init()
# pygame.font.init()

# screen_height, screen_width = 640, 640
# screen = pygame.display.set_mode((screen_height, screen_width))
# pygame.display.set_caption("Tic Tac Toe")

# class Checkers:
# 	def __init__(self):
# 		self.running = True
# 		self.font = pygame.font.SysFont("Courier New", 35)
# 		self.FPS = pygame.time.Clock()

# 	def main(self):
# 		board = Board(screen_height, screen_width)
# 		while self.running:
# 			for self.event in pygame.event.get():
# 				if self.event.type == pygame.QUIT:
# 					self.running = False

# 			pygame.display.flip()
# 			self.FPS.tick(60)


# if __name__ == "__main__":
# 	h = Checkers()
# 	h.main()