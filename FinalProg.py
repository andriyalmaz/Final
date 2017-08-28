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
        
        ans1=QLabel('Answer1sdg  sdfg  dfsg sdfg sdf sdh sdhh sdh ersdfg sh stysfd')
        ans1.setWordWrap(True)
        
        ans2=QLabel('Answer1sdg  sdfg  dfsfg sh stysfd')
        ans2.setWordWrap(True)       
        
        ans3=QLabel('Answer1sdg  sdfg  dfsg sdfg sdf sdh sdhh h stysfd')
        ans3.setWordWrap(True) 
        
        ans4=QLabel('Answer1sdg  sdfg  dfsg sdfg sdf sdh sdhh sdhd') 
        ans4.setWordWrap(True)        
                
        grid = QGridLayout()
        
        grid.setSpacing(25)
        
        que=QLabel('df kjdfgk d ;skdg h ljfgh alfhgklj adfg ')
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