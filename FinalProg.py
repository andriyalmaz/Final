import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QGridLayout)
from PyQt5 import QtCore
n=0
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):      

        self.que=QLabel(lis[n])
        self.que.setWordWrap(True) 
        
        but1=QPushButton('1')
        but1.resize(50,20) 
        but1.clicked.connect(self.newQue)
        
        but2=QPushButton('2')
        but2.resize(50,70)   
        
        but3=QPushButton('3')
        but3.resize(500,70)   

        but4=QPushButton('4')
        but4.resize(250,170)  
        
        ans1=QLabel(lis[n+1],self)
        ans1.setWordWrap(True)
        
        ans2=QLabel(lis[n+2],self)
        ans2.setWordWrap(True)       
        
        ans3=QLabel(lis[n+3],self)
        ans3.setWordWrap(True) 
        
        ans4=QLabel(lis[n+4],self) 
        ans4.setWordWrap(True)        
                
        grid = QGridLayout()
        
        grid.setSpacing(25)
  
        grid.addWidget(self.que,0,1,2,2)
        
        grid.addWidget(ans1, 1, 1)
        grid.addWidget(but1, 2, 1)
        
        grid.addWidget(ans2, 1, 2)       
        grid.addWidget(but2, 2, 2) 
        
        grid.addWidget(ans3, 3, 1)        
        grid.addWidget(but3, 4, 1) 
        
        grid.addWidget(ans4, 3, 2)        
        grid.addWidget(but4, 4, 2)
        
        self.setLayout(grid)
        
        self.setGeometry(300, 300, 890, 510)
        self.setWindowTitle('Test Program')
        self.show()
    def newQue(self):
        self.que=QLabel(lis[n+5])   
     
if __name__ == '__main__':
    f = open('que.txt', 'r')
    lis=[] 
    for line in f:
        lis.append(line)
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())