def my_max(a_list: list) -> int:
    """
    The Function Takes a Python List as an input & returns the Maximum value in the List.
    :param a_list:
    :return an Integer value: Maximum Value
    """
    max_value = a_list[0]
    for i in a_list:
        if max_value < i:
            max_value = i
    return max_value


def my_min(a_list: list) -> int:
    """
    The Function Takes a Python List as an input & returns the Minimum value in the List.
    :param a_list:
    :return an Integer value: Minimum Value
    """
    min_value = a_list[0]
    for i in a_list:
        if min_value > i:
            min_value = i
    return min_value


my_list = [5, 9, 3, 6, 87, 4, 199, 10, 25, 1, 78, 87, 63]

print(my_max(a_list=my_list))
print(my_min(a_list=my_list))
