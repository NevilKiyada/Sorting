# Shell sort algorithm 

from sorting_visualizer.gui.draw import draw_list


def shell_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and ((lst[j - gap] > temp and ascending) or (lst[j - gap] < temp and not ascending)):
                lst[j] = lst[j - gap]
                j -= gap
                draw_list(draw_info, {j: draw_info.GREEN, j+gap: draw_info.RED}, True)
                yield True
            lst[j] = temp
            draw_list(draw_info, {j: draw_info.GREEN, i: draw_info.RED}, True)
            
            yield True
        gap //= 2
