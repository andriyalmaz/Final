import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.btn = QPushButton("kykyky",self)
        self.btn.move(30, 50)

        self.btn.clicked.connect(self.buttonClicked)

        self.que=QLabel('kykyky',self)
        self.que.move(15,10)
        
        self.setWindowTitle('kykyky')   
        
        self.statusBar().showMessage('kykyky')
        
        self.setGeometry(300, 300, 290, 150)
        self.show()

    def buttonClicked(self):
        self.btn.setText('rarara')
        self.que.setText('rarara')
        
        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())