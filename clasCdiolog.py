from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
q_colors_2 = {'blue': Qt.blue, 'red': Qt.red, 'yellow': Qt.yellow, 'magenta': Qt.magenta,
              'cyan': Qt.cyan, 'green': Qt.green, 'gray': Qt.gray, 'white': Qt.white, 'black': Qt.black,
              'darkRed': Qt.darkRed, 'darkGreen': Qt.darkGreen, 'darkBlue': Qt.darkBlue,
              'darkCyan': Qt.darkCyan, 'darkGray': Qt.darkGray, 'darkMagenta': Qt.darkMagenta,
              'darkYellow': Qt.darkYellow, 'lightGray': Qt.lightGray}


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(284, 282)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 240, 161, 21))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 40, 111, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox_4 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_4)
        self.comboBox_5 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox_5)
        self.comboBox_6 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_6.setObjectName("comboBox_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox_6)
        self.comboBox_7 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_7.setObjectName("comboBox_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBox_7)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 10, 91, 16))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 240, 81, 21))
        self.pushButton.setObjectName("pushButton")

        a = list(q_colors_2.keys())
        for i in range(len(a)):
            self.comboBox.addItem(a[i])
            self.comboBox_2.addItem(a[(i + 1) % len(a)])
            self.comboBox_3.addItem(a[(i + 2) % len(a)])
            self.comboBox_4.addItem(a[(i + 3) % len(a)])
            self.comboBox_5.addItem(a[(i + 4) % len(a)])
            self.comboBox_6.addItem(a[(i + 5) % len(a)])
            self.comboBox_7.addItem(a[(i + 6) % len(a)])

        self.comboBoxes = [self.comboBox, self.comboBox_2, self.comboBox_3,
                  self.comboBox_4, self.comboBox_5, self.comboBox_6,
                  self.comboBox_7]

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "2"))
        self.label_3.setText(_translate("Dialog", "3"))
        self.label_4.setText(_translate("Dialog", "4"))
        self.label_5.setText(_translate("Dialog", "5"))
        self.label_6.setText(_translate("Dialog", "6"))
        self.label_7.setText(_translate("Dialog", "7"))
        self.label.setText(_translate("Dialog", "1"))
        self.label_8.setText(_translate("Dialog", "Выберете цвета"))
        self.pushButton.setText(_translate("Dialog", "Сбросить"))
