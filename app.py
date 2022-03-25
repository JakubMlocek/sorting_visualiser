import pygame
import random

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

def generate_random_list(n, min_val, max_val):
    tab = []

    for _ in range(n):
        val = random.randint(min_val,max_val)
        tab.append(val)
    
    return tab
    
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

def bubble_sort(draw_info, ascending = True):
    tab = draw_info.tab

    for i in range(len(tab) - 1):
        for j in range(len(tab) - 1 - i):
            num1 = tab[j]
            num2 = tab[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
                draw_tab(draw_info, {j: draw_info.GREEN, j+1: draw_info.RED}, True)

                yield True
    return tab

def insertion_sort(draw_info, ascending = True):
    tab = draw_info.tab

    for i in range(1, len(tab)):
        curr = tab[i]

        while True:
            ascending_sort = i > 0 and tab[i - 1] > curr and ascending
            descending_sort = i > 0 and tab[i - 1] < curr and not ascending

            if not ascending_sort and not descending_sort:
                break
                
            tab[i] = tab[i - 1]
            i = i - 1
            tab[i] = curr
            draw_tab(draw_info, {i: draw_info.GREEN, i-1: draw_info.RED}, True)
            yield True
    return tab

def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100
    
    tab = generate_random_list(n, min_val, max_val)
    draw_info = DrawInformation(800,600,tab)

    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort
    sorting_algorithm_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(75)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algorithm_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue
                
            if event.key == pygame.K_r:
                tab = generate_random_list(n, min_val, max_val)
                draw_info.set_list(tab)
                sorting = False

            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            
            elif event.key == pygame.K_SPACE and sorting:
                sorting = False

            elif event.key == pygame.K_a and not sorting:
                ascending = True

            elif event.key == pygame.K_d and not sorting:
                ascending = False

            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algorithm_name = "Insertion Sort"

            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algorithm_name = "Bubble Sort"


    pygame.quit()


if __name__ == "__main__":
    main()