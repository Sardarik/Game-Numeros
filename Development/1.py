from merge import *
from operations import arithmetic_check
from configurations import *


move1 = [(4, 7, '8'), (5, 7, '+'), (6, 7, '9'), (7, 7, '='), (8, 7, '1'), (9, 7, '7')]
move = [(4, 8, '+'), (4, 9, '4'), (4, 10, '='), (4, 11, '1'), (4, 12, '2')]

checked_matrix = [['-1']*15 for _ in range(15)]
current_matrix = [['-1']*15 for _ in range(15)]
for i in move1:
    checked_matrix[i[0]][i[1]] = i[2]
number_of_the_move = 1
player1 = 8
player2 = 0






current_matrix = [['-1'] * 15 for _ in range(15)]
for i in range(15):
    for j in range(15):
        current_matrix[i][j] = checked_matrix[i][j]
for element in move:
    current_matrix[element[0]][element[1]] = element[2]
    
print(move,all(move[j][0] == move[j + 1][0] for j in range(len(move)-1)),(move[0][j] == move[0][j+1] for j in range(len(move)-1)))
for j in range(len(move)-1):
    print(move[j],move[j][0],move[j + 1][0])
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
            print('error1', number_of_the_move, player1, player2, checked_matrix)

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
        print(1, number_of_the_move + 1, player1, player2, current_matrix)
    print('error2', number_of_the_move, player1, player2, checked_matrix)



elif all(move[0][j] == move[0][j+1] for j in range(len(move)-1)):
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
            print('error3', number_of_the_move, player1, player2, checked_matrix)

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
        print(1, number_of_the_move + 1, player1, player2, current_matrix)
    print('error4', number_of_the_move, player1, player2, checked_matrix)


else:
    print('error5', number_of_the_move, player1, player2, checked_matrix)




