import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Функция угадывания числа, гарантированно отгадывает число за 7 попыток.
       Алгоритм угадывания основан на методе дихотомии (половинного деления).
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Cчётчик попыток и предполагаемое число
    count, predict = 1, 50 
    # Верхняя и нижняя граница угадывания
    upper_border, lower_border = 101, 0 
    
    while number != predict:
        count += 1     
        if number > predict:
            lower_border = predict
            predict += (upper_border - predict) // 2
        elif number < predict:
            upper_border = predict
            predict -= (predict - lower_border) // 2

    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict (function): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # Фиксируем сид для воспроизводимости
    np.random.seed(1)  
    # Загадали список чисел
    random_array = np.random.randint(1, 101, size=(10000))  

    # Угадываем каждое число из списка
    for number in random_array: 
        count_ls.append(random_predict(number))
    
    # Среднее, максимальное и минимальное число попыток 
    score = int(np.mean(count_ls)) 
    max_score = int(max(count_ls)) 
    min_score = int(min(count_ls)) 
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток, максимальное кол-во попыток: {max_score}, минимальное количество попыток: {min_score}")
    #return score
  
    
if __name__ == '__main__':
    score_game(game_core_v3)