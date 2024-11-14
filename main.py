#Написать программу, которая:
#- Запрашивает у пользователя количество строк. (*должно быть проверка*)
#- Затем сами строки.
#- Определяет, сколько различных слов содержится в этом тексте, и выводит из количество
#   *Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.*
kolvo_strok=int(input("Введите число строк: "))
if kolvo_strok <=0 : #Проверяем условие
    print("Ошибка") #Вывод ошибки
strings=[] #Создаем список
for i in range(kolvo_strok): #Цикл для повторения количества строк
    string=str(input("Введите строку: ")) #Запрашиваем строки
    strings.append(string) #Добавляем в список
words=[] #Создаем список
for string in strings: #Перебираем строки в списке
     word = string.split() #Разделяем строки по разделителю
     for i in word: #Перебираем элементы в word
        if i not in words: #Если элемента нет в списке для различных слов
            words.append(i) #Добавляем элемент в список
a = len(words) #Длина списка
print("Количество слов: ", a) #Выводим количество