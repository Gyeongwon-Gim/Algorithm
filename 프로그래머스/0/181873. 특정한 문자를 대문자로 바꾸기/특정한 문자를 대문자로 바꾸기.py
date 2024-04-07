def solution(my_string, alp):
    while True:
        if alp in my_string :    
            idx = my_string.index(alp)
            my_string = list(my_string)
            my_string[idx] = my_string[idx].upper()
        else: 
            break
    return ''.join(my_string)