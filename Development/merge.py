def merge_sort_by_x(s):
    '''
    Сортирует список элементов по значению x-координаты с использованием сортировки слиянием (merge sort).

    :param s: Список элементов, где каждый элемент является кортежем в формате (x, y, символ).
    :type s: list

    :returns: Отсортированный по возрастанию x-координат список элементов.
    :rtype: list

    :raises ValueError: Если входные данные неправильного формата.
    '''
    
    if len(s) < 2: return s
    
    middle=len(s) // 2
    left_block=s[:middle]
    right_block=s[middle:]
    
    merge_sort_by_x(left_block)
    merge_sort_by_x(right_block)
    
    ind_left=ind_right=ind_final=0
    
    while ind_left < len(left_block) and ind_right < len(right_block):
        if left_block[ind_left][0] > right_block[ind_right][0]:
            s[ind_final]=right_block[ind_right]
            ind_right+=1
        else:
            s[ind_final]=left_block[ind_left]
            ind_left+=1  
        ind_final+=1
        
    while ind_right < len(right_block):
        s[ind_final]=right_block[ind_right]
        ind_final+=1
        ind_right+=1
        
    while ind_left < len(left_block):
        s[ind_final]=left_block[ind_left]
        ind_final+=1
        ind_left+=1
        
    return s



def merge_sort_by_y(s):
    '''
    Сортирует список элементов по значению y-координаты с использованием сортировки слиянием (merge sort).

    :param s: Список элементов, где каждый элемент является кортежем в формате (x, y, символ).
    :type s: list

    :returns: Отсортированный по возрастанию y-координат список элементов.
    :rtype: list

    :raises ValueError: Если входные данные неправильного формата.
    '''
    if len(s) < 2: return s
    
    middle=len(s)//2
    left_block=s[:middle]
    right_block=s[middle:]
    
    merge_sort_by_y(left_block)
    merge_sort_by_y(right_block)
    
    ind_left=ind_right=ind_final=0
    
    while ind_left < len(left_block) and ind_right < len(right_block):
        if left_block[ind_left][1] > right_block[ind_right][1]:
            s[ind_final]=right_block[ind_right]
            ind_right+=1
        else:
            s[ind_final]=left_block[ind_left]
            ind_left+=1  
        ind_final+=1
        
    while ind_right < len(right_block):
        s[ind_final]=right_block[ind_right]
        ind_final+=1
        ind_right+=1
        
    while ind_left < len(left_block):
        s[ind_final]=left_block[ind_left]
        ind_final+=1
        ind_left+=1
        
    return s

