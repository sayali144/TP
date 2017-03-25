from PyQt4 import QtGui, QtCore
import os, sys


class PrettyWidget(QtGui.QWidget):
    
    def __init__(self):
        super(PrettyWidget, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        self.setGeometry(600, 500, 300, 200)
        self.setWindowTitle('Multiple Browse') 
	    
        
        btn = QtGui.QPushButton('Browse\n(MULTIPLE)', self)
	
	#btn.setGeometry(200, 200, 350, 120) 
	btn.resize(btn.sizeHint())
        btn.clicked.connect(self.SingleBrowse)
	btn.resize(200,200)
        btn.move(150, 100) 
        go_button = QtGui.QPushButton("next", self)
	go_button.setDefault(True)
	   

        self.show()

  


    def SingleBrowse(self):
        filePaths = QtGui.QFileDialog.getOpenFileNames(self, 
                                                       'Multiple File',
                                                       "~/Desktop/PyRevolution/PyQt4",
                                                      '*.xlsx')
        for filePath in filePaths:
            print('filePath',filePath, '\n')
            fileHandle = open(filePath, 'r')
            lines = fileHandle.readlines()
            for line in lines:
                print(line)
	

    
def main():
    app = QtGui.QApplication(sys.argv)
    w = PrettyWidget()
    app.exec_()


if __name__ == '__main__':
    main()
s
