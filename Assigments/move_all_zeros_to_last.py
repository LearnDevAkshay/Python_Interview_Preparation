def move_zeros_to_last(my_list):
    for i in range(0, len(my_list)):
        if my_list[i] == 0:
            my_list.pop(i)
            my_list.append(0)

    return my_list