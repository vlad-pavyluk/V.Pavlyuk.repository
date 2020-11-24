import math

class Library():
	def __init__(self,name,author,year,genre):
		self.name = name
		self.author = author
		self.year = year
		self.genre = genre

book_1 = Library('Ми','Євгєній Замятін','1920 рік','Антиутопія')
book_2 = Library('Квіти для Елджернона','Деніел Кіз','1959 рік','Фантастика')
book_3 = Library('Таємнича історія Біллі Мілігана','Деніел Кіз','1981 рік','Документальний роман')
book_4 = Library('Механічний Апельсин','Ентоні Берджес','1962 рік','Антиутопія')
book_5 = Library('Список Шиндлера','Томас Кініллі','1982 рік','Біографічний роман')
book_6 = Library('Ніч у Лісабоні','Еріх Марія Ремарк','1962 рік','Роман')
book_7 = Library('Зелена миля','Стівен Кінг','1996 рік','Фантастика')
book_8 = Library('О дивний новий світ','Олдос Хакслі','1932 рік','Антиутопія')
book_9 = Library('11/22/63','Стівен Кінг','2011 рік','Альтернативна історія')

b1 = input("Ви хочете дізнатися про нашу бібліотеку?\n")

if b1 != "Ні":
	print("Наша біблотека налічує 9 книжок")
	a = input("Ви хочете дізнатися більше?\n")
else:
	print('Ну тоді допобачення!')
if a != 'Ні':
	print('Зараз надамо вам наш список')
	print('Зразу хочу зазначити,що це моя домашня бібліотека,і ми не можемо її змінити')
	print(book_1.name)
	print(book_2.name)
	print(book_3.name)
	print(book_4.name)
	print(book_5.name)
	print(book_6.name)
	print(book_7.name)
	print(book_8.name)
	print(book_9.name)
	while True:
		b = input('Що вам саме цікаво дізнатися?\n')
		if b == 'Жанри':
			print('Зараз ми вам покажемо!')
			print(book_1.name + ' - ' + (book_1.genre))
			print(book_2.name + ' - ' + (book_2.genre))
			print(book_3.name + ' - ' + (book_3.genre))
			print(book_4.name + ' - ' + (book_4.genre))
			print(book_5.name + ' - ' + (book_5.genre))
			print(book_6.name + ' - ' + (book_6.genre))
			print(book_7.name + ' - ' + (book_7.genre))
			print(book_8.name + ' - ' + (book_8.genre))
			print(book_9.name+  ' - ' + (book_9.genre))
		elif b == 'Автори':
			print('Зараз ми вам покажемо!')
			print(book_1.name + ' - ' + (book_1.author))
			print(book_2.name + ' - ' + (book_2.author))
			print(book_3.name + ' - ' + (book_3.author))
			print(book_4.name + ' - ' + (book_4.author))
			print(book_5.name + ' - ' + (book_5.author))
			print(book_6.name + ' - ' + (book_6.author))
			print(book_7.name + ' - ' + (book_7.author))
			print(book_8.name + ' - ' + (book_8.author))
			print(book_9.name+  ' - ' + (book_9.author))
		else:
			print('Зараз ми вам покажемо!')
			print(book_1.name + ' - ' + (book_1.year))
			print(book_2.name + ' - ' + (book_2.year))
			print(book_3.name + ' - ' + (book_3.year))
			print(book_4.name + ' - ' + (book_4.year))
			print(book_5.name + ' - ' + (book_5.year))
			print(book_6.name + ' - ' + (book_6.year))
			print(book_7.name + ' - ' + (book_7.year))
			print(book_8.name + ' - ' + (book_8.year))
			print(book_9.name+  ' - ' + (book_9.year))
			break

else:
	print('Ну тоді допобачення!')

c = input('Можливо ви хочете знайти книгу за списком від 1 до 9?\n')
if c != "Ні":
	cb = input('Ну тоді введіть цифру від 1 до 9\n')
	while True:
		cc = input('Введіть ще,якщо бажайте\n')
		if cc == "1":
			print(book_1.name)
		elif cc == "2":
			print(book_2.name)
		elif cc == "3":
			print(book_3.name)
		elif cc == "4":
			print(book_4.name)
		elif cc == "5":
			print(book_5.name)
		elif cc == "6":
			print(book_6.name)
		elif cc == "7":
			print(book_7.name)
		elif cc == "8":
			print(book_8.name)
		elif cc == "9":
			print(book_9.name)
		else:
			print('Ну тоді добре!')
			break
else:
	print("Ну тоді допобачення!")


print('Ви вже все про них бачили')
print('На жаль,на цьому функціонал нашої програми закінчується,дякую за увагу!')


def main():
	return 0
if __name__ == '__main__':
     main()