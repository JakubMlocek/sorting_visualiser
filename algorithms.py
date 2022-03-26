from drawer import draw_tab

class SortingAlgorithms:
    @staticmethod    
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

    @staticmethod
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

    @staticmethod
    def selection_sort(draw_info, ascending = True):
        T = draw_info.tab
        n = len(T)
        for i in range(n):
            to_swap = i
            for idx in range(i + 1, n):
                if T[idx] < T[to_swap] and ascending:
                    to_swap = idx
                elif T[idx] > T[to_swap] and not ascending:
                    to_swap = idx
                draw_tab(draw_info, {i: draw_info.GREEN, to_swap: draw_info.RED}, True)
                T[i], T[to_swap] = T[to_swap], T[i]
                yield True
        return T

