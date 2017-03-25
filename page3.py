import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
   def __init__(self, parent=None):
      super(Form, self).__init__(parent)
		
      layout = QVBoxLayout()
      self.setGeometry(500, 500, 300, 300)
      self.b1 = QPushButton("Submit")
      self.b1.setCheckable(True)
      self.b1.toggle()
      self.b1.clicked.connect(lambda:self.whichbtn(self.b1))
      self.b1.clicked.connect(self.btnstate)
      layout.addWidget(self.b1)
		
     
      self.setLayout(layout)
     # self.b3 = QPushButton("Submit")
     # self.b3.setEnabled(True)
      #layout.addWidget(self.b3)
		
      
      
      self.setWindowTitle("Page 3")

   def btnstate(self):
      if self.b1.isChecked():
         print "button pressed"
      else:
         print "button released"
			
   def whichbtn(self,b):
      print "clicked button is "+b.text()

def main():
   app = QApplication(sys.argv)
   ex = Form()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()