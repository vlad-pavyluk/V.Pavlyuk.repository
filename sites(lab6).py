import requests
from bs4 import BeautifulSoup as BS
import sys
import string
import re


max_page = 4
pages = []
frequency = {}
lines = 0
words = 0
letters = 0

print('Добрий день! Чи хочете ви відкрити один сайт і дізнатися про нього трошки більше?')
a = input()
if a != "Ні":
	print("На жаль,зараз в нас є тільки один сайт: 'stopgame'\n Можливо ви про нього чули,він зв'язаний з комп'ютерними іграми")
	print("Вам підходить?")
	b = input()
	if b != "Ні":
		print("Зараз надамо вам список найкращих ігор")

		r = requests.get('https://stopgame.ru/review/new/stopchoice')
		html = BS(r.content, 'html.parser')

		for x in range(1, max_page +1):
			pages.append(requests.get('https://stopgame.ru/review/new/stopchoice' + str(x)))

		for r in pages:
			html = BS(r.content, 'html.parser')

			for el in html.select('.item'):
				title = el.select('.caption > a')
				if title != []:
					print(title[0].text)
	else:
		print('Тоді допобачення!')				
else:
	print('Ну тоді допобачення!')


print("Ми можемо надати вам більш детальну інформацію: кількість слів,рядків та букв")
c = input("Чи хочете ви дізнатися?\n")
if c != "Ні":
	print("Один момент!")

	for line in requests.get('https://stopgame.ru/review/new/stopchoice'):
		lines += 1
		letters += len(line)


		pos = 'out'
		for letter in line:
			if letter != ' ' and pos == 'out':
				words += 1
				pos = 'in'
			elif letter == ' ':
				pos == 'out'


	print("Кількість рядків:", lines)
	print("Кількість слів:", words)
	print("Кількість букв:", letters)

else: 
	print("Ну тоді добре,допобачення!")

print('Також ми можемо вам html-теги,але,на мою думку,це не для слабонервних')
print('(Я не рекомендую цього робити?)')
d = input("Бажаєте?\n")
if d != "Ні":
	r.text [: 10]
	print(r.text)
	print('Ви зробили велику помилку')
	print("Допобачення!")
else:
	print("Ви не зробили цієї великої помилки,вітаю!")
	print('А тепер допобачення!')




