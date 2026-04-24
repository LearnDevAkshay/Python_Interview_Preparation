def create_fibonaci_series(num):
    #0 1 1 2 3 5 7
    first = 0
    second = 1
    temp = 0
    f_list = []

    f_list.append(first)
    for i in range(0,num-1):
        f_list.append(second)
        temp= second
        second = second + first
        first = temp

    return f_list



