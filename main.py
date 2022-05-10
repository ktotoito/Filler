import sys
import sqlite3
from PIL import Image
from PyQt5.QtWidgets import QGraphicsScene, QLabel, \
    QGraphicsRectItem, QGraphicsView, QPushButton, QDialog, QFileDialog
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QBrush, QPixmap, QIcon
from random import choice
import clasAdiolog
import clasBdiolog
import clasCdiolog
import clasDdiolog
import clasEdiolog

win1 = ''
colors = ['blue', 'red', 'yellow', 'magenta', 'cyan', 'green', 'gray']
colors2 = colors[:]
f_colors = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png']
f_colors_2 = f_colors[:]

s = {'player1': 'Игрок 1', 'player2': 'Игрок 2', 'ai': 'Компьютер'}

q_colors_2 = {'blue': Qt.blue, 'red': Qt.red, 'yellow': Qt.yellow, 'magenta': Qt.magenta,
              'cyan': Qt.cyan, 'green': Qt.green, 'gray': Qt.gray, 'white': Qt.white, 'black': Qt.black,
              'darkRed': Qt.darkRed, 'darkGreen': Qt.darkGreen, 'darkBlue': Qt.darkBlue,
              'darkCyan': Qt.darkCyan, 'darkGray': Qt.darkGray, 'darkMagenta': Qt.darkMagenta,
              'darkYellow': Qt.darkYellow, 'lightGray': Qt.lightGray}

SCREEN_SIZE = [830, 545]


class DialogTable(QDialog, clasAdiolog.Ui_Dialog):  # Диалоговое окно "Начать сначала"
    def __init__(self):
        QDialog.__init__(self)

        self.setupUi(self)

        self.buttonBox.accepted.connect(self.accept_data)
        self.buttonBox.rejected.connect(self.reject_data)
        self.data_is_accepted1 = 0

    def accept_data(self):
        self.data_is_accepted1 = 1
        self.close()

    def reject_data(self):
        self.close()


class DialogTable1(QDialog, clasBdiolog.Ui_Dialog1):  # Диалоговое окно настроек файлов
    def __init__(self):
        QDialog.__init__(self)

        self.setupUi(self)
        self.buttons = [self.pushButton_1, self.pushButton_2, self.pushButton_3,
                        self.pushButton_4, self.pushButton_5, self.pushButton_6,
                        self.pushButton_7]
        for v in self.buttons:
            v.clicked.connect(self.run)
        self.buttonBox.accepted.connect(self.accept_data)
        self.buttonBox.rejected.connect(self.reject_data)

        self.QLabels = [self.label_1, self.label_3, self.label_2,
                        self.label_4, self.label_5,
                        self.label_6, self.label_7]
        self.f_colors_3 = f_colors[:]
        self.data_is_accepted = False

        for j in range(7):
            pixmap = QPixmap(f_colors[j])
            self.QLabels[j].resize(20, 20)
            self.QLabels[j].setPixmap(pixmap)

        self.pushButton.clicked.connect(self.run2)

    def accept_data(self):
        global f_colors
        self.data_is_accepted = True
        f_colors = self.f_colors_3
        self.close()

    def reject_data(self):
        self.close()

    def run(self):
        for i in range(7):
            if self.buttons[i] == self.sender():
                fname = QFileDialog.getOpenFileName(
                    self, 'Выбрать картинку', '',
                    'Картинка (*.png);;Картинка (*.jpg);;Все файлы (*)')[0]
                if fname:
                    fname1 = fname.split('/')[-1]

                    self.f_colors_3[i] = fname1
                    a = Image.open(fname)
                    a2 = a.resize((20, 20))
                    a2.save(fname1)

                    pixmap = QPixmap(self.f_colors_3[i])
                    self.QLabels[i].resize(20, 20)
                    self.QLabels[i].setPixmap(pixmap)

    def run2(self):  # Сброс до начальных файлов
        global f_colors, f_colors_2
        f_colors.clear()
        self.f_colors_3.clear()
        f_colors = f_colors_2[:]
        self.f_colors_3 = f_colors[:]
        for i in range(7):
            pixmap = QPixmap(f_colors[i])
            self.QLabels[i].resize(20, 20)
            self.QLabels[i].setPixmap(pixmap)


class DialogTable2(QDialog, clasCdiolog.Ui_Dialog2):  # Диалоговое окно настроек цветов
    def __init__(self):
        QDialog.__init__(self)

        self.setupUi(self)

        self.data_is_accepted1 = False
        self.pushButton.clicked.connect(self.run2)
        self.buttonBox.accepted.connect(self.accept_data)
        self.buttonBox.rejected.connect(self.reject_data)

        f3 = open('comboBoxes.txt', encoding='utf8')  # Открываем файл с цветами и, согласно ему, активируем нужные
        self.setting_colors = ''  # значения в выпадающих списках
        for i in list(f3.read()):
            self.setting_colors += i
        self.setting_colors = self.setting_colors.split('\n')
        for i in range(7):
            self.comboBoxes[i].setCurrentText(self.setting_colors[i])
        f3.close()
        for g in self.comboBoxes:
            g.activated.connect(self.run)


    def accept_data(self):
        global colors
        f4 = open('comboBoxes.txt', mode='w', encoding='utf8')
        f4.write('\n'.join(self.setting_colors))
        f4.close()
        self.close()
        colors = self.setting_colors
        self.data_is_accepted1 = True

    def reject_data(self):
        self.close()

    def run(self):
        for m in range(7):
            self.setting_colors[m] = (self.comboBoxes[m].currentText())

    def run2(self):  # Сброс до начальных значений выпадающих списков
        global colors, colors2
        self.setting_colors = colors2
        colors = colors2
        for n in self.comboBoxes:
            n.setCurrentIndex(0)


class DialogTable3(QDialog, clasDdiolog.Ui_Dialog3):  # Диалоговое окно таблицы рекордов на двух игроков
    def __init__(self):
        QDialog.__init__(self)

        self.setupUi(self)
        self.buttonBox.accepted.connect(self.accept_data)
        self.buttonBox.rejected.connect(self.reject_data)
        con = sqlite3.connect('newbd1.sqlite')
        cur = con.cursor()
        result = cur.execute("""
        SELECT * from Records """).fetchall()
        for i in result:
            print(i)
        self.lcdNumber.display(str(max(result[0][-1], result[1][-1])))
        self.lcdNumber_2.display(str(min(result[1][-1], result[0][-1])))
        if max(result[0][-1], result[1][-1]) == result[0][-1]:
            self.label_4.setText(s[result[0][1]])
            self.label_5.setText(s[result[1][1]])
        else:
            self.label_4.setText(s[result[1][1]])
            self.label_5.setText(s[result[0][1]])
        con.close()

    def accept_data(self):
        self.close()

    def reject_data(self):
        self.close()


class DialogTable4(QDialog, clasDdiolog.Ui_Dialog3):  # Диалоговое окно таблицы рекордов на игрока и ии
    def __init__(self):
        QDialog.__init__(self)

        self.setupUi(self)
        self.buttonBox.accepted.connect(self.accept_data)
        self.buttonBox.rejected.connect(self.reject_data)
        con = sqlite3.connect('newbd1.sqlite')
        cur = con.cursor()
        result = cur.execute("""
        SELECT * from Records_2 """).fetchall()
        for i in result:
            print(i)
        self.lcdNumber.display(str(max(result[0][-1], result[1][-1])))
        self.lcdNumber_2.display(str(min(result[1][-1], result[0][-1])))
        if max(result[0][-1], result[1][-1]) == result[0][-1]:
            self.label_4.setText(s[result[0][1]])
            self.label_5.setText(s[result[1][1]])
        else:
            self.label_4.setText(s[result[1][1]])
            self.label_5.setText(s[result[0][1]])
        con.close()

    def accept_data(self):
        self.close()

    def reject_data(self):
        self.close()


class DialogTable5(QDialog, clasEdiolog.Ui_Dialog4):  # Диалоговое окно "Конец игры"
    def __init__(self):
        QDialog.__init__(self)

        self.setupUi(self)

        self.pushButton.clicked.connect(self.accept_data)
        self.pushButton_2.clicked.connect(self.reject_data)
        self.label.setText(win1)
        self.data_is_accepted2 = 0

    def accept_data(self):
        self.data_is_accepted2 = 1
        self.close()

    def reject_data(self):
        self.data_is_accepted2 = 2
        self.close()


def create_new_matrix(clas):
    a = []
    for x in range(40):
        b = []
        for y in range(20):
            b.append(clas())
        a.append(b)
    return a


def coloring(a, user_num, pos_x, pos_y):  # Изменение цветов в матрице
    g = a[:]

    while True:
        for row in range(20):
            for col in range(40):
                if a[col][row].color == a[pos_x][pos_y].color and a[col][row].user == 0:
                    if col < 39:
                        if a[col + 1][row].user == user_num:
                            a[col][row].user = user_num
                    if row < 19:
                        if a[col][row + 1].user == user_num:
                            a[col][row].user = user_num
                    if col > 0:
                        if a[col - 1][row].user == user_num:
                            a[col][row].user = user_num
                    if row > 0:
                        if a[col][row - 1].user == user_num:
                            a[col][row].user = user_num
        if g == a:
            break
        g = a[:]

    for row in range(20):
        for col in range(40):
            if a[col][row].user == user_num:
                a[col][row].color = a[pos_x][pos_y].color
    return a


def filing(a, user_num, pos_x, pos_y):  # Изменение файлов в матрице
    g = a[:]

    while True:
        for row in range(20):
            for col in range(40):
                if a[col][row].pic == a[pos_x][pos_y].pic and a[col][row].user == 0:
                    if col < 39:
                        if a[col + 1][row].user == user_num:
                            a[col][row].user = user_num
                    if row < 19:
                        if a[col][row + 1].user == user_num:
                            a[col][row].user = user_num
                    if col > 0:
                        if a[col - 1][row].user == user_num:
                            a[col][row].user = user_num
                    if row > 0:
                        if a[col][row - 1].user == user_num:
                            a[col][row].user = user_num
        if g == a:
            break
        g = a[:]

    for row in range(20):
        for col in range(40):
            if a[col][row].user == user_num:
                a[col][row].pic = a[pos_x][pos_y].pic
    return a


def counting(a, user):  # Рассчитывание процента захваченных клеток
    c, b = 800, 0
    for x in range(20):
        for y in range(40):
            b += int(a[y][x].user == user)
    return round(b / c * 100)


def recoloring(matrix, scene):  # Раскрашивание поля в соответствии с цветами в матрице
    for x in range(40):
        for y in range(20):
            rect = QGraphicsRectItem(0, 0, 20, 20)
            rect.setPos(x * 20, y * 20)
            brush = QBrush(matrix[x][y].color)
            rect.setBrush(brush)
            scene.addItem(rect)


class Box:  # Класс, обеспечивающий игру с помощью цветов
    def __init__(self):
        self.color = choice([q_colors_2[i] for i in colors])
        self.user = 0  # Показывает, свободна ли клетка (user = 0)
        # или захвачена первым (user = 1) или вторым игроком (user = 2)


class BoxPic:  # Класс, обеспечивающий игру с помощью файлов
    def __init__(self):
        self.user = 0
        self.pic = choice(f_colors)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(0, 0, 800, 400)
        self.batons = []
        self.batons_2 = []
        self.matrix = create_new_matrix(Box)
        self.percent_of_captured_1 = 0
        self.percent_of_captured_2 = 0
        self.do_hod = 0  # Если переменная равна 0, то ходит первый игрок; если 1, то - второй
        self.type_of_playing_field = True  # True для цветов, False для файлов
        self.playing_mode_2 = True  # True для игры вдвоём, False для одиночной игры

        self.matrix[0][19].user = 1  # Стартовая клетка первого игрока
        self.matrix[39][0].user = 2  # Стартовая клетка второго игрока
        self.initUI()

    def initUI(self):
        self.setGeometry(830, 545, *SCREEN_SIZE)
        self.setWindowTitle('filler')

        f1 = open('radiobut.txt', encoding='utf8')  # Установка выбранного при последнем открытии программы
        f11 = list(f1.read())  # типа поля и режима игры
        if f11:
            if f11[0] == '1':
                self.matrix = create_new_matrix(BoxPic)
                self.type_of_playing_field = False
            if f11[-1] == '2':
                self.playing_mode_2 = False

        self.baton_1 = QPushButton(self)
        self.baton_1.setText('рекорды')
        self.baton_1.resize(200, 30)
        self.baton_1.move(15, 5)
        self.baton_1.clicked.connect(self.records)

        self.lebel = QLabel(self)
        self.lebel.setText("Захвачено: 0%")
        self.lebel.move(40, 30)

        self.lebel_2 = QLabel(self)
        self.lebel_2.setText("Захвачено: 0%")
        self.lebel_2.move(700, 30)

        self.baton_2 = QPushButton('начать заново', self)
        self.baton_2.resize(200, 30)
        self.baton_2.move(215, 5)
        self.baton_2.clicked.connect(self.beginning)

        self.baton_3 = QPushButton('настройки', self)
        self.baton_3.resize(200, 30)
        self.baton_3.move(415, 5)
        self.baton_3.clicked.connect(self.settings)

        self.graphicView_1 = QGraphicsView(self)
        self.graphicView_1.resize(830, 420)
        self.graphicView_1.move(0, 60)

        if self.type_of_playing_field:  # Генерация поля
            recoloring(self.matrix, self.scene)
        else:
            for y in range(20):
                for x in range(40):
                    pixmap = QPixmap(self.matrix[x][y].pic)
                    pixmapitem = self.scene.addPixmap(pixmap)
                    pixmapitem.setPos(x * 20, y * 20)

        self.graphicView_1.setScene(self.scene)

        for i in range(7):  # Генерация кнопок 1 игрока
            baton = QPushButton(self)
            baton.resize(40, 40)
            baton.move(10 + 50 * i, 490)
            if self.type_of_playing_field:
                baton.setStyleSheet('background-color: {}'.format(colors[i]))
            else:
                baton.setStyleSheet('background-color: lightGrey')
                baton.setIcon(QIcon(f_colors[i]))
                baton.setIconSize(QSize(40, 40))
            baton.clicked.connect(self.play_1)
            self.batons.append(baton)

        for i in range(7):  # Генерация кнопок 2 игрока
            baton = QPushButton(self)
            baton.resize(40, 40)
            baton.move(480 + 50 * i, 490)
            if self.type_of_playing_field:
                baton.setStyleSheet('background-color: {}'.format(colors[i]))
            else:
                baton.setStyleSheet('background-color: lightGrey')
                baton.setIcon(QIcon(f_colors[i]))
                baton.setIconSize(QSize(40, 40))
            if f11[-1] == '2':  # Если стоит рижим одиночной игры, то кнопки для второго игрока убираются
                baton.hide()
            baton.clicked.connect(self.play_2)
            self.batons_2.append(baton)

        f1.close()

    def play_1(self):  # Первый игрок
        if self.playing_mode_2:  # если режим игры на двух игроков
            if self.do_hod == 0:  # Проверка очерёдности хода
                if self.type_of_playing_field:  # если тип поля "цвета"
                    for i in range(7):
                        if self.batons[i] == self.sender():
                            self.matrix[0][19].color = q_colors_2[colors[i]]

                    self.matrix = coloring(self.matrix, 1, 0, 19)
                    recoloring(self.matrix, self.scene)

                    self.graphicView_1.setScene(self.scene)

                else:  # если тип поля "файлы"
                    for i in range(7):
                        if self.batons[i] == self.sender():
                            self.matrix[0][19].pic = f_colors[i]

                    self.matrix = filing(self.matrix, 1, 0, 19)

                    for y in range(20):  # Расставление файлов в соответсвии с файлами в матрице
                        for x in range(40):
                            pixmap = QPixmap(self.matrix[x][y].pic)
                            pixmapitem = self.scene.addPixmap(pixmap)
                            pixmapitem.setPos(x * 20, y * 20)

                    self.graphicView_1.setScene(self.scene)

            self.do_hod = 1

            self.percent_of_captured_1 = counting(self.matrix, 1)
            self.lebel.setText('Захвачено: {0}%'.format(self.percent_of_captured_1))
            self.count()  # проверка на победу

        else:  # если стоит одиночный режим игры
            if self.type_of_playing_field:  # если тип поля "цвета"
                for i in range(7):
                    if self.batons[i] == self.sender():
                        self.matrix[0][19].color = q_colors_2[colors[i]]

                self.matrix = coloring(self.matrix, 1, 0, 19)

                recoloring(self.matrix, self.scene)
                self.graphicView_1.setScene(self.scene)

                a = [0, 0, 0, 0, 0, 0, 0]  # алгоритм выбора нового цвета
                b = [q_colors_2[i] for i in colors]
                for row in range(20):
                    for col in range(40):
                        if self.matrix[col][row].user == 0:
                            if col != 39:
                                if self.matrix[col + 1][row].user == 2:
                                    a[b.index(self.matrix[col][row].color)] += 1
                            if row != 19:
                                if self.matrix[col][row + 1].user == 2:
                                    a[b.index(self.matrix[col][row].color)] += 1
                            if col != 0:
                                if self.matrix[col - 1][row].user == 2:
                                    a[b.index(self.matrix[col][row].color)] += 1
                            if row != 0:
                                if self.matrix[col][row - 1].user == 2:
                                    a[b.index(self.matrix[col][row].color)] += 1
                self.matrix[39][0].color = b[a.index(max(a))]

                self.matrix = coloring(self.matrix, 2, 39, 0)

                recoloring(self.matrix, self.scene)
                self.graphicView_1.setScene(self.scene)

            else:  # если тип поля "файлы"
                for i in range(7):
                    if self.batons[i] == self.sender():
                        self.matrix[0][19].pic = f_colors[i]

                self.matrix = filing(self.matrix, 1, 0, 19)

                for y in range(20):
                    for x in range(40):
                        pixmap = QPixmap(self.matrix[x][y].pic)
                        pixmapitem = self.scene.addPixmap(pixmap)
                        pixmapitem.setPos(x * 20, y * 20)

                self.graphicView_1.setScene(self.scene)

                a = [0, 0, 0, 0, 0, 0, 0]  # алгоритм выбора нового файла
                for row in range(20):
                    for col in range(40):
                        if self.matrix[col][row].user == 0:
                            if col != 39:
                                if self.matrix[col + 1][row].user == 2:
                                    a[f_colors.index(self.matrix[col][row].pic)] += 1
                            if row != 19:
                                if self.matrix[col][row + 1].user == 2:
                                    a[f_colors.index(self.matrix[col][row].pic)] += 1
                            if col != 0:
                                if self.matrix[col - 1][row].user == 2:
                                    a[f_colors.index(self.matrix[col][row].pic)] += 1
                            if row != 0:
                                if self.matrix[col][row - 1].user == 2:
                                    a[f_colors.index(self.matrix[col][row].pic)] += 1
                self.matrix[39][0].pic = f_colors[a.index(max(a))]

                self.matrix = filing(self.matrix, 2, 39, 0)

                for y in range(20):
                    for x in range(40):
                        pixmap = QPixmap(self.matrix[x][y].pic)
                        pixmapitem = self.scene.addPixmap(pixmap)
                        pixmapitem.setPos(x * 20, y * 20)
                self.graphicView_1.setScene(self.scene)

            a = counting(self.matrix, 1)
            a1 = counting(self.matrix, 2)  # проверка на победу в одиночном режиме
            self.lebel.setText('Захвачено: {0}%'.format(a))
            self.lebel_2.setText('Захвачено: {0}%'.format(a1))
            if a == a1 == 50:
                self.end('Ничья', '"ai", "player1"')
            elif a >= 50:
                self.end('Вы выиграли', '"player1"')
            elif a1 >= 50:
                self.end('Вы проиграли', '"ai"')

    def count(self):  # проверка на победу в режиме игры на двух игроков
        if self.percent_of_captured_1 == self.percent_of_captured_2 == 50:
            self.end('Ничья', '"player2", "player1"')
        elif self.percent_of_captured_1 >= 50:
            self.end('Выиграл первый игрок', '"player1"')
        elif self.percent_of_captured_2 >= 50:
            self.end('Выиграл второй игрок', '"player2"')

    def end(self, win, winner):  # конец игры, победа одного из игроков или ии
        global win1
        win1 = win

        con = sqlite3.connect('newbd1.sqlite')
        cur = con.cursor()
        if not self.playing_mode_2:
            cur.execute("""UPDATE Records_2
                SET Number_of_wins = Number_of_wins + 1
                WHERE Player IN ({})""".format(winner)).fetchall()
        else:
            cur.execute("""UPDATE Records
                SET Number_of_wins = Number_of_wins + 1
                WHERE Player IN ({})""".format(winner)).fetchall()
        con.commit()
        con.close()
        self.hide()

        self.dialog = DialogTable5()
        self.dialog.show()
        self.dialog.exec_()

        if self.dialog.data_is_accepted2 == 1:
            self.beginning()
        elif self.dialog.data_is_accepted2 == 2:
            self.close()

    def play_2(self):  # второй игрок
        if self.do_hod == 1:  # Проверка очерёдности хода
            if self.type_of_playing_field:  # если тип поля "цвета"
                for i in range(7):
                    if self.batons_2[i] == self.sender():
                        self.matrix[39][0].color = q_colors_2[colors[i]]

                self.matrix = coloring(self.matrix, 2, 39, 0)

                recoloring(self.matrix, self.scene)
                self.graphicView_1.setScene(self.scene)

            else:  # если тип поля "файлы"
                for i in range(7):
                    if self.batons_2[i] == self.sender():
                        self.matrix[39][0].pic = f_colors[i]

                self.matrix = filing(self.matrix, 2, 39, 0)

                for y in range(20):
                    for x in range(40):
                        pixmap = QPixmap(self.matrix[x][y].pic)
                        pixmapitem = self.scene.addPixmap(pixmap)
                        pixmapitem.setPos(x * 20, y * 20)

                self.graphicView_1.setScene(self.scene)

        self.do_hod = 0
        self.percent_of_captured_2 = counting(self.matrix, 2)
        self.lebel_2.setText('Захвачено: {0}%'.format(self.percent_of_captured_2))
        self.count()  # проверка на победу

    def beginning(self):  # Начать заново
        self.hide()
        self.dialog = DialogTable()
        self.dialog.show()
        self.dialog.exec_()
        self.show()

        if self.dialog.data_is_accepted1:  # если пользователь нажал "OK"
            try:
                f2 = open('radiobut.txt', mode='w', encoding='utf8')  # Записываем в файл активированные радиобаттоны
                if self.dialog.radioButton.isChecked():  # тип поля "цвета"
                    self.matrix.clear()
                    self.matrix = create_new_matrix(Box)
                    recoloring(self.matrix, self.scene)
                    self.type_of_playing_field = True
                    f2.write('0')  # первая цифра в файле отвечает за тип поля, вторая - за режим игры

                    for i in range(7):  # изменение кнопок в соответствии с выбранным типом поля
                        self.batons[i].setStyleSheet('background-color: {}'.format(colors[i]))
                        self.batons[i].setIcon(QIcon())

                        self.batons_2[i].setStyleSheet('background-color: {}'.format(colors[i]))
                        self.batons_2[i].setIcon(QIcon())

                if self.dialog.radioButton_2.isChecked():  # тип поля "файлы"
                    self.matrix.clear()
                    self.matrix = create_new_matrix(BoxPic)
                    for y in range(20):
                        for x in range(40):
                            pixmap = QPixmap(self.matrix[x][y].pic)
                            pixmapitem = self.scene.addPixmap(pixmap)
                            pixmapitem.setPos(x * 20, y * 20)
                    self.type_of_playing_field = False
                    f2.write('1')

                    for c in range(7):  # изменение кнопок в соответствии с выбранным типом поля
                        self.batons[c].setStyleSheet('background-color: lightGrey')
                        self.batons[c].setIcon(QIcon(f_colors[c]))

                        self.batons_2[c].setStyleSheet('background-color: lightGrey')
                        self.batons_2[c].setIcon(QIcon(f_colors[c]))

                if self.dialog.radioButton_3.isChecked():  # режим игры "одиночный"
                    for n in range(7):
                        self.batons_2[n].hide()
                    self.playing_mode_2 = False
                    f2.write('2')

                if self.dialog.radioButton_4.isChecked():  # режим игры "на двух игроков"
                    for q in range(7):
                        self.batons_2[q].show()
                    self.playing_mode_2 = True
                    f2.write('3')

                self.matrix[0][19].user = 1
                self.matrix[39][0].user = 2
                self.lebel.setText("Захвачено: 0%")
                self.lebel_2.setText("Захвачено: 0%")
                self.do_hod = 0
                self.percent_of_captured_1, self.percent_of_captured_2 = 0, 0
                f2.close()
            except Exception as e:
                print(e, 12345)

    def records(self):  # таблица рекордов
        try:
            if self.playing_mode_2:  # таблица рекордов на двух игроков
                self.dialog = DialogTable3()
                self.dialog.show()
                self.dialog.exec_()
            else:  # таблица рекордов на одного игрока и ии
                self.dialog = DialogTable4()
                self.dialog.show()
                self.dialog.exec()
        except Exception as e:
            print(e)

    def settings(self):  # настройки
        if not self.type_of_playing_field:
            self.dialog = DialogTable1()
            self.dialog.show()
            self.dialog.exec_()

            if self.dialog.data_is_accepted:  # если пользователь нажал "OK"
                self.beginning()
        else:
            self.dialog = DialogTable2()
            self.dialog.show()
            self.dialog.exec_()

            if self.dialog.data_is_accepted1:  # если пользователь нажал "OK"
                self.beginning()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Выход', 'Вы уверены, что хотите выйти?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
