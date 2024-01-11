import sys
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QTimer, QTime
per = None
time_a = ""
tx = None
class Final_win(QWidget):
    def __init__(self):
        super().__init__()
        calculations = (int(tx.hz.text()) +int(tx.pere_1.text())+int(tx.pere_2.text())-200)/10
        self.result = QLabel('Индекс Руфье:'+str(calculations))
        if int(tx.iii.text()) >= 15:
            if calculations>=15:
                res = 'низкий'
            if 11<=calculations<=14.9:
                res = 'удовлетворительный'
            if 6<=calculations<=10.9:
                res = 'средний'
            if 0.5<=calculations<=5.9:
                res = 'выше среднего'
            if 0.4>=calculations:
                res = 'высокий'
        if  tx.iii.text() == '12' or tx.iii.text() == '11' :
            if calculations>=18:
                res = 'низкий'
            if 14<=calculations<=17.9:
                res = 'удовлетворительный'
            if 9<=calculations<=13.9:
                res = 'средний'
            if 3.5<=calculations<=8.9:
                res = 'выше среднего'
            if 3.4>=calculations:
                res = 'высокий'        
        if tx.iii.text() == '13' or tx.iii.text() == '14':
            if calculations>=16.5:
                res = 'низкий'
            if 12.5<=calculations<=16.4:
                res = 'удовлетворительный'
            if 6.5<=calculations<=12.4:
                res = 'средний'
            if 2<=calculations<=7.4:
                res = 'выше среднего'
            if 1.9>=calculations:
                res = 'высокий'
        if tx.iii.text() == '7' or tx.iii.text() == '8':
            if calculations>=21:
                res = 'низкий'
            if 17<=calculations<=20.9:
                res = 'удовлетворительный'
            if 12<=calculations<=16.9:
                res = 'средний'
            if 6.5<=calculations<=11.9:
                res = 'выше среднего'
            if 6.4>=calculations:
                res = 'высокий'                                                
        self.recomendation = QLabel("Работоспособность cердца:"+res)
        self.pol = QVBoxLayout()
        self.pol.addWidget(self.result, alignment=Qt.AlignCenter)
        self.pol.addWidget(self.recomendation, alignment=Qt.AlignCenter)
        self.setLayout(self.pol)

class TestWin(QWidget):
    def __init__(self, ):
        super().__init__()
        self.timer = QTimer()
        self.v_2 =QVBoxLayout()
        self.time = QTime(0,0,15)
        self.vremya = QLabel(self.time.toString("hh:mm:ss"))
        self.fio = QLabel('Введите Ф.И.О.:')
        self.imya = QLineEdit()
        self.imya.setPlaceholderText('Ф.И.О.')
        self.perem_1 = self.imya.text()
        self.polet = QLabel('Полных лет:')
        self.iii = QLineEdit()
        self.iii.setPlaceholderText('0')
        self.txt_text1 = QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\nРезультат запишите в соответствующее поле.')
        self.start = QPushButton('Начать первый тест')
        self.hz = QLineEdit()
        self.hz.setPlaceholderText('0')
        self.presed = QLabel('Выполните 30 пресеаний за 45 секунд. Для этого нажмите кнопку "Начать делать преседания",\n чтобы запустить счётчик преседаний "')
        self.nachat = QPushButton('Начать делать преседания')
        self.nachat.setEnabled(False)
        self.iiii = QPushButton('Начать финальный тест')
        self.iiii.setEnabled(False)
        self.kod = QHBoxLayout()
        self.timer.timeout.connect(self.func)
        self.pere_1 = QLineEdit()
        self.pere_1.setPlaceholderText('0')
        self.pere_2 = QLineEdit()
        self.pere_2.setPlaceholderText('0')
        self.perehod = QPushButton('Перейти на следущую страницу')
        self.v_2.addWidget(self.fio, alignment=Qt.AlignLeft)
        self.v_2.addWidget(self.imya, alignment=Qt.AlignLeft)
        self.v_2.addWidget(self.polet, alignment=Qt.AlignLeft)
        self.v_2.addWidget(self.iii, alignment=Qt.AlignLeft)
        self.v_2.addWidget(self.txt_text1, alignment=Qt.AlignLeft)
        self.v_2.addWidget(self.start, alignment=Qt.AlignLeft)
        self.v_2.addWidget(self.hz, alignment=Qt.AlignLeft)
        self.v_2.addLayout(self.kod)
        self.v_2.addWidget(self.nachat, alignment=Qt.AlignLeft)
       # self.v_2.addWidget(self.lag, alignment=Qt.AlignLeft)
        self.v_2.addWidget(self.iiii, alignment=Qt.AlignLeft)
        self.v_2.addWidget(self.presed, alignment=Qt.AlignLeft)
        self.v_2.addWidget(self.pere_1, alignment=Qt.AlignLeft)
        self.v_2.addWidget(self.pere_2, alignment=Qt.AlignLeft)
        self.v_2.addWidget(self.perehod, alignment=Qt.AlignLeft)
        self.kod.addWidget(self.vremya, alignment=Qt.AlignRight)
        self.start.clicked.connect(self.tuimer_nachat)
        self.nachat.clicked.connect(self.tuimer_nachat_1)
        self.iiii.clicked.connect(self.tuimer_nachat_2)
        self.perehod.clicked.connect(self.func_to_perehod)
        self.setLayout(self.v_2)
    def func_to_perehod(self):
        self.close()
        global per
        per = Final_win()
        per.show()
    def tuimer_nachat(self):
        self.time = QTime(0, 0, 15)
        self.vremya.setText(self.time.toString("hh:mm:ss"))
        self.timer.start(1000)
        self.start.setEnabled(False)
    def tuimer_nachat_1(self):
        self.time = QTime(0, 0, 45)
        self.vremya.setText(self.time.toString("hh:mm:ss"))
        self.timer.start(1000)
        self.start.setEnabled(False)
        self.iiii.setEnabled(True)

    def tuimer_nachat_2(self):
        self.time = QTime(0, 1, 0)
        if self.time == "00:00:45":
            self.vremya.setStyleSheet("color: rgb(0,255,0)")
        self.vremya.setText(self.time.toString("hh:mm:ss"))
        self.timer.start(1000)
        self.start.setEnabled(False)

    def func(self):
        if self.time.toString("hh:mm:ss") == '00:00:00':
            self.timer.stop()  # Stop the timer when time is up
            self.start.setEnabled(True)
            self.nachat.setEnabled(True)
            self.iiii.setEnabled(True)  # Enable the "Начать финальный тест" button
        else:
            self.time = self.time.addSecs(-1)
            self.vremya.setText(self.time.toString("hh:mm:ss"))

class Main_win(QWidget):
    def __init__(self):
        super().__init__()
        self.welc = QLabel('Добро пожаловать в программу по определению состояния здоровья!')
        self.txt_next = QPushButton('Начать')
        self.txt_into = QLabel(
            'Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
            'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
            'У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
            'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
            'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
            'а потом — за последние 15 секунд первой минуты периода восстановления.\n'
            'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
            'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.')
        self.v_v = QVBoxLayout()
        self.v_v.addWidget(self.welc, alignment=Qt.AlignCenter)
        self.v_v.addWidget(self.txt_into, alignment=Qt.AlignCenter)
        self.v_v.addWidget(self.txt_next, alignment=Qt.AlignCenter)
        print(111)
        self.setLayout(self.v_v)
        self.setWindowTitle("Introduction win")
        self.txt_next.clicked.connect(self.pere)
    def pere(self):
        self.hide()
        global tx
        tx = TestWin()
        tx.show()

app = QApplication([])
mw = Main_win()

mw.show()
app.exec_()
