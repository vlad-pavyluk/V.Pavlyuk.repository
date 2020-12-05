import numpy as np

import matplotlib.pyplot as plt
import pylab 
import sys
import collections
import re
import string


lines = 0
words = 0
letters = 0
frequency = {}

print('Добрий день,ми можемо показати вам графік функції "y = 5*sin(10*x)*sin(3*x)","x = [0,4]" ')
a = input("Вас це цікавить?\n")
if a != "Ні":
	print('Графік відкриється в окремому окні та сохраниться під назвою "Figure1"')
	x = np.linspace(0,4,1000	)
	y = np.sin(10*x)*5 * np.sin(3*x)
	plt.plot(x,y)

	plt.show()

	plt.savefig('Figure1.png')
else:
	print('Не будемо вас затримувати!')


print('Ми можемо надати вам декілька команд "Кількість слів","Кількість букв","Кількість рядків" та "Дістаграма"')

for line in open('text1.txt',encoding = "utf-8"):
    lines += 1
    letters += len(line)
 
    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'
document_text = open('text1.txt', 'r',encoding = 'utf-8')
text_string = document_text.read()		
match_pattern = re.findall(r'[a-z]{3,15}'	,text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 


while True:
		xc = input('Введіть команду\n')
		if xc == "Кількість слів":
			print("Кількість слів:",words)
		elif xc == "Кількість букв":
			print("Кількість букв:",letters)
		elif xc == "Кількість рядків":
			print("Кількість рядків:",lines)
		elif xc == "Дістаграма":
			plt.hist(frequency_list, 25) 
			plt.show()
			for words in frequency_list:
    				print (words, frequency[words])
			print("Ви подивилися кількість повторення уникальних слів,і як бачите,вони повторюються по 1 разу")
		else:
			print("У нас немає такої команди")
			break

print("Вашу гістограму збережено у .png файлі")
plt.savefig("gisto1.png")
print("На цьому функціонал нашої програми закінчився,дякую за увагу!")