def remove_duplicates(actual_list):
    without_duplicate_list = []
    for i in range(0, len(actual_list)):
        if actual_list[i] in without_duplicate_list:
            pass
        else:
            without_duplicate_list.append(actual_list[i])

    return without_duplicate_list