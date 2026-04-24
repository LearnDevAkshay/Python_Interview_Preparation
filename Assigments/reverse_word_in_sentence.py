def reverse_sentence(input_string):
    my_list = input_string.split()
    reverse_list= my_list[::-1]
    return " ".join(reverse_list)