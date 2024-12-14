from merge import *
from operations import arithmetic_check
from configurations import *







def correctness_of_the_move(move, number_of_the_move, player1, player2, checked_matrix):
    '''
    Проверяет корректность хода и обновляет состояние игры.

    :param move: Список элементов, представляющих текущий ход. Каждый элемент — это кортеж в формате 
                 (координата_x, координата_y, символ), где символ может быть числом или оператором (символ поступает в виде        строкового типа данных).
    :type move: list

    :param number_of_the_move: Номер текущего хода.
    :type number_of_the_move: int

    :param player1: Очки первого игрока.
    :type player1: int

    :param player2: Очки второго игрока.
    :type player2: int

    :param checked_matrix: Матрица текущего игрового поля, где каждая ячейка содержит символ либо '-1' 
                           для пустых клеток и каждый пример внесенный в нее - гарантированно корректный.
    :type checked_matrix: list

    :returns: Список из 5 элементов:
              - 1 или 0, указывающий, был ли корректным сделанный ход;
              - Обновленный номер хода;
              - Обновленные очки первого игрока;
              - Обновленные очки второго игрока;
              - Обновленная матрица игрового поля.
    :rtype: list

    :raises ValueError: Если входные данные некорректны.
    '''
    current_matrix = [['-1'] * 15 for _ in range(15)]
    for i in range(15):
        for j in range(15):
            current_matrix[i][j] = checked_matrix[i][j]
    for element in move:
        current_matrix[element[0]][element[1]] = element[2]

    if all(move[j][1] == move[j + 1][1] for j in range(len(move)-1)):
        move = merge_sort_by_y(move)
        lower_pointer = move[-1][0]
        upper_pointer = move[0][0]
        vert = move[0][1]

        example = ''

        for i in range(move[-1][0],-1,-1):
            if current_matrix[i][vert] == '-1': break
            upper_pointer = i
        for i in range(move[0][0],15):
            if current_matrix[i][vert] == '-1': break
            lower_pointer = i

        for i in range(upper_pointer, lower_pointer + 1):
            example += current_matrix[i][vert]

        if number_of_the_move != 0:
            if len(example) <= len(move):
                return [0, number_of_the_move, player1, player2, checked_matrix]

        if arithmetic_check(example):
            new_points = 0
            for i in example:
                if i in '0123456789':
                    new_points += VALUE_OF_NUMBER
                else:
                    new_points += VALUE_OF_OPERATOR
            if (number_of_the_move + 1) % 2 == 0:
                player2 += new_points
            else:
                player1 += new_points
            return [1, number_of_the_move + 1, player1, player2, current_matrix]
        return [0, number_of_the_move, player1, player2, checked_matrix]



    elif all(move[j][0] == move[j+1][0] for j in range(len(move)-1)):
        move = merge_sort_by_x(move)
        left_pointer = 0
        right_pointer =  0
        hor = move[0][0]
        
        example = ''

        for i in range(move[0][1],15):
            if current_matrix[hor][i] == '-1': break
            right_pointer = i
        for i in range(move[-1][1],-1,-1):
            if current_matrix[hor][i] == '-1': break
            left_pointer = i

        for i in range(left_pointer, right_pointer + 1):
            example += current_matrix[hor][i]

        if number_of_the_move != 0:
            if len(example) <= len(move):
                return [0, number_of_the_move, player1, player2, checked_matrix]

        if arithmetic_check(example):
            new_points = 0
            for i in example:
                if i in '0123456789':
                    new_points += VALUE_OF_NUMBER
                else:
                    new_points += VALUE_OF_OPERATOR
            if (number_of_the_move + 1) % 2 == 0:
                player2 += new_points
            else:
                player1 += new_points
            return [1, number_of_the_move + 1, player1, player2, current_matrix]
        return [0, number_of_the_move, player1, player2, checked_matrix]


    else:
        return [0, number_of_the_move, player1, player2, checked_matrix]
    

    

