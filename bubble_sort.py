def bubble_sort(a_list: list):
    """
    The function bubble_sort takes a list as an input and returns the sorted list
    :param a_list:
    :return doesn't return anything:
    """
    for i in range(len(a_list)):
        for j in range(0, len(a_list)-i-1):
            if a_list[j] > a_list[i]:
                temp = a_list[j]
                a_list[j] = a_list[j+1]
                a_list[j+1] = temp


my_list = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(my_list)

print(my_list)