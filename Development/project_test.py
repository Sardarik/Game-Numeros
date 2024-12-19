#тесты для функции мерджа по икс и по игрек
import unittest
import pytest
from visual import *

def test_valid_sort():
    """Хороший случай - корректная сортировка по первой координате x"""
    data=[(3, 4), (1, 2), (5, 6), (0, 0)]
    expected=[(0, 0), (1, 2), (3, 4), (5, 6)]
    assert merge_sort_by_x(data) == expected

def test_empty_list():
    """Плохой случай - передан пустой список"""
    data=[]
    assert merge_sort_by_x(data) == []


def test_valid_sort():
    """Хороший случай - корректная сортировка по второй координате y"""
    data=[(3, 4), (1, 2), (5, 6), (0, 0)]
    expected=[(0, 0), (1, 2), (3, 4), (5, 6)]
    assert merge_sort_by_y(data) == expected

def test_empty_list():
    """Плохой случай - передан пустой список"""
    data=[]
    assert merge_sort_by_y(data) == []
    
    
#тесты для проверки арифметики
def test_valid_expression():
    """Хороший случай - корректный математический пример"""
    example="2+2=4"
    assert arithmetic_check(example) == True

def test_invalid_expression():
    """Плохой случай - некорректный математический пример"""
    example="2+2=5"
    assert arithmetic_check(example) == False

def test_multiple_equals():
    """Плохой случай - несколько символов равенства"""
    example="2+2=4=4"
    assert arithmetic_check(example) == False

def test_consecutive_operators():
    """Плохой случай - два оператора подряд"""
    example="2++2=4"
    assert arithmetic_check(example) == False

def test_leading_zero():
    """Плохой случай - число начинается с нуля"""
    example="02+3=5"
    assert arithmetic_check(example) == False

def test_negative_number():
    """Странный случай - пример с отрицательным числом"""
    example="5-10=-5"
    assert arithmetic_check(example) == False
    
#тесты для проверки основной функции хода
def test_valid_vertical_move():
    """Хороший случай - правильный вертикальный ход, образующий корректный пример"""
    move=[(10, 10, '2'), (11, 10, '+'), (12, 10, '2'), (13, 10, '='), (14, 10, '4')]
    number_of_the_move=0  # первый ход
    player1=0
    player2=0
    checked_matrix=[['-1'] * 15 for _ in range(15)]
    result=correctness_of_the_move(move, number_of_the_move, player1, player2, checked_matrix)
    assert result[0] == 1  # ход успешен
    assert result[1] == 1  # номер хода увеличился
    assert result[2] == 7  # очки игрока 1 (если value_of_number + value_of_operator=7)
    assert result[3] == 0  # очки игрока 2 не изменились

def test_invalid_move_overlaps():
    """Плохой случай - пример не пересекается с существующими числами на втором ходу"""
    move=[(10, 10, '4'), (10, 11, '+'), (10, 12, '4'), (10, 13, '='), (10, 14, '8')]
    number_of_the_move=1  # второй ход
    player1=0
    player2=0
    checked_matrix=[['0'] * 15 for _ in range(15)]
    result=correctness_of_the_move(move, number_of_the_move, player1, player2, checked_matrix)
    assert result[0] == 0  # ход неуспешен
    assert result[1] == 1  # номер хода не изменился
    assert result[2] == 0  # очки игрока 1 остались прежними
    assert result[3] == 0  # очки игрока 2 остались прежними

def test_invalid_arithmetic_expression():
    """Плохой случай - пример некорректен с точки зрения арифметики"""
    move=[(10, 10, '2'), (11, 10, '/'), (12, 10, '0'), (13, 10, '='), (14, 10, '0')]
    number_of_the_move=0
    player1=0
    player2=0
    checked_matrix=[['0'] * 15 for _ in range(15)]
    result=correctness_of_the_move(move, number_of_the_move, player1, player2, checked_matrix)
    assert result[0] == 0  # ход неуспешен
    assert result[1] == 0  # номер хода не изменился
    assert result[2] == 0  # очки игрока 1 остались прежними
    assert result[3] == 0  # очки игрока 2 остались прежними


IMG_PATH='/Users/aidasardarova/Documents/HSE/АиП/Numeros/Images/'
IMAGE=["image_0.png", "image_1.png"]  

class TestCell(unittest.TestCase):

    def test_cell_initialization(self):
        """ Положительный тест: проверка корректной инициализации ячейки. """
        pg.init()
        
        color_index=1
        size=50
        coord=(5, 10)
        
        cell=Cell(color_index, size, coord)
        
        self.assertEqual(cell.x, 5) 
        self.assertEqual(cell.y, 10)
        self.assertEqual(cell.color, color_index) 
        self.assertEqual(cell.image.get_size(), (size, size)) 
        self.assertEqual(cell.rect.x, 5 * size) 
        self.assertEqual(cell.rect.y, 10 * size)  
        self.assertEqual(cell.rect.width, size)  
        self.assertEqual(cell.rect.height, size) 
        self.assertEqual(cell.sign, "")  
        self.assertFalse(cell.is_occupated) 
        self.assertFalse(cell.is_anchored) 
        pg.quit()

    def test_invalid_size(self):
        """ Отрицательный тест: проверка инициализации с некорректным размером ячейки. """
        pg.init()
        color_index=1
        coord=(5, 5)
        
        size=-50
        with self.assertRaises(ValueError):
            Cell(color_index, size, coord)
        pg.quit()
            
            


BUTTONS_PATH='/Users/aidasardarova/Documents/HSE/АиП/Numeros/Images/Buttons/' 
IMAGE=["Enter.png", "re.png"]  

class TestButtons(unittest.TestCase):


    def test_button_initialization(self):
        """ Положительный тест: проверка правильной инициализации кнопки."""
        pg.init()
        
        size=50
        coord=(100, 150)
        file_name="Enter.png"  
        
        button=Buttons(size, coord, file_name)
        
   
        self.assertEqual(button.x, 100) 
        self.assertEqual(button.y, 150) 
        self.assertEqual(button.image.get_size(), (size, size)) 
        self.assertEqual(button.rect.x, 100)  
        self.assertEqual(button.rect.y, 150)  
        self.assertEqual(button.rect.width, size)  
        self.assertEqual(button.rect.height, size) 
        pg.quit()
    
    def test_invalid_image_file(self):
        """ Отрицательный тест: проверка инициализации с неправильным файлом изображения. """
        pg.init()
        
        size=50
        coord=(100, 150)
        file_name="nonexistent_button.png"  

    
        with self.assertRaises(FileNotFoundError):
            Buttons(size, coord, file_name)
        pg.quit()







class TestGameArea(unittest.TestCase):
    def test_game_area_creation(self):
        """Проверяет, что игровой объект GameArea создается корректно с правильными параметрами."""
        pg.init()
        
        screen=pg.display.set_mode((800, 600)) 
        cell_count=10
        cell_size=50
        hand_cell_count_elements=5
        hand_cell_count_lines=2
        game_area=GameArea(screen, cell_count, cell_size, hand_cell_count_elements, hand_cell_count_lines)
        
        self.assertEqual(game_area._GameArea__count, cell_count)
        self.assertEqual(game_area._GameArea__size, cell_size)
        self.assertEqual(game_area._GameArea__hand_count_elements, hand_cell_count_elements)
        self.assertEqual(game_area._GameArea__hand_count_lines, hand_cell_count_lines)
        self.assertIsInstance(game_area._GameArea__all_cells, pg.sprite.Group)
        self.assertIsInstance(game_area._GameArea__all_signs, pg.sprite.Group)
        self.assertIsInstance(game_area._GameArea__all_hand_cells, pg.sprite.Group)
        self.assertIsInstance(game_area._GameArea__all_buttons, pg.sprite.Group)
        pg.quit()


    def test_invalid_parameters(self):
        """Проверяет, что при некорректных параметрах конструктора выбрасывается ошибка."""
        pg.init()
        screen=pg.display.set_mode((800, 600))  

        invalid_cell_count=-5
        invalid_cell_size=-50
        invalid_hand_cell_count_elements=0
        invalid_hand_cell_count_lines=-2
        

        with self.assertRaises(ValueError):
            game_area=GameArea(screen, invalid_cell_count, invalid_cell_size, invalid_hand_cell_count_elements, invalid_hand_cell_count_lines)
        
        pg.quit()



from unittest.mock import MagicMock

class TestGameArea(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pg.init()  
        cls.display=pg.display.set_mode((800, 600)) 

    @classmethod
    def tearDownClass(cls):
        pg.quit()  

    def setUp(self):
        parent_surface=TestGameArea.display 
        self.game_area=GameArea(parent_surface) 
        self.sign_mock=MagicMock()
        self.sign_mock.rect.collidepoint=MagicMock()
        self.sign_mock.cell.is_anchored=False
        self.game_area._GameArea__all_signs=[self.sign_mock]

       
        self.cell_mock=MagicMock()
        self.cell_mock.rect.collidepoint=MagicMock()
        self.cell_mock.is_occupated=False
        self.game_area._GameArea__all_cells=[self.cell_mock]

    def test_get_sign_positive(self):
        """Положительный тест: знак найден и возвращён."""
        self.sign_mock.rect.collidepoint.return_value=True
        position=(100, 100)
        result=self.game_area.get_sign(position)
        self.assertEqual(result, self.sign_mock)

    def test_get_sign_negative(self):
        """Отрицательный тест: знак не найден."""
        self.sign_mock.rect.collidepoint.return_value=False
        position=(200, 200)
        result=self.game_area.get_sign(position)
        self.assertIsNone(result)

    def test_get_cell_positive(self):
        """Положительный тест: ячейка найдена и не занята."""
        self.cell_mock.rect.collidepoint.return_value=True
        self.cell_mock.is_occupated=False
        position=(50, 50)
        result=self.game_area._GameArea__get_cell(position)
        self.assertEqual(result, self.cell_mock)

    def test_get_cell_negative(self):
        """Отрицательный тест: ячейка не найдена или занята."""
        self.cell_mock.rect.collidepoint.return_value=False
        position=(200, 200)
        result=self.game_area._GameArea__get_cell(position)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
