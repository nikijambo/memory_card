from PyQt5.QtCore import Qt#подключаем модули
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QRadioButton, QGroupBox
from random import shuffle#подключаем модуль рандом
from random import randint

class Question():
    def __init__(
     self, question, right_answer,
     wrong1, wrong2, wrong3):
            self.question = question
            self.right_answer = right_answer
            self.wrong1 = wrong1
            self.wrong2 = wrong2
            self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('')
text = QLabel('Какой национальности не существует?')#создание первого текста
win = QPushButton('Ответить')#создание кнопки ответить

RadioGroupBox = QGroupBox('Варианты ответов')#первая группа

rbtn_1 = QRadioButton('Энцы')#создание кнопки 1
rbtn_2 = QRadioButton('Смурфы')#создание кнопки 2
rbtn_3 = QRadioButton('Чульмцы')#создание кнопки 3
rbtn_4 = QRadioButton('Алеуты')#создание кнопки 4
#линии для группы
layout_ans1 = QHBoxLayout()#создание гориз. линии
layout_ans2 = QVBoxLayout()#создание вертик. линии
layout_ans3 = QVBoxLayout()#создание вертик. линии

layout_ans4 = QHBoxLayout()#линия для текста
layout_ans5 = QHBoxLayout()#линия для группы
layout_ans6 = QHBoxLayout()#линия для кнопки

layout_ans4.addWidget(text,alignment=Qt.AlignCenter)#выравнивание текста
layout_ans5.addWidget(RadioGroupBox)
layout_ans6.addWidget(win,alignment=Qt.AlignCenter)#выравнивание кнопки ответить

layout_ans2.addWidget(rbtn_1)#подключаем вертик линию к первой кнопке
layout_ans2.addWidget(rbtn_2)#подключаем вертик линию к второй кнопке
layout_ans3.addWidget(rbtn_3)#подключаем вертик линию к третьей кнопке
layout_ans3.addWidget(rbtn_4)#подключаем вертик линию к четвертой кнопке
layout_ans1.addLayout(layout_ans2)#подлючаем гориз. линию к вертик.
layout_ans1.addLayout(layout_ans3)#подлючаем гориз. линию к вертик.

RadioGroupBox.setLayout(layout_ans1)#подключаем первую группу к гориз. линии

glav_lin = QVBoxLayout()#создание главной линии
glav_lin.addLayout(layout_ans4)
glav_lin.addLayout(layout_ans5)
glav_lin.addLayout(layout_ans6)
main_win.setLayout(glav_lin)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


RadioGroupBox2 = QGroupBox('Результат теста')#вторая группа
text2 = QLabel('Самый сложный вопрос в мире!')#второй текст
text3 = QLabel('Правильно/Неверно')#третий текст
text4 = QLabel('Правильный ответ')#четвертый текст
win2 = QPushButton('Следующий вопрос')#вторая кнопка
text.setText('Самый сложный вопрос в мире!')#меняем "Какой национальности не существует?" на "Самый сложный вопрос в мире!"
layout_ans7 = QVBoxLayout()#создание седьмой вертикальной линии 

    

def show_question():#обработка всех переключателей
    RadioGroupBox2.hide()
    RadioGroupBox.show()
    win.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result(rez):#cоздание функции show_result
    RadioGroupBox.hide()#скрытие первого окна
    RadioGroupBox2.show()#показать второе окно
    text3.setText(rez)
    win.setText('Следующий вопрос')#меняет надпись на "следующий вопрос"

def start_test():#cоздание функции start_test
    if win.text() == 'Ответить':
        show_result()

    else:
        show_question()

#win.clicked.connect(start_test)#обработчик нажатия на кнопку

q = Question('Государственый язык бразилии', 'Португальский', 'Русский', 'Английский', 'Китайский')

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):#создание функции ask
    shuffle(answers)#перемешиваем кнопки
    answers[0].setText(q.right_answer)#правильный ответ
    answers[1].setText(q.wrong1)#не правильный ответ
    answers[2].setText(q.wrong2)#не правильный ответ
    answers[3].setText(q.wrong3)#не правильный ответ
    text.setText(q.question)
    text4.setText(q.right_answer)
    show_question()
ask(q)


def check_answer():
    if answers[0].isChecked():
        show_result('Правильно')
        main_win.score += 1
    elif answers[1].isChecked:
        show_result('Неверно')
    elif answers[2].isChecked:
        show_result('Неверно')
    elif answers[3].isChecked:
        show_result('Неверно')
    print('Статистика')
    print('-Всего вопросов:', main_win.total)
    print('-Правильных ответов:', main_win.score)
    print('Рейтинг:', main_win.total/main_win.score)


    

#ask('Государственый язык бразилии', 'Португальский', 'Русский', 'Английский', 'Китайский')


questions_list = []
q1 = Question(
    'Государственый язык Бразилии',
'Португальский',
    'Английский', 'Испанский', 'Французский')
questions_list.append(q1)
q2 = Question(
    'Сколько зубов у человека',
'32',
    '48', '50', '25')
questions_list.append(q2)
q3 = Question(
    'Сколько лет Путину',
'70',
    '90', '45', '33')
questions_list.append(q3)
q4 = Question(
    'Какого цвета нету во флаге России',
'Черного',
    'Красного', 'Синего', 'Белого')
questions_list.append(q4)
q5 = Question(
    'Когда была куликовская битва',
'1380',
    '1232', '1460', '1879')
questions_list.append(q5)
q6 = Question(
    'Где было ледовое побоище',
'на Чукодском озере',
    'на озере Байкал', 'на Онежском озере', 'на озере Таймыр')
questions_list.append(q6)
q7 = Question(
    'В какой стране проживает больше всего людей',
'В Китае',
    'В России', 'В Америке', 'В Канаде')



main_win.score = 0
main_win.total = 0


#main_win.cur_question = -1
def next_question():
    main_win.total += 1

    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(questions_list[cur_question])

def click_OK():
    
    if win.text() == 'Ответить':
        check_answer()
    else:
        next_question()
next_question()
layout_ans7.addWidget(text3)#подключаем 7-ю линию к 3-му тексту
layout_ans7.addWidget(text4,alignment=Qt.AlignCenter)#выравниваем текст
RadioGroupBox2.hide()#скрываем 2-ю группу
RadioGroupBox2.setLayout(layout_ans7)
layout_ans5.addWidget(RadioGroupBox2)#подключаем 5-ю линию к 2-й группе
main_win.resize(400, 200)#параметры окна
main_win.show()
win.clicked.connect(click_OK)#обработка кнопки
app.exec_()

