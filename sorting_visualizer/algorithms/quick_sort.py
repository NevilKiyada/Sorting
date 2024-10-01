# Quick sort algorithm 

from sorting_visualizer.gui.draw import draw_list


def quick_sort(draw_info, ascending=True):
    lst = draw_info.lst

    def partition(start, end):
        pivot_index = start
        pivot = lst[pivot_index]

        while start < end:
            while start < len(lst) and ((lst[start] <= pivot and ascending) or (lst[start] >= pivot and not ascending)):
                start += 1

            while (lst[end] > pivot and ascending) or (lst[end] < pivot and not ascending):
                end -= 1

            if start < end:
                lst[start], lst[end] = lst[end], lst[start]
                draw_list(draw_info, {start: draw_info.GREEN, end: draw_info.RED}, True)
                yield True

        lst[end], lst[pivot_index] = lst[pivot_index], lst[end]
        draw_list(draw_info, {end: draw_info.GREEN, pivot_index: draw_info.RED}, True)
        

        yield True

        return end
     
    def quick_sort_recursive(start, end):
        if start < end:
            p = yield from partition(start, end)
            yield from quick_sort_recursive(start, p - 1)
            yield from quick_sort_recursive(p + 1, end)

    yield from quick_sort_recursive(0, len(lst) - 1)
