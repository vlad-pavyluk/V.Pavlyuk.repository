

print('Ви можете дізнатися середній бал наших студентів')

b = ['Цегельник','Хорольський','Форбз','Томулець','Степаненко','Сокрут','Павлюк','Мельник']
c = ['Сиропятов','Романенко','Максименко','Крупка','Костюк']
d = ['Рибак','Німченко']
Z = open('zege.txt')
H = open('horo.txt')
F = open('forbz.txt')
T = open('tomu.txt')
S = open('stepane.txt')
So = open('sokrut.txt')
P = open('pavl.txt')
M = open('meln.txt')
Sy = open('syro.txt')
Ro = open('romane.txt')
Ma = open('maksy.txt')
Kr = open('kru.txt')
Ko = open('kost.txt')
Ry = open('rybak.txt')
Ni = open('nimch.txt')

G = input('Ви хочете дізнатися?\n')
if G== 'Так':
	print('У нас є база данних,яка має три рівня,оберіть один з них: "a","b","c"')
	a = input()
	A = print ('Зараз надамо вам список') if a == 'a' else 'b'
	print (A)
if a == 'a':
	print (b)
	f = input('Про кого вам цікаво дізнатися?\n')
	if f == 'Цегельник':
		print('Зараз надамо вам файл')
		print(Z.read())
		Z.close()
		qw = input('Хочете подивитися ще когось?')
		if qw == "Так":
			qe == input('Кого саме?')
			if qe == 'Хорольський':
				print('Зараз надамо вам файл')
				print(H.read())
				H.close()
			elif qe == 'Форбз':
				print('Зараз надамо вам файл')
				print(F.read())
				F.close()
			elif qe == 'Томулець':
				print('Зараз надамо вам файл')
				print(T.read())
				T.close()
			elif qe == 'Степаненко':
				print('Зараз надамо вам файл')
				print(S.read())
				S.close()
			elif qe == 'Сокрут':
				print('Зараз надамо вам файл')
				print(So.read())
				So.close()		
			elif qe == 'Павлюк':
				print('Зараз надамо вам файл')
				print(P.read())
				P.close()
			else:
				print('Зараз надамо вам файл')
				print(M.read())
				M.close()
			print('Вибачте,ви не можете подивитись більше 2')
			print('Допобачення')



	elif f == 'Хорольський':
		print('Зараз надамо вам файл')
		print(H.read())
		H.close()
		qr = input('Хочете подивитися ще когось?')
		if qr == "Так":
			qy = input('Кого саме?')
			if qy == 'Цегельник':
				print('Зараз надамо вам файл')
				print(Z.read())
				Z.close()
			elif qu == 'Форбз':
				print('Зараз надамо вам файл')
				print(F.read())
				F.close()
			elif qu == 'Томулець':
				print('Зараз надамо вам файл')
				print(T.read())
				T.close()
			elif qu == 'Степаненко':
				print('Зараз надамо вам файл')
				print(S.read())	
			elif qu == 'Сокрут':
				print('Зараз надамо вам файл')
				print(So.read())
				So.close()
			elif qu == 'Павлюк':
				print('Зараз надамо вам файл')
				print(P.read())
				P.close()
			else:
				print('Зараз надамо вам файл')
				print(M.read())
				M.close()		
			print('Вибачте,ви не можете подивитись більше 2')
			print('Допобачення')

	elif f == 'Форбз':
		print('Зараз надамо вам файл')
		print(F.read())
		F.close()
		qi = input('Хочете подивитися ще когось?')
		if qi == "Так":
			qo = input('Кого саме?')
			if qo == 'Цегельник':
				print('Зараз надамо вам файл')
				print(Z.read())
				Z.close()
			elif qo == 'Хорольський':
				print('Зараз надамо вам файл')
				print(H.read())
				H.close()
			elif qo == 'Томулець':
				print('Зараз надамо вам файл')
				print(T.read())
				T.close()
			elif qo == 'Степаненко':
				print('Зараз надамо вам файл')
				print(S.read())
				S.close()
			elif qo == 'Сокрут':
				print('Зараз надамо вам файл')
				print(So.read())
				So.close()
			elif qo == 'Павлюк':
				print('Зараз надамо вам файл')
				print(P.read())
				P.close()
			else:
				print('Зараз надамо вам файл')
				print(M.read())
				M.close()		
			print('Вибачте,ви не можете подивитись більше 2')
			print('Допобачення')


	elif f == 'Томулець':
		print('Зараз надамо вам файл')
		print(T.read())
		T.close()
		QW = input('Хочете подивитися ще когось?')
		if QW == "Так":
			QE = input('Кого саме?')
			if QE == 'Цегельник':
				print('Зараз надамо вам файл')
				print(Z.read())
				Z.close()
			elif QE == 'Хорольський':
				print('Зараз надамо вам файл')
				print(H.read())
				H.close()
			elif QE == 'Форбз':
				print('Зараз надамо вам файл')
				print(F.read())
				F.close()
			elif QE == 'Степаненко':
				print('Зараз надамо вам файл')
				print(S.read())
				S.close()
			elif QE == 'Сокрут':
				print('Зараз надамо вам файл')
				print(So.read())
				So.close()
			elif QE == "Павлюк":
				print('Зараз надамо вам файл')
				print(P.read())
				P.close()
			elif QE == "Павлюк":
				print('Зараз надамо вам файл')
				print(P.read())
				P.close()
			else:
				print('Зараз надамо вам файл')
				print(M.read())
				M.close()
			print('Вибачте,ви не можете подивитись більше 2')
			print('Допобачення')
	elif f == 'Степаненко':
		print('Зараз надамо вам файл')
		print(S.read())
		S.close()
		QR = input('Хочете подивитися ще когось?')
		if QК == "Так":
			QT = input('Кого саме?')
			if QT == 'Цегельник':
				print('Зараз надамо вам файл')
				print(Z.read())
				Z.close()
			elif QT == 'Хорольський':
				print('Зараз надамо вам файл')
				print(H.read())
				H.close()
			elif QT == 'Форбз':
				print('Зараз надамо вам файл')
				print(F.read())
				F.close()
			elif QT == 'Томулець':
				print('Зараз надамо вам файл')
				print(T.read())
				T.close()
			elif QT == 'Сокрут':
				print('Зараз надамо вам файл')
				print(So.read())
				So.close()
			elif QT == "Павлюк":
				print('Зараз надамо вам файл')
				print(P.read())
				P.close()
			else:
				print('Зараз надамо вам файл')
				print(M.read())
				M.close()		
			print('Вибачте,ви не можете подивитись більше 2')
			print('Допобачення')
	
					
	elif f == 'Сокрут':
		print('Зараз надамо вам файл')
		print(So.read())
		So.close()
		QY = input('Хочете подивитися ще когось?')
		if QY == "Так":
			QU = input('Кого саме?')
			if QU == 'Цегельник':
				print('Зараз надамо вам файл')
				print(Z.read())
				Z.close()
			elif QU == 'Хорольський':
				print('Зараз надамо вам файл')
				print(H.read())
				H.close()
			elif QU == 'Форбз':
				print('Зараз надамо вам файл')
				print(F.read())
				F.close()
			elif f == 'Степаненко':
				print('Зараз надамо вам файл')
				print(S.read())
				S.close()
			elif QU == "Павлюк":
				print('Зараз надамо вам файл')
				print(P.read())
				P.close()
			else:
				print('Зараз надамо вам файл')
				print(M.read())
				M.close()		
			print('Вибачте,ви не можете подивитись більше 2')
			print('Допобачення')


	elif f == "Павлюк":
		print('Зараз надамо вам файл')
		print(P.read())
		P.close()
		QI = input('Хочете подивитися ще когось?')
		if QO == "Так":
			QO = input('Кого саме?')
			if QO == 'Цегельник':
				print('Зараз надамо вам файл')
				print(Z.read())
				Z.close()
			elif QO == 'Хорольський':
				print('Зараз надамо вам файл')
				print(H.read())
				H.close()
			elif QO == 'Форбз':
				print('Зараз надамо вам файл')
				print(F.read())
				F.close()	
			elif QO == 'Томулець':
				print('Зараз надамо вам файл')
				print(T.read())
				T.close()
			elif QO == 'Степаненко':
				print('Зараз надамо вам файл')
				print(S.read())
				S.close()
			elif QO == 'Сокрут':
				print('Зараз надамо вам файл')
				print(So.read())
				So.close()
			else:
				print('Зараз надамо вам файл')
				print(M.read())
				M.close()		
			print('Вибачте,ви не можете подивитись більше 2')
			print('Допобачення')
	
	else:
		print('Зараз надамо вам файл')
		print(M.read())
		M.close()		
		qa = input('Хочете подивитися ще когось?')
		if qa == "Так":
			qs = input('Кого саме?')
			if qs == 'Цегельник':
				print('Зараз надамо вам файл')
				print(Z.read())
				Z.close()	
			elif qs == 'Хорольський':
				print('Зараз надамо вам файл')
				print(H.read())
				H.close()
			elif qs == 'Форбз':
				print('Зараз надамо вам файл')
				print(F.read())
				F.close()	
			elif qs == 'Томулець':
				print('Зараз надамо вам файл')
				print(T.read())
				T.close()	
			elif qs == 'Степаненко':
				print('Зараз надамо вам файл')
				print(S.read())
				S.close()
			elif qs == 'Сокрут':
				print('Зараз надамо вам файл')
				print(So.read())
				So.close()
			elif qs == "Павлюк":
				print('Зараз надамо вам файл')
				print(P.read())
				P.close()
			print('Вибачте,ви не можете подивитись більше 2')
			print('Допобачення')		



elif a == 'b':
	print (c)
	while True:
	  zx = input('Про кого вам цікаво дізнатися?\n')
	  if zx == "Сиропятов":
	  	print('Зараз надамо вам файл')
	  	current = b.pop()
	  	print(Sy.read())
	  	Sy.close()
	  elif zx == 'Романенко':
	  	print('Зараз надамо вам файл')
	  	print(Ro.read())
	  	Ro.close()
	  elif zx == 'Максименко':
	  	print('Зараз надамо вам файл')
	  	print(Ma.read())
	  	Ma.close()
	  elif zx == 'Крупка':
	  	print('Зараз надамо вам файл')
	  	print(Kr.read())
	  	Kr.close()
	  else:
	  	print('Зараз надамо вам файл')
	  	print(Ko.read())
	  	Ko.close()
	  	print("Дякую за увагу!")
	  	break
	  	
else:
	while True:
		xc = input('Про кого вам цікаво дізнатися?\n')
		if xc == "Рибак":
			print('Зараз надамо вам файл')
			print(Ry.read())
			Ry.close()
		elif xc == "Німченко":
			print('Зараз надамо вам файл')
			print(Ni.read())
			Ni.close()
			print("Дякую за увагу!")
			break








