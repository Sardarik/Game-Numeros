#тесты для функции мерджа по икс и по игрек

import pytest
from visual import *

def test_valid_sort():
    """Хороший случай - корректная сортировка по первой координате x"""
    data = [(3, 4), (1, 2), (5, 6), (0, 0)]
    expected = [(0, 0), (1, 2), (3, 4), (5, 6)]
    assert merge_sort_by_x(data) == expected

def test_empty_list():
    """Плохой случай - передан пустой список"""
    data = []
    assert merge_sort_by_x(data) == []


def test_valid_sort():
    """Хороший случай - корректная сортировка по второй координате y"""
    data = [(3, 4), (1, 2), (5, 6), (0, 0)]
    expected = [(0, 0), (1, 2), (3, 4), (5, 6)]
    assert merge_sort_by_y(data) == expected

def test_empty_list():
    """Плохой случай - передан пустой список"""
    data = []
    assert merge_sort_by_y(data) == []
    
    
#тесты для проверки арифметики
def test_valid_expression():
    """Хороший случай - корректный математический пример"""
    example = "2+2=4"
    assert arithmetic_check(example) == True

def test_invalid_expression():
    """Плохой случай - некорректный математический пример"""
    example = "2+2=5"
    assert arithmetic_check(example) == False

def test_multiple_equals():
    """Плохой случай - несколько символов равенства"""
    example = "2+2=4=4"
    assert arithmetic_check(example) == False

def test_consecutive_operators():
    """Плохой случай - два оператора подряд"""
    example = "2++2=4"
    assert arithmetic_check(example) == False

def test_leading_zero():
    """Плохой случай - число начинается с нуля"""
    example = "02+3=5"
    assert arithmetic_check(example) == False

def test_negative_number():
    """Странный случай - пример с отрицательным числом"""
    example = "5-10=-5"
    assert arithmetic_check(example) == False
    
#тесты для проверки основной функции хода
def test_valid_vertical_move():
    """Хороший случай - правильный вертикальный ход, образующий корректный пример"""
    move = [(10, 10, '2'), (11, 10, '+'), (12, 10, '2'), (13, 10, '='), (14, 10, '4')]
    number_of_the_move = 0  # первый ход
    player1 = 0
    player2 = 0
    checked_matrix = [['-1'] * 15 for _ in range(15)]
    result = correctness_of_the_move(move, number_of_the_move, player1, player2, checked_matrix)
    assert result[0] == 1  # ход успешен
    assert result[1] == 1  # номер хода увеличился
    assert result[2] == 7  # очки игрока 1 (если value_of_number + value_of_operator = 7)
    assert result[3] == 0  # очки игрока 2 не изменились

def test_invalid_move_overlaps():
    """Плохой случай - пример не пересекается с существующими числами на втором ходу"""
    move = [(10, 10, '4'), (10, 11, '+'), (10, 12, '4'), (10, 13, '='), (10, 14, '8')]
    number_of_the_move = 1  # второй ход
    player1 = 0
    player2 = 0
    checked_matrix = [['0'] * 15 for _ in range(15)]
    result = correctness_of_the_move(move, number_of_the_move, player1, player2, checked_matrix)
    assert result[0] == 0  # ход неуспешен
    assert result[1] == 1  # номер хода не изменился
    assert result[2] == 0  # очки игрока 1 остались прежними
    assert result[3] == 0  # очки игрока 2 остались прежними

def test_invalid_arithmetic_expression():
    """Плохой случай - пример некорректен с точки зрения арифметики"""
    move = [(10, 10, '2'), (11, 10, '/'), (12, 10, '0'), (13, 10, '='), (14, 10, '0')]
    number_of_the_move = 0
    player1 = 0
    player2 = 0
    checked_matrix = [['0'] * 15 for _ in range(15)]
    result = correctness_of_the_move(move, number_of_the_move, player1, player2, checked_matrix)
    assert result[0] == 0  # ход неуспешен
    assert result[1] == 0  # номер хода не изменился
    assert result[2] == 0  # очки игрока 1 остались прежними
    assert result[3] == 0  # очки игрока 2 остались прежними

