import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QGridLayout)
n=0
rez=0

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):      

        self.que=QLabel(lis[n])
        self.que.setWordWrap(True) 
        
        self.but1=QPushButton('1',self)
        self.but1.resize(50,20) 
        self.but1.clicked.connect(self.newQue)
        
        self.but2=QPushButton('2',self)
        self.but2.resize(50,70) 
        self.but2.clicked.connect(self.newQue)
        
        self.but3=QPushButton('3',self)
        self.but3.resize(500,70)
        self.but3.clicked.connect(self.newQue)

        self.but4=QPushButton('4',self)
        self.but4.resize(250,170)
        self.but4.clicked.connect(self.newQue)
        
        self.ans1=QLabel(lis[n+1])
        self.ans1.setWordWrap(True)
        
        self.ans2=QLabel(lis[n+2])
        self.ans2.setWordWrap(True)       
        
        self.ans3=QLabel(lis[n+3],self)
        self.ans3.setWordWrap(True) 
        
        self.ans4=QLabel(lis[n+4],self) 
        self.ans4.setWordWrap(True)        
                
        grid = QGridLayout()
        
        grid.setSpacing(25)
  
        grid.addWidget(self.que,0,1,2,2)
        
        grid.addWidget(self.ans1, 1, 1)
        grid.addWidget(self.but1, 2, 1)
        
        grid.addWidget(self.ans2, 1, 2)       
        grid.addWidget(self.but2, 2, 2) 
        
        grid.addWidget(self.ans3, 3, 1)        
        grid.addWidget(self.but3, 4, 1) 
        
        grid.addWidget(self.ans4, 3, 2)        
        grid.addWidget(self.but4, 4, 2)
        
        self.setLayout(grid)
        
        self.setGeometry(300, 300, 890, 510)
        self.setWindowTitle('Test Program')
        self.show()
        
    def newQue(self):
        global rez
        global n
        sender=self.sender()
        if sender.text()==str(lis[n+5]):
            rez=rez+1
        print (rez)
        n=n+6  
        if n<len (lis):
            self.que.setText(lis[n])
            self.ans1.setText(lis[n+1])
            self.ans2.setText(lis[n+2])
            self.ans3.setText(lis[n+3])
            self.ans4.setText(lis[n+4])
        else:
            self.que.setText('результат')
            self.but1.setParent(None)
            self.but2.setParent(None)
            self.but3.setParent(None)
            self.but4.setParent(None)
            self.ans1.setText(str(rez))
            self.ans2.setParent(None)
            self.ans3.setParent(None)
            self.ans4.setParent(None)
            
     
if __name__ == '__main__':
    f = open('que.txt', 'r')
    lis=[] 
    for line in f:
        lis.append(line)
    lis = [line.rstrip() for line in lis]
    while n<len(lis):
        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())