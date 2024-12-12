import pygame as pg
#pygame is a Python wrapper for the SDL library, which stands for Simple DirectMedia Layer
from configurations import *

class Sign(pg.sprite.Sprite):
    def __init__(self, cell_size: int, points: str, field_name: str, file_name: str):
        '''
        Инициализирует объект с изображением, которое загружается и масштабируется,
        а также сохраняет переданные параметры для дальнейшего использования.

        :param cell_size: Размер клетки, на который будет масштабировано изображение.
        :type cell_size: int
        :param points: Строка, содержащая информацию о баллах или другой информации, связанной с объектом.
        :type points: str
        :param field_name: Название поля, к которому относится объект.
        :type field_name: str
        :param file_name: Имя файла изображения, которое будет загружено.
        :type file_name: str

        :raises TypeError: Если типы переданных аргументов не соответствуют ожидаемым.
        '''
        super().__init__()
        picture = pg.image.load(Signs_path + file_name)
        self.image = pg.transform.scale(picture,(cell_size,cell_size))
        self.rect = self.image.get_rect()
        self.points = points
        self.field_name = field_name


class Sign_0(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        '''
        Инициализирует объект класса Sign_0, который является наследником класса Sign.
        Загружает и масштабирует изображение, а также сохраняет переданные параметры.

        :param cell_size: Размер клетки, на который будет масштабировано изображение.
        :type cell_size: int
        :param points: Строка, содержащая информацию о баллах или другой информации, связанной с объектом.
        :type points: str
        :param field: Название поля, к которому относится объект.
        :type field: str

        :returns: None
        :rtype: None
        :raises TypeError: Если типы переданных аргументов не соответствуют ожидаемым.
        
        '''
        super().__init__(cell_size, points, field, '0.png')


class Sign_1(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '1.png')
    
class Sign_2(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '2.png')

class Sign_3(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '3.png')

class Sign_4(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '4.png')

class Sign_5(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '5.png')


class Sign_6(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '6.png')


class Sign_7(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '7.png')


class Sign_8(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '8.png')


class Sign_9(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '9.png')


class Sign_plus(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '+.png')


class Sign_minus(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '-.png')


class Sign_product(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '*.png')

class Sign_divide(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, ':.png')

class Sign_equal(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '=.png')
