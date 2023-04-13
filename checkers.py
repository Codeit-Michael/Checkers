import pygame

from board import Board

pygame.init()

WINDOW_SIZE = (640, 640)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Checkers")

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

def draw(display):
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

		# if board.is_win('black'):
		# 	print('Black wins!') --> Message()
		# elif board.is_win('red'):
		# 	print('Red wins!') --> Message()
		# 	running = False

		draw(screen)