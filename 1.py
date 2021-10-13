def swap_words(string):
    # Формируем список из слов строки
    lst = string.split(' ')
    # Меняем порядок слов на обратный
    lst.reverse()
    # Соединяем слова в предложение через пробелы и возвращаем полученное значение
    return ' '.join(lst)


if __name__ == '__main__':
    print(swap_words('идет снег'))
    print(swap_words('лето наступило'))