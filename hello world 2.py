name = input("Привіт,як тебе звати?")
print("Привіт,мене звати",name)
print("У мене є до тебе одне питання,якщо відповідь буде правильною,то ти щось отримаєш")
mission = input("Ти згоден?")
if mission == " Так":
    print('Добре,почнемо')
    question = input("Скільки буде 2+2*2?")
    if question == " 6":
        print("Ти молодець,тримай цукерку")
        print("Все, не буду затримувати")
elif mission == "Ні":
    print('Добре,не буду затримувати')
