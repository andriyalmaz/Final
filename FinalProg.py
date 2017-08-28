import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QGridLayout)

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):      

        but1=QPushButton('1')
        but1.resize(50,20)  
        
        but2=QPushButton('2')
        but2.resize(50,70)   
        
        but3=QPushButton('3')
        but3.resize(500,70)   

        but4=QPushButton('4')
        but4.resize(250,170)  
        
        ans1=QLabel('Відповідь номер один')
        ans1.setWordWrap(True)
        
        ans2=QLabel('Відповідь номер два')
        ans2.setWordWrap(True)       
        
        ans3=QLabel('Відповідь номер три')
        ans3.setWordWrap(True) 
        
        ans4=QLabel('Відповідь номер чотири') 
        ans4.setWordWrap(True)        
                
        grid = QGridLayout()
        
        grid.setSpacing(25)
        
        que=QLabel('Головне питання ')
        que.setWordWrap(True)        

        grid.addWidget(que,0,1,2,2)
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
        

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())