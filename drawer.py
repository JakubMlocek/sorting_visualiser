import pygame

pygame.init()

class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BACKGROUND_COLOR = BLACK

    GREY_GRADIENTS = [
        (128,128,128),
        (160,160,160),
        (192,192,192)
    ]

    SIDE_PAD = 100
    TOP_PAD = 150

    FONT = pygame.font.SysFont('comicsans',25)
    LARGE_FONT = pygame.font.SysFont('comicsans',40)


    def __init__(self, width, height, tab):
        self.width = width
        self.height= height
        
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualisation")
        self.set_list(tab)

    def set_list(self, tab):
        self.tab = tab
        self.min_val = min(tab)
        self.max_val = max(tab)

        self.block_width = (self.width - self.SIDE_PAD) // len(tab) #calculating width of blocks based on length of array
        self.block_height = (self.height - self.TOP_PAD) / (self.max_val - self.min_val) #calculating height of blocks basen on difference between max and min val
        self.start_x = self.SIDE_PAD // 2

    
def draw(draw_info, sorting_algorithm_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(f"{sorting_algorithm_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.WHITE)
    draw_info.window.blit(title, (draw_info.width//2 - title.get_width()//2,5))
    
    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.WHITE)
    draw_info.window.blit(controls, (draw_info.width//2 - controls.get_width()//2,55))
    
    sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort", 1, draw_info.WHITE)
    draw_info.window.blit(sorting, (draw_info.width//2 - sorting.get_width()//2,85))

    draw_tab(draw_info)
    pygame.display.update()

def draw_tab(draw_info, colored_positions = {}, clear_bg = False):
    tab = draw_info.tab

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD, 
                     draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)


    for i, val in enumerate(tab):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GREY_GRADIENTS[i % 3] 

        if i in colored_positions:
            color = colored_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()