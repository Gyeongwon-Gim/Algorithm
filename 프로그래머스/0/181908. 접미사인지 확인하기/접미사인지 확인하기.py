def solution(my_string, is_suffix):
    check = my_string[len(my_string)-len(is_suffix):]
    return 1 if check == is_suffix else 0