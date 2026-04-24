def first_non_repeating_character(my_str):
    for i in range(0,len(my_str)):
        match_found =  True
        for j in range(i+1,len(my_str)):
            if my_str[i] == my_str[j]:
                match_found = False
                break
        if match_found:
            return my_str[i]

def max_occurring_character(my_str):
    my_set = set(my_str)
    max_count = 0
    max_character = ''
    for item_in_set in my_set:
        current_ch_count = 0
        for ch in range(0,len(my_str)):
            if item_in_set == my_str[ch]:
                current_ch_count = current_ch_count + 1

        if current_ch_count > max_count:
            max_count = current_ch_count
            max_character = item_in_set

    return max_character