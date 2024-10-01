# Entry point for the application 
from sorting_visualizer.gui.draw import DrawInformation
from sorting_visualizer.gui.draw import draw

from sorting_visualizer.gui.button import Button
from sorting_visualizer.algorithms.bubble_sort import bubble_sort
from sorting_visualizer.algorithms.selection_sort import selection_sort
from sorting_visualizer.algorithms.insertion_sort import insertion_sort
from sorting_visualizer.algorithms.quick_sort import quick_sort
from sorting_visualizer.algorithms.merge_sort import merge_sort
from sorting_visualizer.algorithms.heap_sort import heap_sort
from sorting_visualizer.algorithms.shell_sort import shell_sort
from utils.file_operations import select_csv_file, read_csv
from utils.list_operations import generate_starting_list, store_csv_file
import pygame
import time

def main():
    pygame.init()
    pygame.font.init()
    run = True
    clock = pygame.time.Clock() 

    n = 50
    min_val = 0
    max_val = 100
    sorting = False
    elapsed_time = 0  # Variable to store elapsed time
    start_time = None  # Variable to store the start time


    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(1000, 750, lst)
    draw_info = DrawInformation(1000, 750, lst)
    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None
   
    # print ("Before sorting list="+draw_info.lst)

    buttons = [
        Button(775, 0, 100, 28, "Reset", draw_info.RED, draw_info.FONT, draw_info.WHITE),
        Button(900, 0, 100, 28, "Start", draw_info.GREEN, draw_info.FONT),
        Button(0, 10, 110, 50, "Ascending", draw_info.GRAY, draw_info.FONT),
        Button(0, 70, 110, 50, "Descending", draw_info.GRAY, draw_info.FONT),
        Button(150, 78, 100, 50, "Insertion", draw_info.BUTTN, draw_info.FONT),
        Button(270, 78, 100, 50, "Bubble", draw_info.BUTTN, draw_info.FONT),
        Button(390, 78, 100, 50, "Selection", draw_info.BUTTN, draw_info.FONT),
        Button(870, 78, 100, 50, "Quick", draw_info.BUTTN, draw_info.FONT),
        Button(630, 78, 100, 50, "Merge", draw_info.BUTTN, draw_info.FONT, draw_info.WHITE),
        Button(750, 78, 100, 50, "Heap", draw_info.BUTTN, draw_info.FONT),
        Button(510, 78, 100, 50, "Shell", draw_info.BUTTN, draw_info.FONT),
        Button(900, 40, 100, 28, "GetList", draw_info.BUTTN, draw_info.FONT),
        Button(775, 40, 100, 28, "Load CSV", draw_info.BUTTN, draw_info.FONT)  # New CSV button
    ]

    while run:
        clock.tick(30)
        if sorting:
            try:
                next(sorting_algorithm_generator)
                elapsed_time = time.time() - start_time  # Update elapsed time
            except StopIteration:
                
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending, buttons,elapsed_time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                for button in buttons:
                    if button.is_clicked(pos):
                        if button.text == "Reset":
                            lst = generate_starting_list(n, min_val, max_val)
                            draw_info.set_list(lst)
                            elapsed_time = 0  # Reset elapsed time
                            start_time = None  # Reset start time
                        elif button.text == "Start" and not sorting:
                            sorting = True
                            sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
                            start_time = time.time()  # Set start time
                        elif button.text == "Ascending" and not sorting:
                            ascending = True
                        elif button.text == "Descending" and not sorting:
                            ascending = False
                            
                        elif button.text == "Insertion" and not sorting:
                            sorting_algorithm = insertion_sort
                            sorting_algo_name = "Insertion Sort"
                        elif button.text == "Bubble" and not sorting:
                            sorting_algorithm = bubble_sort
                            sorting_algo_name = "Bubble Sort"
                        elif button.text == "Selection" and not sorting:
                            sorting_algorithm = selection_sort
                            sorting_algo_name = "Selection Sort"
                        elif button.text == "Quick" and not sorting:
                            sorting_algorithm = quick_sort
                            sorting_algo_name = "Quick Sort"
                        elif button.text == "Merge" and not sorting:
                            sorting_algorithm = merge_sort
                            sorting_algo_name = "Merge Sort"
                        elif button.text == "Heap" and not sorting:
                            sorting_algorithm = heap_sort
                            sorting_algo_name = "Heap Sort"
                        elif button.text == "Shell" and not sorting:
                            sorting_algorithm = shell_sort
                            sorting_algo_name = "Shell Sort"
                        elif button.text == "Load CSV":
                            file_path = select_csv_file()
                            if file_path:
                                lst = read_csv(file_path)
                                draw_info.set_list(lst)
                                elapsed_time = 0  # Reset elapsed time
                        elif button.text == "GetList":
                            store_csv_file(lst , sorting_algo_name)

        
    pygame.quit()
    pass

if __name__ == "__main__":
    main()





