def rotate_list(actual_list, input_rotation):
    actual_rotation_required = input_rotation % len(actual_list)
    print(actual_list[-actual_rotation_required::] + actual_list[:-actual_rotation_required])
    return actual_list[-actual_rotation_required::] + actual_list[:-actual_rotation_required]