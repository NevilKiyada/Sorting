# Heap sort algorithm 
from sorting_visualizer.gui.draw import draw_list

def heap_sort(draw_info, ascending=True):
    lst = draw_info.lst

    def heapify(end, i):
        l = 2 * i + 1
        r = 2 * (i + 1)
        max_idx = i
        if l < end and ((lst[i] < lst[l] and ascending) or (lst[i] > lst[l] and not ascending)):
            max_idx = l
        if r < end and ((lst[max_idx] < lst[r] and ascending) or (lst[max_idx] > lst[r] and not ascending)):
            max_idx = r
        if max_idx != i:
            lst[i], lst[max_idx] = lst[max_idx], lst[i]
            draw_list(draw_info, {i: draw_info.GREEN, max_idx: draw_info.RED}, True)
            yield True
            yield from heapify(end, max_idx)

    length = len(lst)
    start = length // 2 - 1
    for i in range(start, -1, -1):
        yield from heapify(length, i)
    for i in range(length - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        draw_list(draw_info, {i: draw_info.GREEN, 0: draw_info.RED}, True)
        yield True
        yield from heapify(i, 0)
