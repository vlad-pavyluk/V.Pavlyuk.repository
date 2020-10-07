#Модуль,який необхідний для обробки вхідних даних#
data = {}
def ReadDataLab():
    """ Ця функція зчитує рядкі з текстового файлу в масив. """
    i = 0
    f = open('data/data.txt', 'r', encoding='UTF-8')
    for line in f:
        data[i] = line
        i += 1
    f.close()
    a = 0
    while a < len(data):
        print(data[a])
        a += 1
    
ReadDataLab()