import pygame

class Board:

	def __init__(self, screen_height, screen_width, screen):
		self.cell_height = screen_height // 8
		self.cell_width = screen_width // 8
		self.screen = screen

		self.config = [
			['','bP','','bP','','bP','','bP'],
			['bP','','bP','','bP','','bP',''],
			['','bP','','bP','','bP','','bP'],
			['','','','','','','',''],
			['','','','','','','',''],
			['rP','','rP','','rP','','rP',''],
			['','rP','','rP','','rP','','rP'],
			['rP','','rP','','rP','','rP',''],
		]

		self.light_color = (255, 206, 158)
		self.dark_color = (209, 139, 71)

	def draw_board(self):
		for row in range(8):
			for col in range(8):
				x = col * self.cell_width
				y = row * self.cell_height
				if (row + col) % 2 == 0:
					pygame.draw.rect(self.screen, self.light_color, (x, y, 80, 80))
				else:
					pygame.draw.rect(self.screen, self.dark_color, (x, y, 80, 80))

	def setup_board(self):
		pass
