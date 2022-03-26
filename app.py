import pygame
import random

from drawer import draw, DrawInformation
from algorithms import SortingAlgorithms


def generate_random_list(n, min_val, max_val):
    tab = []

    for _ in range(n):
        val = random.randint(min_val,max_val)
        tab.append(val)
    
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

    sorting_algorithm = SortingAlgorithms.bubble_sort
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
                sorting_algorithm = SortingAlgorithms.insertion_sort
                sorting_algorithm_name = "Insertion Sort"

            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = SortingAlgorithms.bubble_sort
                sorting_algorithm_name = "Bubble Sort"


            elif event.key == pygame.K_s and not sorting:
                sorting_algorithm = SortingAlgorithms.selection_sort
                sorting_algorithm_name = "Selection Sort"

    pygame.quit()


if __name__ == "__main__":
    main()