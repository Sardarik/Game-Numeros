from sign_items import *
import board_data
pg.init()
Font_text = pg.font.SysFont('applemyungjo', 30)

class Field:
    def __init__(self, parent_surface: pg.Surface, 
                 cell_count: int=Cell_count, cell_size: int = Cell_size):
        '''
            
        Инициализирует объект игрового поля с заданными параметрами.

        :param parent_surface: Поверхность, на которой будет отрисовываться игровое поле (обычно это окно или экран игры).
        :type parent_surface: pg.Surface
        :param cell_count: Количество ячеек в игровом поле (по умолчанию `Cell_count`).
        :type cell_count: int
        :param cell_size: Размер каждой ячейки на экране (по умолчанию `Cell_size`).
        :type cell_size: int
        :returns: None
        :rtype: None
        :raises TypeError: Если один из параметров имеет неправильный тип (например, не является объектом `pg.Surface` для `parent_surface`).

        Создает игровое поле с заданным количеством ячеек и их размером, а также инициирует все необходимые группы спрайтов
        для отображения поля и знаков на экране. После инициализации автоматически обновляется экран.
        
        '''
        self.__screen = parent_surface
        self.__table = board_data.playboard
        self.__count = cell_count
        self.__size = cell_size
        self.__signs_types = Signs_types
        self.__all_cells = pg.sprite.Group()
        self.__all_signs = pg.sprite.Group()
        self.__pressed_cell = None
        self.__picked_sign = None
        self.__draw_field()
        self.__draw_all_signs()
        pg.display.update()


    def __draw_field(self):
        '''
       Отрисовывает все клетки на игровом поле с учетом их размера и смещения.

        Метод рассчитывает общую ширину поля, создает все клетки с помощью метода `__create_all_cells`,
        а затем рисует клетки на экране с учетом заданного смещения, чтобы разместить поле по центру экрана.

        :returns: None
        :rtype: None
        :raises TypeError: Если объекты `self.__count`, `self.__size`, или другие используемые параметры имеют неправильный тип (не являются целыми числами).
        

        '''
        total_width = self.__count * self.__size
        self.__all_cells = self.__create_all_cells()
        cell_offset = ((Window_size[0] - total_width) // 2, (Window_size[1]-total_width) // 2 - 25)
        self.__draw_cells_on_playboard(cell_offset)


    def __create_all_cells(self):
        '''
        Создает все клетки для игрового поля и добавляет их в группу спрайтов.

        Метод создает клетки для поля размером `__count` x `__count`, где каждая клетка
        имеет размер `__size`. Если клетка находится в центре поля (или по определенному
        условию), она получает особый тип (например, с другим значением цвета или другого
        свойства). Каждая клетка добавляется в группу спрайтов для последующей отрисовки.

        :returns: Группа спрайтов, содержащая все клетки для игрового поля.
        :rtype: pg.sprite.Group
        :raises TypeError: Если объект `self.__count` или `self.__size` имеет неправильный тип (не является целым числом).
        
        '''
        group = pg.sprite.Group()
        for x in range(self.__count):
            for y in range(self.__count):
                if x == Cell_count//2 and y == x:
                    cell = Cell(
                        1,
                        self.__size,
                        (x,y),
                        'F' + str(self.__count-y) + str(self.__count-x)
                        )
                else:
                    cell = Cell(
                        0,
                        self.__size,
                        (x,y),
                        'F' + str(self.__count-y) + str(self.__count-x)
                        )
                group.add(cell)
        return group
    
    
    def __draw_cells_on_playboard(self,cell_offset):
        '''
        Отображает все клетки на игровом поле с учетом смещения.

        Метод перебирает все клетки, применяет к их координатам смещение, переданное через
        параметр `cell_offset`, а затем рисует все клетки на экране.

        :param cell_offset: Смещение, которое будет применено к каждой клетке. 
                            Это кортеж, содержащий два целых числа (x, y), представляющих
                            смещение по осям X и Y.
        :type cell_offset: tuple
        :returns: None
        :rtype: None
        :raises TypeError: Если параметр `cell_offset` не является кортежем с двумя целыми числами.
        
        '''
        for cell in self.__all_cells:
            cell.rect.x += cell_offset[0]
            cell.rect.y += cell_offset[1]
        self.__all_cells.draw(self.__screen)


    def __draw_all_signs(self):
        '''
        Настраивает игровое поле и рисует все знаки на экране.

        Метод вызывает метод `__setup_board` для размещения знаков на поле в соответствии
        с данными таблицы, а затем отрисовывает все знаки, добавленные в коллекцию `__all_signs`,
        на экране.

        :returns: None
        :rtype: None
        :raises TypeError: Если структура данных для знаков или экрана некорректна.
        
        '''
        self.__setup_board()
        self.__all_signs.draw(self.__screen)


    def __setup_board(self):
        '''
        Настроить игровое поле, разместив знаки на основе данных таблицы.

        Метод перебирает все ячейки в таблице `__table`, проверяет значение в каждой ячейке.
        Если значение не равно 0, создается знак для этой ячейки и добавляется в коллекцию всех знаков.
        Затем для каждого знака устанавливается его позиция на экране, соответствующая полю на игровом поле.

        :returns: None
        :rtype: None
        :raises TypeError: Если структура данных `__table` или других компонентов некорректна.
        
        '''
        for j, row in enumerate(self.__table):
            for i, field_value in enumerate(row):
                if field_value != 0:
                    sign = self.__create_sign(field_value, (j,i))
                    self.__all_signs.add(sign)
        for sign in self.__all_signs:
            for cell in self.__all_cells:
                if sign.field_name == cell.field_name:
                    sign.rect = cell.rect.copy()
    

    def __create_sign(self, sign_symbol: str, table_coord: tuple):
        '''
      Создает знак на игровом поле по символу и координатам.

        Этот метод использует символ знака и его координаты на игровом поле для создания
        соответствующего знака. Метод извлекает тип знака из словаря `__signs_types`, 
        а затем создает экземпляр соответствующего класса знака.

        :param sign_symbol: Символ знака, который нужно создать. Например, 'X' или 'O'.
        :type sign_symbol: str
        :param table_coord: Координаты клетки на игровом поле, где будет размещен знак.
        :type table_coord: tuple
        :returns: Экземпляр класса знака, созданный на основе переданного символа и координат.
        :rtype: экземпляр класса знака (например, объект типа `XSign` или `OSign`)
        :raises TypeError: Если переданный символ не существует в словаре `__signs_types` или координаты некорректны.
        
        '''
        field_name = self.__to_field_name(table_coord)
        sign_tuple = self.__signs_types[sign_symbol]
        classname = globals()[sign_tuple[0]]
        return classname(self.__size, sign_tuple[1], field_name)


    def __to_field_name(self, table_coord: tuple):
        '''
        Находит клетку по заданным координатам на экране.

        Этот метод перебирает все клетки на игровом поле и проверяет, перекрывает ли клетка
        точку, соответствующую позиции клика. Если такая клетка найдена, она возвращается.
        Если клетка не найдена, возвращается `None`.

        :param position: Позиция на экране в формате (x, y), для которой нужно найти клетку.
        :type position: tuple
        :returns: Клетка, на которую нажали, если она была найдена; `None`, если клетка не найдена.
        :rtype: Cell | None
        :raises TypeError: Если параметр `position` не является кортежем из двух целых чисел.
        
        '''
        return 'F' + str(self.__count - table_coord[0]) + str(self.__count - table_coord[1])


    def __get_cell(self, position:tuple):
        '''
        Ищет клетку, которая содержит точку, заданную в параметре `position`.
    
        Этот метод проверяет все клетки на наличие столкновения с точкой, переданной
        в параметре `position`. Если такая клетка найдена, она возвращается. В противном
        случае возвращается `None`.

        :param position: Кортеж, содержащий координаты точки (x, y), которую нужно проверить.
        :type position: tuple

        :returns: Клетка, в которой находится указанная точка, или None, если клетка не найдена.
        :rtype: Union[Cell, None]
        
        '''
        for cell in self.__all_cells:
            if cell.rect.collidepoint(position):
                return cell
        return None
    

    def btn_down(self, button_type: int, position: tuple):
        '''
        Обрабатывает событие нажатия кнопки мыши. Определяет, какую клетку было выбрано на экране,
        и сохраняет ее в `__pressed_cell`.

        Этот метод вызывается, когда пользователь нажимает на экран. Он использует позицию
        нажатия для определения клетки, которая была выбрана, и сохраняет эту клетку для
        дальнейшей обработки.

        :param button_type: Тип кнопки мыши (например, левая, правая кнопка).
        :type button_type: int
        :param position: Позиция на экране, где было произведено нажатие, в формате (x, y).
        :type position: tuple
        :returns: None
        :rtype: None
        :raises TypeError: Если переданный параметр `position` не является кортежем с двумя целыми числами.
        
        '''
        self.__pressed_cell = self.__get_cell(position)

    
    def btn_up(self, button_type: int, position:tuple):
        '''
       Создает группу клеток для руки игрока и рисует их на экране с учетом смещения.

        Этот метод вызывает функцию для создания клеток руки, затем рассчитывает смещение для
        правильного расположения клеток на экране, и рисует их на экране с использованием
        метода `__draw_hand_cells`.

        :returns: None
        :rtype: None
        :raises TypeError: Если типы данных для создания клеток руки неверны (например, если координаты или размер не правильные).
        
        '''
        released_cell = self.__get_cell(position)
        if (released_cell is not None) and (released_cell == self.__pressed_cell):
            if button_type == 1:
                self.__pick_cell(released_cell)
        self.__grand_update()

    def __pick_cell(self,cell):
        '''
        Обрабатывает выбор клетки для перемещения знака. Если знак не выбран, выбирает его.
        Если знак уже выбран, перемещает его в новую клетку.

        Этот метод проверяет, выбран ли уже знак. Если нет, он выбирает знак, который соответствует
        выбранной клетке. Если знак уже выбран, то он перемещается в новую клетку.

        :param cell: Клетка, с которой производится взаимодействие (выбор или перемещение знака).
        :type cell: Cell
        :returns: None
        :rtype: None
        :raises TypeError: Если переданный параметр не является экземпляром класса `Cell`.
        '''
        if self.__picked_sign is None:
            for sign in self.__all_signs:
                if sign.field_name == cell.field_name:
                    self.__picked_sign = sign
                    break
        else:
            self.__picked_sign.rect=cell.rect
            self.__picked_sign.field__name = cell.field_name
            self.__picked_sign = None

    def __grand_update(self):
        '''
        Отображает все клетки и знаки на экране, обновляя его.

        Этот метод отрисовывает все элементы, хранящиеся в группах `__all_cells` и `__all_signs`,
        и обновляет экран, чтобы отобразить изменения.

        :returns: None
        :rtype: None
        :raises TypeError: Если объекты в группах `__all_cells` или `__all_signs` не поддерживают метод `draw` (не являются спрайтами).
        
        '''
        self.__all_cells.draw(self.__screen)
        self.__all_signs.draw(self.__screen)
        pg.display.update()


class Hand(Field):
    def __init__(self, parent_surface: pg.Surface, 
                 cell_count: int = Cell_count, cell_size: int = Cell_size,
                 hand_cell_count_elements: int=Hand_cell_count_elements, hand_cell_count_lines: int=Hand_cell_count_lines):
        '''
        Инициализирует объект, создавая таблицу с клетками и знаками, а также выполняет настройку экрана.

        Этот конструктор инициализирует параметры для клеток и знаков, а также устанавливает 
        поверхность для отрисовки и другие важные параметры для поля и руки игрока. 
        После инициализации вызываются методы для рисования клеток и знаков.

        :param parent_surface: Поверхность Pygame, на которой будет отрисовываться игра.
        :type parent_surface: pg.Surface
        :param cell_count: Количество клеток в игровом поле.
        :type cell_count: int
        :param cell_size: Размер клетки (ширина и высота) в пикселях.
        :type cell_size: int
        :param hand_cell_count_elements: Количество элементов в руке игрока (по горизонтали).
        :type hand_cell_count_elements: int
        :param hand_cell_count_lines: Количество линий в руке игрока (по вертикали).
        :type hand_cell_count_lines: int
        :returns: None
        :rtype: None
        :raises TypeError: Если параметры не соответствуют ожидаемым типам (например, если передаются значения неправильного типа).
        
        '''
        #super().__init__()
        self.__screen = parent_surface
        self.__hand_table = board_data.handboard
        self.__count = cell_count
        self.__size = cell_size
        self.__signs_types = Signs_types
        self.__all_hand_cells = pg.sprite.Group()
        self.__all_signs = pg.sprite.Group()
        self.__hand_count_elements = hand_cell_count_elements
        self.__hand_count_lines = hand_cell_count_lines
        self.__pressed_hand_cell = None
        self.__picked_hand_sign = None
        self.__draw_hand()
        self.__draw_all_signs()
        pg.display.update()

    def __draw_hand(self):
        '''
        Создает клетки для руки игрока и рисует их на экране с учетом смещения.

        Этот метод вызывает функцию для создания клеток руки, затем рассчитывает смещение для
        правильного расположения клеток на экране, и рисует их с использованием метода `__draw_hand_cells`.

        :returns: None
        :rtype: None
        :raises TypeError: Если типы данных для создания клеток или расчета смещения некорректны, например,
            
        '''
        self.__all_hand_cells = self.__create_hand()
        hand_cell_offset  = ((Window_size[0] - self.__hand_count_elements*self.__size) // 2,(Window_size[1])//2 + self.__count*self.__size//2 - 15)

        self.__draw_hand_cells(hand_cell_offset)


    def __create_hand(self):
        '''
        Создает и возвращает группу спрайтов клеток для руки игрока.

        Этот метод создает группы клеток, где каждая клетка имеет уникальные координаты и имя,
        и добавляет их в группу спрайтов. Клетки представляют собой ячейки в руке игрока.

        :returns: Группа спрайтов, содержащая все клетки руки игрока.
        :rtype: pg.sprite.Group
        :raises TypeError: Если при создании клетки передаются неверные типы данных (например, если координаты не кортеж).
        
        '''
        group = pg.sprite.Group()
        for x in range(self.__hand_count_elements):
            for y in range(self.__hand_count_lines):
                hand_cell = Cell(
                    0,
                    self.__size,
                    (x,y),
                    'H'+str(self.__hand_count_lines-y)+str(self.__hand_count_elements-x)
                )
                group.add(hand_cell)
        return group


    def __draw_hand_cells(self, hand_cell_offset):
        '''

        Рисует клетки на экране с учетом смещения для каждой клетки.

        Этот метод перебирает все клетки в группе `__all_hand_cells`, применяет смещение 
        по оси X и Y для каждой клетки, а затем рисует их на экране.

        :param hand_cell_offset: Смещение для клеток (кортеж из двух значений), где
                                первый элемент - смещение по оси X, второй - по оси Y.
        :type hand_cell_offset: tuple
        :returns: None
        :rtype: None
        :raises TypeError: Если `hand_cell_offset` не является кортежем с двумя числовыми значениями (int или float).

        '''
        for hand_cell in self.__all_hand_cells:
            hand_cell.rect.x += hand_cell_offset[0]
            hand_cell.rect.y += hand_cell_offset[1]
        self.__all_hand_cells.draw(self.__screen)


    def __draw_all_signs(self):
        '''
        Обновляет отображение всех объектов на экране, рисуя клетки и знаки, а затем обновляя экран.

        Этот метод рисует все клетки и знаки на экране с использованием групп спрайтов, 
        а затем обновляет отображение с помощью `pg.display.update()`, чтобы изменения стали видимыми.

        :param: Нет параметров.
        :returns: None
        :rtype: None
        :raises TypeError: Если `self.__all_hand_cells` или `self.__all_signs` не являются правильными объектами `pg.sprite.Group`.
        
        Метод рисует все элементы в группах `self.__all_hand_cells` и `self.__all_signs` на экране (`self.__screen`) и 
        обновляет экран с помощью `pg.display.update()`.
        '''
        self.__setup_board()
        self.__all_signs.draw(self.__screen)


    def __setup_board(self):
        '''
        Инициализирует и настраивает игровое поле, создавая знаки для каждой ячейки,
        если значение в таблице отличается от нуля, и размещая их на соответствующих ячейках.

        Метод проходит по всем строкам таблицы `__hand_table`, создает знаки для ненулевых значений
        и добавляет их в коллекцию `__all_signs`. Затем для каждого знака определяется
        его положение на поле, основываясь на совпадении имени поля с ячейкой в `__all_hand_cells`.

        :returns: None
        :rtype: None
        :raises TypeError: Если `__hand_table` или `__all_hand_cells` имеют неправильный тип данных.
        
        '''
        for j, row in enumerate(self.__hand_table):
            for i, field_value in enumerate(row):
                if field_value != 0:
                    sign = self.__create_sign(field_value, (j,i))
                    self.__all_signs.add(sign)
        for sign in self.__all_signs:
            for hand_cell in self.__all_hand_cells:
                if sign.field_name == hand_cell.field_name:
                    sign.rect = hand_cell.rect.copy()
    

    def __create_sign(self, sign_symbol: str, table_coord: tuple):
        '''
        Создает объект знака (например, фигуру на игровом поле) на основе символа и координат в таблице.

        Метод принимает символ знака и его координаты на игровом поле, затем находит соответствующий 
        тип знака, использует его для создания экземпляра класса знака и возвращает его.

        :param sign_symbol: Символ, представляющий тип знака, например, 'X' или 'O'.
        :type sign_symbol: str
        :param table_coord: Координаты (строка, столбец) ячейки на поле, где должен быть размещен знак.
        :type table_coord: tuple

        :returns: Экземпляр класса знака, соответствующего типу, определенному `sign_symbol`.
        :rtype: object (например, экземпляр класса Sign_0 или другого типа знака)

        :raises KeyError: Если `sign_symbol` не найден в словаре `__signs_types`.
        :raises TypeError: Если типы переданных параметров некорректны.
        
        '''
        field_name = self.__to_field_name(table_coord)
        sign_tuple = self.__signs_types[sign_symbol]
        classname = globals()[sign_tuple[0]]
        return classname(self.__size, sign_tuple[1], field_name)


    def __to_field_name(self, table_coord: tuple):
        '''
        Находит клетку, в которую попадает указатель мыши, на основе координат.

        Метод проверяет каждую клетку в коллекции `__all_hand_cells` и возвращает клетку,
        чье прямоугольное ограничение (`rect`) содержит точку, заданную координатами `position`.

        :param position: Координаты (x, y) точки на экране, где проверяется наличие клетки.
        :type position: tuple

        :returns: Клетка, в которую попадает точка. Если клетка не найдена, возвращается None.
        :rtype: object (клетка из коллекции `__all_hand_cells` или None)

        :raises TypeError: Если `position` не является кортежем из двух чисел (x, y).
        
        '''
        return 'H' + str(self.__hand_count_lines - table_coord[0]) + str(self.__hand_count_elements - table_coord[1])

    def __get_hand_cell(self, position:tuple):
        '''
        Находит клетку, в которую попадает указатель мыши, на основе координат.

        Метод проверяет каждую клетку в коллекции `__all_hand_cells` и возвращает клетку,
        чье прямоугольное ограничение (`rect`) содержит точку, заданную координатами `position`.

        :param position: Координаты (x, y) точки на экране, где проверяется наличие клетки.
        :type position: tuple

        :returns: Клетка, в которую попадает точка. Если клетка не найдена, возвращается None.
        :rtype: object (клетка из коллекции `__all_hand_cells` или None)

        :raises TypeError: Если `position` не является кортежем из двух чисел (x, y).
        
        '''
        for hand_cell in self.__all_hand_cells:
            if hand_cell.rect.collidepoint(position):
                return hand_cell
        return None

    
    def btn_down(self, button_type: int, position: tuple):
        '''
        Обрабатывает событие нажатия кнопки мыши. Сохраняет клетку, на которой произошло нажатие.

        Когда кнопка мыши нажата, метод сохраняет клетку, над которой находится курсор, в 
        переменной `__pressed_hand_cell`. Это позволяет отслеживать, на какой клетке 
        было сделано нажатие для последующих операций.

        :param button_type: Тип кнопки мыши, которая была нажата. Например, 1 — это левая кнопка.
        :type button_type: int
        :param position: Координаты (x, y) точки на экране, где была нажата кнопка.
        :type position: tuple

        :returns: None
        :rtype: None
        :raises TypeError: Если переданные параметры имеют неправильный тип или если `position` 
                        не является кортежем с двумя числами.
        
        '''
        self.__pressed_hand_cell = self.__get_hand_cell(position)


    
    def btn_up(self, button_type: int, position:tuple):
        '''
        Обрабатывает событие отпускания кнопки мыши на экране. В зависимости от типа кнопки 
        и выбранной клетки, выполняет определенные действия, такие как выбор или перемещение знака.

        Если кнопка мыши была отпущена над выбранной клеткой, и если тип кнопки соответствует 
        правой кнопке мыши (button_type == 1), метод пытается выбрать знак для перемещения 
        или обновления его позиции.

        :param button_type: Тип кнопки мыши, которая была отпущена. Например, 1 — это левая кнопка.
        :type button_type: int
        :param position: Координаты (x, y) точки на экране, где была отпущена кнопка.
        :type position: tuple

        :returns: None
        :rtype: None
        :raises TypeError: Если переданные параметры имеют неправильный тип или если 
                        `released_hand_cell` не поддерживает нужные методы.
        
        '''
        released_hand_cell = self.__get_hand_cell(position)
        if (released_hand_cell is not None) and (released_hand_cell == self.__pressed_hand_cell):
            if button_type == 1:
                self.__pick_hand_cell(released_hand_cell)
        self.__grand_update()

    def __pick_hand_cell(self,hand_cell):
        '''
        Обрабатывает выбор клетки для знака. Если знак ещё не выбран, то метод выбирает знак для перемещения.
        Если знак уже выбран, он перемещается в новую клетку.

        Метод проверяет, выбран ли уже какой-либо знак. Если знак ещё не выбран, он ищет знак, 
        чье поле совпадает с полем клетки (`hand_cell`) и выбирает его. Если знак уже выбран, 
        его позиция обновляется на основе клетки, и выбор сбрасывается.

        :param hand_cell: Клетка, с которой взаимодействует пользователь.
        :type hand_cell: object (предполагается, что объект клетки имеет атрибуты `rect` и `field_name`)

        :returns: None
        :rtype: None
        :raises TypeError: Если параметр `hand_cell` не имеет необходимых атрибутов (`rect`, `field_name`).
        
        '''
        if self.__picked_hand_sign is None:
            for sign in self.__all_signs:
                if sign.field_name == hand_cell.field_name:
                    self.__picked_hand_sign = sign
                    break
        else:
            self.__picked_hand_sign.rect=hand_cell.rect
            self.__picked_hand_sign.field__name = hand_cell.field_name
            self.__picked_hand_sign = None

    def __grand_update(self):
        '''
        Обновляет экран, рисуя все клетки и знаки на поле, а затем обновляет отображение.

        Метод вызывает метод `draw` для всех клеток и знаков, которые находятся в коллекциях `__all_hand_cells` и `__all_signs`,
        соответственно. После этого обновляется экран, чтобы отобразить все изменения.

        :returns: None
        :rtype: None
        :raises TypeError: Если объекты в `__all_hand_cells` или `__all_signs` не поддерживают метод `draw` или имеют некорректный тип.
        
        '''
        self.__all_hand_cells.draw(self.__screen)
        self.__all_signs.draw(self.__screen)
        pg.display.update()




class Cell(pg.sprite.Sprite):
    def __init__(self, color_index: int, size: int, coords: tuple, name: str):
        '''
        Инициализирует объект клетки игрового поля с заданными параметрами.

        :param color_index: Индекс цвета клетки, который используется для выбора соответствующего изображения.
        :type color_index: int
        :param size: Размер клетки (ширина и высота) в пикселях.
        :type size: int
        :param coords: Координаты клетки в виде кортежа (x, y), которые указывают на позицию клетки на поле.
        :type coords: tuple
        :param name: Название или идентификатор поля, к которому принадлежит клетка.
        :type name: str
        :returns: None
        :rtype: None
        :raises TypeError: Если один из параметров имеет неправильный тип (например, если `coords` не является кортежем или `color_index` не является целым числом).

        Конструктор создает клетку, загружает соответствующее изображение на основе индекса цвета,
        масштабирует его до указанного размера и позиционирует клетку на игровом поле по заданным координатам.
        
        '''
        super().__init__()
        x,y = coords
        self.color = color_index
        self.field_name = name
        self.image = pg.image.load(Img_path+image[color_index])
        self.image = pg.transform.scale(self.image, (size, size))
        self.rect = pg.Rect(x * size, y * size, size, size)



