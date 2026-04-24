def duplicate_in_list(actual_list):
    duplicate_list = []
    for i in range(0,len(actual_list)):
        for j in range(i+1,len(actual_list)):
            if actual_list[i] == actual_list[j]:
                if actual_list[i] not in duplicate_list:
                    duplicate_list.append(actual_list[i])



    return duplicate_list
