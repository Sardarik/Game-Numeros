import pygame as pg
from configurations import *
import random
from logic import *



pg.init()


temp_sign=None
temp_move=[]  
move=[]  
number_of_the_move=0  
player1=0 
player2=0 
checked_matrix=[['-1'] * 15 for _ in range(15)]  



class Cell(pg.sprite.Sprite):
    """
    Представляет одну ячейку на игровом поле.

    Атрибуты:
    x (int): X-координата ячейки.
    y (int): Y-координата ячейки.
    color (int): Индекс цвета или типа ячейки.
    image (pygame.Surface): Изображение, представляющее ячейку.
    rect (pygame.Rect): Прямоугольник, используемый для отображения и коллизий.
    sign (str): Знак или значение, размещённое в ячейке.
    is_occupated (bool): Признак занятости ячейки (есть ли в ней знак).
    is_anchored (bool): Признак закреплённости ячейки (можно ли изменить знак).
    """
    
    def __init__(self, color_index: int, size: int, coord: tuple):
        """
        Инициализирует объект ячейки.

        :param color_index: Индекс цвета или типа ячейки.
        :type color_index: int
        :param size: Размер ячейки в пикселях.
        :type size: int
        :param coord: Координаты ячейки на поле (x, y).
        :type coord: tuple[int, int]
        :raises ValueError: Если координаты или индекс цвета недопустимы.
        """
        x, y = coord
        super().__init__()
        self.x = x
        self.y = y
        self.color = color_index
        self.image = pg.image.load(IMG_PATH + IMAGE[color_index])
        self.image = pg.transform.scale(self.image, (size, size))
        self.rect = pg.Rect(x * size, y * size, size, size)
        self.sign = ""
        self.is_occupated = False
        self.is_anchored = False



class Buttons(pg.sprite.Sprite):
    """
    Представляет кнопку на игровом экране.

    Атрибуты:
    x (int): X-координата кнопки.
    y (int): Y-координата кнопки.
    image (pygame.Surface): Изображение кнопки.
    rect (pygame.Rect): Прямоугольник, определяющий размеры и положение кнопки.
    """
    
    def __init__(self, size: int, coord: tuple, file_name: str):
        """
        Инициализирует кнопку.

        :param size: Размер кнопки (в пикселях).
        :type size: int
        :param coord: Координаты верхнего левого угла кнопки на экране (x, y).
        :type coord: tuple[int, int]
        :param file_name: Имя файла изображения кнопки.
        :type file_name: str
        :raises ValueError: Если указанный файл изображения не найден или неправильный путь.
        """
        x, y = coord
        super().__init__()
        self.x = x
        self.y = y
        self.image = pg.image.load(BUTTONS_PATH + file_name)
        self.image = pg.transform.scale(self.image, (size, size))
        self.rect = pg.Rect(x, y, size, size)



class Sign(pg.sprite.Sprite):
    """
    Представляет знаки.

    Атрибуты:
    sign (str): Знак.
    image (pygame.Surface): Изображение знака, загруженное из файла.
    rect (pygame.Rect): Прямоугольник, определяющий размеры и положение знака на экране.
    cell (Cell): Клетка, к которой прикреплен знак.
    """
    
    def __init__(self, sign: str, cell: Cell):
        """
        Инициализирует знак, связывает его с клеткой и загружает изображение.

        :param sign: Знак, который будет отображаться.
        :type sign: str
        :param cell: Клетка, в которой будет находиться Знак.
        :type cell: Cell
        :raises ValueError: Если файл изображения для символа не найден или неправильный путь.
        """
        cell_size = CELL_SIZE
        super().__init__()
        self.sign = sign
        picture = pg.image.load(SIGNS_PATH + sign + '.png')
        self.image = pg.transform.scale(picture, (cell_size, cell_size))
        self.rect = cell.rect
        self.cell = cell



class Equal(Sign):
    """
    Представляет знак "=" на игровом поле, наследующий от класса `Sign`.

    Атрибуты:
    sign (str): Знак, который отображается на плитке (в данном случае всегда "=").
    image (pygame.Surface): Изображение знака загруженное из файла.
    rect (pygame.Rect): Прямоугольник, определяющий размеры и положение знака на экране.
    cell (Cell): Клетка, к которой прикреплен знак.
    """

    def __init__(self, coord: tuple):
        """
        Инициализирует знак "=" и размещает его в заданной координате на игровом поле.

        :param coord: Координаты (x, y), где будет отображаться символ "=".
        :type coord: tuple
        :raises ValueError: Если возникнут проблемы при создании клетки или загрузке изображения.
        """
        self.__size = CELL_SIZE  
        dummy_cell = Cell(0, self.__size, coord) 
        super().__init__('=', dummy_cell) 
        self.rect.topleft = coord  



class GameArea:
    """
    Класс, представляющий игровую область, содержащую клетки, кнопки и символы игры.

    Атрибуты:
    __screen (pg.Surface): Поверхность, на которой будет отрисовываться игровая область.
    __count (int): Количество клеток в игровом поле (размер поля).
    __size (int): Размер каждой клетки.
    __hand_count_elements (int): Количество элементов в руке игрока.
    __hand_count_lines (int): Количество строк в руке игрока.
    __signs_types (list): Список типов знаков для игры.
    __all_cells (pg.sprite.Group): Группа всех клеток на игровом поле.
    __all_signs (pg.sprite.Group): Группа всех символов на игровом поле.
    __all_hand_cells (pg.sprite.Group): Группа клеток в руке игрока.
    __all_buttons (pg.sprite.Group): Группа кнопок для управления игрой.
    player1_score (int): Очки игрока 1.
    player2_score (int): Очки игрока 2.
    Font_text (pg.font.Font): Шрифт для отображения текста (например, очков).
    """

    def __init__(self, parent_surface: pg.Surface, 
                 cell_count: int=CELL_COUNT, 
                 cell_size: int=CELL_SIZE,
                 hand_cell_count_elements: int=HAND_CELL_COUNT_ELEMENTS,
                 hand_cell_count_lines: int=HAND_CELL_COUNT_LINES):
        """
        Инициализирует игровую область.

        :param parent_surface: Поверхность Pygame, на которой будет рисоваться игровая область.
        :type parent_surface: pg.Surface
        :param cell_count: Количество клеток по вертикали и горизонтали на игровом поле.
        :type cell_count: int, по умолчанию CELL_COUNT
        :param cell_size: Размер одной клетки.
        :type cell_size: int, по умолчанию CELL_SIZE
        :param hand_cell_count_elements: Количество элементов в руке игрока.
        :type hand_cell_count_elements: int, по умолчанию HAND_CELL_COUNT_ELEMENTS
        :param hand_cell_count_lines: Количество строк в руке игрока.
        :type hand_cell_count_lines: int, по умолчанию HAND_CELL_COUNT_LINES
        :raises ValueError: Если параметры некорректны (например, неверное количество клеток или размер).
        """
        self.__screen = parent_surface
        self.__count = cell_count
        self.__size = cell_size
        self.__hand_count_elements = hand_cell_count_elements
        self.__hand_count_lines = hand_cell_count_lines
        self.__signs_types = SIGNS_ARRAY
        self.__all_cells = pg.sprite.Group()
        self.__all_signs = pg.sprite.Group()
        self.__all_hand_cells = pg.sprite.Group()
        self.__all_buttons = pg.sprite.Group()
        self.__draw_area()  
        self.__draw_all_signs()  
        self.__draw_all_buttons()  
        pg.display.update()


        self.player1_score = 0
        self.player2_score = 0

        self.Font_text = FONT_TEXT


    def __draw_area(self):
        """
        Рисует игровую область, включая поле и руку игрока.


        :raises ValueError: Если в процессе рисования возникает ошибка (например, неверные координаты или размер).
        """
        self.__draw_field()
        self.__draw_hand()

    def __draw_field(self):
        """
        Рисует игровое поле.

        :raises ValueError: Если возникла ошибка при создании или рисовании клеток.
        """
        total_width = self.__count * self.__size  # Вычисление общей ширины поля
        self.__all_cells = self.__create_all_cells()  # Создание всех клеток
        cell_offset = ((WINDOW_SIZE[0] - total_width) // 2, (WINDOW_SIZE[1] - total_width) // 2 - 25)  # Центровка поля
        self.__draw_cells_on_playboard(self.__all_cells, cell_offset)  # Рисуем клетки на экране


    def __draw_hand(self):
        """
        Рисует руку игрока (набора клеток).

        :raises ValueError: Если возникла ошибка при создании или рисовании клеток руки.
        """
        self.__all_hand_cells = self.__create_hand()  
        hand_cell_offset = ((WINDOW_SIZE[0] - self.__hand_count_elements * self.__size) // 2,
                            (WINDOW_SIZE[1]) // 2 + self.__count * self.__size // 2 - 15)  
        self.__draw_cells_on_playboard(self.__all_hand_cells, hand_cell_offset)  


    def __create_all_cells(self):
        """
        Создаёт все клетки на игровом поле.

        :returns: Группа спрайтов всех клеток поля.
        :rtype: pg.sprite.Group

        :raises ValueError: Если возникла ошибка при создании клетки.
        """
        group=pg.sprite.Group()
        for x in range(self.__count):
            for y in range(self.__count):
                if x == CELL_COUNT // 2 and y == x:
                    cell=Cell(1, self.__size, (x, y))
                else:
                    cell=Cell(0, self.__size, (x, y))
                group.add(cell)
        return group

    def __create_hand(self):
        """
        Создаёт клетки для руки игрока.
        
        :returns: Группа спрайтов клеток руки игрока.
        :rtype: pg.sprite.Group

        :raises ValueError: Если возникла ошибка при создании клетки.
        """
        group=pg.sprite.Group()
        for x in range(self.__hand_count_elements):
            for y in range(self.__hand_count_lines):
                hand_cell=Cell(0, self.__size, (x, y))
                group.add(hand_cell)
        return group

    def __draw_cells_on_playboard(self, cells_to_draw, cell_offset):
        """
        Отображает клетки на игровом поле с учётом смещения.

        :param cells_to_draw: Клетки, которые необходимо отобразить на поле.
        :type cells_to_draw: pg.sprite.Group
        :param cell_offset: Смещение для отображения клеток (по осям X и Y).
        :type cell_offset: tuple[int, int]

        :raises ValueError: Если произошла ошибка при отрисовке клеток.
        """
        for cell in cells_to_draw:
            cell.rect.x += cell_offset[0]
            cell.rect.y += cell_offset[1]
        cells_to_draw.draw(self.__screen)

    def __draw_all_signs(self):
        """
        Отображает все знаки на игровом поле.

        :raises ValueError: Если произошла ошибка при установке или отрисовке знаков.
        """
        self.__setup_board()
        self.__all_signs.draw(self.__screen)

    def create_sign(self, sign: str, cell: Cell):
        """
        Создает новый объект знака на основе предоставленного типа знака и ячейки.

        :param sign: Тип знака, который должен быть отображен.
        :type sign: str
        :param cell: Ячейка, в которой должен быть размещен знак.
        :type cell: Cell
        :returns: Новый объект `Sign`, который будет отображаться на игровом поле.
        :rtype: Sign
        :raises ValueError: Если возникает ошибка при создании знака или если предоставлены некорректные данные.
        """
        return Sign(sign=sign, cell=cell)
    
    def __setup_board(self):
        """
        Настраивает начальное состояние игрового поля, заполняя все клетки на руке случайными знаками.

        :raises ValueError: Если возникает ошибка при установке знаков для ячеек.
        """
        for var in self.__all_hand_cells:
            varsign=SIGNS_ARRAY[random.randrange(0, 13)]
            sign=self.create_sign(sign=varsign, cell=var)
            self.__all_signs.add(sign)
            var.is_occupated=True
            var.sign=varsign
            
    def __clear_player_hand(self):
        """
        Очищает руку игрока от всех знаков.

        :raises ValueError: Может быть выброшено, если возникла ошибка при очистке руки игрока.
        """
        for cell in self.__all_hand_cells:
            if cell.is_occupated:
                sign_to_remove = next((sign for sign in self.__all_signs if sign.cell == cell), None)
                if sign_to_remove:
                    self.__all_signs.remove(sign_to_remove)
                cell.is_occupated = False
                cell.sign = ""
        self.__grand_update()

    def __draw_all_buttons(self):
        """
        Отрисовывает все кнопки на игровом экране, включая кнопку равенства и кнопку ввода.

        :raises ValueError: Если возникает ошибка при отрисовке кнопок.
        """
        self.__draw_equal()
        self.__draw_enter()
    
    def __draw_equal(self):
        """
        Отрисовывает кнопку равенства на игровом экране.

        :raises ValueError: Если возникает ошибка при отрисовке кнопки.
        """
        equal_sign=Equal((WINDOW_SIZE[0] * 3 // 4 - 20, WINDOW_SIZE[1] * 3 // 4 + 120))
        self.__all_signs.add(equal_sign)
        self.__all_signs.draw(self.__screen)
        
    def __draw_enter(self):
        """
        Отрисовывает кнопку "Enter" на игровом экране.

        :raises ValueError: Если возникает ошибка при отрисовке кнопки.
        """
        enter_sign=Buttons(self.__size, (WINDOW_SIZE[0] * 3 // 4 + 100, WINDOW_SIZE[1] * 3 // 4 + 120), "Enter.png")
        self.__all_buttons.add(enter_sign)
        self.__all_buttons.draw(self.__screen)

    def __get_cell(self, position: tuple):
        """
        Возвращает ячейку на игровом поле, которая не занята, по указанной позиции.

        :param position: Позиция на экране, где должна находиться ячейка.
        :type position: tuple
        :returns: Ячейка, которая не занята, или None, если такая ячейка не найдена.
        :rtype: Cell or None
        :raises ValueError: Если при проверке возникла ошибка.
        """
        for cell in self.__all_cells:
            if cell.rect.collidepoint(position) and cell.is_occupated == False:
                return cell 
        return None

    def get_sign(self, position):
        """
        Находит и выбирает знак по переданной позиции на экране.

        :param position: Позиция на экране, где пользователь предполагает выбрать знак.
        :type position: tuple
        :returns: None
        :rtype: None
        :raises ValueError: Если при выборе знака произошла ошибка.
        """
        global temp_sign
        for sign in self.__all_signs:
            if sign.rect.collidepoint(position) and not sign.cell.is_anchored:
                temp_sign=sign
                return
        temp_sign=None

    def btn_down(self, button_type: int, position: tuple):
        """
        Обрабатывает нажатие кнопки на игровом поле и выполняет действие, связанное с этим нажатием.

        :param button_type: Тип кнопки, которая была нажата.
        :type button_type: int
        :param position: Позиция на экране, где пользователь нажал для выполнения действия.
        :type position: tuple
        :returns: None
        :rtype: None
        :raises ValueError: Может быть выброшено, если произошла ошибка при обработке события.
        """
        global temp_sign
        global temp_move
        if temp_sign == None:
            self.get_sign(position)
        else: 
            temp_cell=self.__get_cell(position)
            if temp_cell is not None:
                temp_cell.sign=temp_sign.sign
                temp_cell.is_occupated=True
                temp_cell.is_anchored=True
                temp_sign.cell=temp_cell
                temp_sign.rect=temp_cell.rect
                temp_move.append((temp_cell.x, temp_cell.y, temp_sign.sign))
                temp_cell=None
                temp_sign=None
        self.__grand_update()  

    def btn_up(self, button_type: int, position: tuple):
        """
        Обрабатывает отпускание кнопки на игровом поле, выполняя необходимые действия после завершения хода.

        :param button_type: Тип кнопки, которая была отпущена.
        :type button_type: int
        :param position: Позиция на экране, где пользователь отпустил кнопку.
        :type position: tuple
        :returns: None
        :rtype: None
        :raises ValueError: Может быть выброшено, если произошла ошибка при обработке события.
        """
        if any(button.rect.collidepoint(position) for button in self.__all_buttons):
            global temp_move, move, number_of_the_move, player1, player2, checked_matrix
            move=temp_move.copy()
            temp_move.clear()
            self.__draw_equal()
            
            if len(move) == 0:
                return None

            after_move=correctness_of_the_move(move, number_of_the_move, player1, player2, checked_matrix)
            number_of_the_move=after_move[1]
            player1=after_move[2]
            player2=after_move[3]
            checked_matrix=after_move[4]
            print(move)
            print(after_move)
            print(player1, player2)

            if after_move[0] == 0:  
                pass
            elif after_move[0] == 1:
                pass  
            
            self.__clear_player_hand()   
            self.__setup_board()
            self.__draw_score()

        self.__grand_update()


    def __draw_score(self):
        """
        Отображает текущие очки игроков на экране.


        :raises ValueError: Может быть выброшено, если произошла ошибка при отображении счета.
        """
        score_background=pg.Surface((180, 38))  
        score_background.fill(((251, 235, 212))) 
        self.__screen.blit(score_background, (WINDOW_SIZE[0] // 2 - 100, 10))  

        player1_text=self.Font_text.render(f"{self.player1_score}", True, (0, 0, 0))
        player2_text=self.Font_text.render(f"{self.player2_score}", True, (0, 0, 0))
        
        self.__screen.blit(player1_text, (WINDOW_SIZE[0] // 2 - 40, 18))  
        self.__screen.blit(player2_text, (WINDOW_SIZE[0] // 2 + 40, 18))  
  


    def __grand_update(self):
        """
        Выполняет полный обновление экрана, рисуя все объекты игры.

        :raises ValueError: Может быть выброшено, если произошла ошибка при рисовании объектов.
        """
        self.__all_cells.draw(self.__screen)
        self.__all_hand_cells.draw(self.__screen)
        self.__all_signs.draw(self.__screen)
        self.__all_buttons.draw(self.__screen) 
        self.__draw_score() 
        pg.display.update()
