# Selection sort algorithm 

from sorting_visualizer.gui.draw import draw_list


def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst

    n = len(lst)

    for i in range(n):
        extreme_index = i
        for j in range(i + 1, n):
            if ascending:
                if lst[j] < lst[extreme_index]: 
                    extreme_index = j
            else:
                if lst[j] > lst[extreme_index]:
                    extreme_index = j

        lst[i], lst[extreme_index] = lst[extreme_index], lst[i]

        draw_list(draw_info, {extreme_index: draw_info.GREEN, i: draw_info.RED}, True)
        yield True

    return lst
