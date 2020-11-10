import sys
import collections
import re
import string
 
lines = 0
words = 0
letters = 0
frequency = {}


print('Ви хотіли дізнатися скільки слів в вашій улюбленій книзі?')
a = input()
if a != "Ні":
	b = input('Але,на жаль,у нас тільки "Зелена миля",підійде?\n')
	if b != "Ні":
		print('Ну тоді почнемо')
else:
	"Ну тоді допобачення"

for line in open('text.txt',encoding = "utf-8"):
    lines += 1
    letters += len(line)
 
    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'
 
print("Кількість рядків:", lines)
print("Кількість слів:", words)
print("Кількість букв:", letters)

c = input("Ви хочете дізнатися кількість уникальних слів та як часто вони зустрічаються?\n")
if c != "Ні":
	print('Зараз надамо')
else:
	print('Якщо ні,то допобачення')

document_text = open('text.txt', 'r',encoding = 'utf-8')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    print (words, frequency[words])
print('Тут немає таких слів як "з","і","ні","а",а є тільки унікальні слова')
print("Дуже дивно,що в україському всі уникальні слова на англійській")
print("І дуже прикро,що тут немає слів,які зустрічаються тільки один раз")
print("Вибачте,але на цьому функціонал нашої програми закінчується.Дякую,допобачення!")