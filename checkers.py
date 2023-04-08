import pygame
from board import Board

pygame.init()
pygame.font.init()

screen_height, screen_width = 640, 640
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Tic Tac Toe")

class Checkers:
	def __init__(self):
		self.running = True
		self.font = pygame.font.SysFont("Courier New", 35)
		self.FPS = pygame.time.Clock()

	def draw_piece(self):
		img = pygame.image.load("images/red-pawn.png")
		imgs = pygame.image.load("images/red-pawn.png")
		img = pygame.transform.scale(img, (80, 80))
		imgs = pygame.transform.scale(imgs, (80, 80))
		screen.blit(img, (80, 480, 80, 80))
		screen.blit(imgs, (0, 560, 80, 80))

	def main(self):
		board = Board(screen_height, screen_width, screen)
		board.draw_board()
		self.draw_piece()
		while self.running:
			for self.event in pygame.event.get():
				if self.event.type == pygame.QUIT:
					self.running = False

			pygame.display.flip()
			self.FPS.tick(60)


if __name__ == "__main__":
	h = Checkers()
	h.main()