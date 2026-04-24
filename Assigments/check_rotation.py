def check_rotation(s1, s2):

    if len(s1) != len(s2):
        return False


    return s1 in (s1 + s2)