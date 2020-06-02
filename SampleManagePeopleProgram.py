'''Simple Manage People Program'''
from PyQt5.QtWidgets import *

'''Friends list'''
names = ['HCK','JDH','KJM']

'''Application'''
app = QApplication([])
app.setApplicationName('Mange Human Network')

win = QMainWindow()
win.resize(500,500)

def add():
    name = nameLineEdit.text()
    if len(name)== 0:
        return
    
    global names
    
    if names.count(name) == 1 :
        sb.showMessage(name + 'is already yout friend.')
    else :
        sb.showMessage(name + 'is your new friend.')
        names.append(name)
    #print('ADD')
    pass
def remove():
    name = nameLineEdit.text()
    if len(name) == 0:
        return
    
    global names
    
    if names.count(name) == 0:
        sb.showMessage(name + 'is not your friend.')
    else:
        sb.showMessage(name + 'is removed.')
        names.remove(name)
    #print('REMOVE')
    pass

def close():
    quit()
    print('EXIT')
    pass

''' Menu Bar'''
menuBar = win.menuBar()
menu = menuBar.addMenu('MENU')
exitAct = QAction('EXIT',win)

exitAct.triggered.connect(close)

menuBar.addAction(exitAct)

menuAdd = QAction('ADD',win)
menuRemove = QAction('REMOVE',win)

menuAdd.triggered.connect(add)
menuRemove.triggered.connect(remove)

menu.addAction(menuAdd)
menu.addAction(menuRemove)

'''BODY(FORM)'''
main = QWidget()
win.setCentralWidget(main)
mainLayout = QFormLayout()
main.setLayout(mainLayout)

'''First line'''
label = QLabel('Start to manage human networks...')
mainLayout.addRow(label)

'''Seconnd line(inputline)'''
inputLayout = QHBoxLayout()
nameLineEdit = QLineEdit()
mainLayout.addRow('name',nameLineEdit)

'''Third line(buttons)'''
btnLayout = QHBoxLayout()
btnAdd = QPushButton('ADD')
btnRemove = QPushButton('REMOVE')


btnLayout.addWidget(btnAdd)
btnLayout.addWidget(btnRemove)

mainLayout.addRow(btnLayout)

'''Status Bar'''
statusBar = win.statusBar()
statusBar.showMessage('Manage human networks.')

win.show()
app.exec_()

