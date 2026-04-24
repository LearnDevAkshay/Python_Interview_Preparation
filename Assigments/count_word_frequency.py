def count_word_frequency(my_str):
    words = my_str.split()
    freq ={}
    for word in words:
        if word in freq.keys():
            freq[word] = freq[word]+1
        else:
            freq[word] =1

    return freq
