import pygame
import math

class DrawInformation:
    BLACK = 0, 0, 0  # black
    WHITE = 255, 255, 255  # white
    GREEN = 0, 255, 0  # green
    RED = 255, 0, 0
    GRAY = 150, 182, 182
    OFFWHITE = 206, 194, 179
    SKY = 204, 204, 255
    BACKGROUND_COLOR = SKY
    BUTTN = 159, 226, 191

    GRADIETS = [
        (52, 204, 235),
        (203, 82, 227),
        (128, 128, 128),
    ]

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        # Move the font initialization here
        self.FONT = pygame.font.SysFont('comicsans', 20)
        self.LARGE_FONT = pygame.font.SysFont('comicsans', 28)

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualization")

        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

def draw(draw_info, algo_name, ascending, buttons, elapsed_time):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.BLACK)
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

    time_text = draw_info.FONT.render(f"Time: {elapsed_time:.3f} Sec", 1, DrawInformation.BLACK)
    draw_info.window.blit(time_text, (0, 125))

    for button in buttons:
        button.draw(draw_info.window)

    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD,
                      draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
        color = draw_info.GRADIETS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))
    if clear_bg:
        pygame.display.update()
