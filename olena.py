from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*


#Створення додатка
app=QApplication([])
win=QWidget()

win.resize(500,500)
win.setWindowTitle('Тест ГітХаб')

title=QLabel('Тестовий додаток для ГітХаб')

line_h=QHBoxLayout()
line_h.addChildWidget(title)

win.setLayout(line_h)

win.show()
win.show(lene_h)
app.exec_()
