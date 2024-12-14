def arithmetic_check(example):
    '''
    Проверяет корректность арифметического выражения и его истинность.

    :param example: Строка, содержащая пример.
    :type example: str

    :returns: True, если выражение корректно и верно, иначе False.
    :rtype: bool

    :raises ValueError: Если входные данные или формат арифметического выражения некорректны.
    '''
    if any(example[j] in '=/*+-' and example[j+1] in '=/*+-' for j in range(len(example)-1)): 
        return False
    
    if example.count('=') != 1:
        return False
    
    if not (example[0] in '1234567890' and example[-1] in '1234567890'):
        return False
    
    

    numbers=[]
    operators=[]
    number=''
    count_of_left_operators=0
    count_of_right_operators=0
    equal_flag=0

    for i in range(len(example)):
         
        if example[i] in '0123456789':
            number += example[i]
        else:
            if example[i] == '=': equal_flag=1
            else:
                if equal_flag == 0: count_of_left_operators += 1
                else: count_of_right_operators += 1
            
            if number[0]=='0' and len(number)>1: 
                return False
            else:
                numbers.append(int(number))
                number=''
            operators.append(example[i])
    numbers.append(int(number))
    

    first_part=0
    second_part=0

    if count_of_left_operators == 1 and count_of_right_operators == 1:
        if operators[0] == '+': first_part=numbers[0] + numbers[1]
        if operators[0] == '-': first_part=numbers[0] - numbers[1]
        if operators[0] == '*': first_part=numbers[0] * numbers[1]
        if operators[0] == '/': first_part=numbers[0] / numbers[1]
        if operators[2] == '+': second_part=numbers[2] + numbers[3]
        if operators[2] == '-': second_part=numbers[2] - numbers[3]
        if operators[2] == '*': second_part=numbers[2] * numbers[3]
        if operators[2] == '/': second_part=numbers[2] / numbers[3]
    elif count_of_left_operators == 1:
        if operators[0] == '+': first_part=numbers[0] + numbers[1]
        if operators[0] == '-': first_part=numbers[0] - numbers[1]
        if operators[0] == '*': first_part=numbers[0] * numbers[1]
        if operators[0] == '/': first_part=numbers[0] / numbers[1]
        second_part=numbers[2]
    elif count_of_right_operators == 1:
        if operators[1] == '+': second_part=numbers[1] + numbers[2]
        if operators[1] == '-': second_part=numbers[1] - numbers[2]
        if operators[1] == '*': second_part=numbers[1] * numbers[2]
        if operators[1] == '/': second_part=numbers[1] / numbers[2]
        first_part=numbers[0]
    else:
        return False


    if first_part == second_part:
        return True
    else:
        return False 
    


    



