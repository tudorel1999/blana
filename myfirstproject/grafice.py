from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QTabWidget, QComboBox, QCheckBox, QGroupBox, QVBoxLayout, QWidget, \
    QLabel, QLineEdit, QDialogButtonBox, QCompleter, QMessageBox
#from numpy import np
import sys
from PyQt5.QtGui import QIcon


class Tab(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Depunere bani online")
        self.setWindowIcon(QIcon("hackerman.png"))
        self.setStyleSheet('background-color:lightseagreen')
        vbox = QVBoxLayout()
        tabWidget = QTabWidget()
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)
        tabWidget.setFont(QtGui.QFont("Wingding", 12))
        tabWidget.addTab(TabContact(), "Detalii cont")
        tabWidget.addTab(TabPeronsalDetails(), "Detalii valuta depusa")
        vbox.addWidget(tabWidget)
        vbox.addWidget(buttonbox)
        self.setLayout(vbox)



class TabContact(QWidget):
    def __init__(self):
        super().__init__()
        nameLabel = QLabel("Nume și prenume: ")
        nameedit = QLineEdit()
        cont = QLabel("Nr. de cont")
        contedit = QLineEdit()
        addr = QLabel("Adresă:")
        addredit = QLineEdit()
        telefon = QLabel("Nr. de telefon:")
        telefonedit = QLineEdit()
        vbox = QVBoxLayout()
        vbox.addWidget(nameLabel)
        nameEdit = ["Zamfir Diana", "Zamfir Alexandru", "Zamfir Radu", "Popescu Octavian", "Ilie Adrian","Ilie Cristi","Popescu Steala","Popescu Mariana"]
        completer = QCompleter(nameedit)
        self.lineedit = QLineEdit()
        self.lineedit.setCompleter(completer)
        vbox.addWidget(self.lineedit)
        vbox.addWidget(cont)
        vbox.addWidget(contedit)
        vbox.addWidget(addr)
        vbox.addWidget(addredit)
        vbox.addWidget(telefon)
        vbox.addWidget(telefonedit)
        self.setLayout(vbox)

class TabPeronsalDetails(QWidget):
    def __init__(self):
        super().__init__()
        groupBox = QGroupBox("Alegeti valuta")
        list = ["LEI", "EURO","LIRE","YENI"]
       # self.setStyleSheet('background-color:white')
        combo = QComboBox()
        combo.addItems(list)
        vbox = QVBoxLayout()
        vbox.addWidget(combo)
        groupBox.setLayout(vbox)
        self.combo.currentIndexChanged.connect(self.selectionchange)
        groupBox2 = QGroupBox("Alegeți suma pe care doriti sa o depuneți în cont:")
        suma1 = QCheckBox("50 lei")
        suma2 = QCheckBox("100 lei")
        suma3 = QCheckBox("200 lei")
        suma4 = QCheckBox("Altă sumă")
        vboxp = QVBoxLayout()
        vboxp.addWidget(suma1)
        vboxp.addWidget(suma2)
        vboxp.addWidget(suma3)
        vboxp.addWidget(suma4)
        groupBox2.setLayout(vboxp)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(groupBox)
        mainLayout.addWidget(groupBox2)
        self.setLayout(mainLayout)

    def selectionchange(self, i):
        print ("Items in the list are :")
        for count in range(self.combo.count()):
            print(self.combo.itemText(count))
        print("Current index", i, "selection changed ", self.combo.currentText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tabdialog = Tab()
    tabdialog.show()
    app.exec()