# Merge sort algorithm 




from sorting_visualizer.gui.draw import draw_list


def merge_sort(draw_info, ascending=True):
    lst = draw_info.lst

    def merge_sort_recursive(start, end):
        if end - start > 1:
            mid = (start + end) // 2
            yield from merge_sort_recursive(start, mid)
            yield from merge_sort_recursive(mid, end)
            left = lst[start:mid]
            right = lst[mid:end]
            k = start
            i = 0
            j = 0
            while start + i < mid and mid + j < end:
                if (left[i] < right[j] and ascending) or (left[i] > right[j] and not ascending):
                    lst[k] = left[i]
                    i = i + 1
                else:
                    lst[k] = right[j]
                    j = j + 1
                k = k + 1
                draw_list(draw_info, {k: draw_info.GREEN, k+1: draw_info.RED}, True)
                yield True

            while start + i < mid:
                lst[k] = left[i]
                i = i + 1
                k = k + 1
                draw_list(draw_info, {k: draw_info.GREEN, k+1: draw_info.RED}, True)
                yield True

            while mid + j < end:
                lst[k] = right[j]
                j = j + 1
                k = k + 1
                draw_list(draw_info, {k: draw_info.GREEN, k+1: draw_info.RED}, True)
                yield True

    yield from merge_sort_recursive(0, len(lst))
