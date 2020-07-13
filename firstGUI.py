import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import Slot
import mergepdf_mod
import os
import PyQt4
from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter
from PyQt4 import QtGui, QtCore
import os
class Window(PyQt4.QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(500,500,500,300);
        self.setWindowTitle("PDF Tool");
        self.setWindowIcon(QtGui.QIcon("Firefox_wallpaper.jpg"))
        self.contents = QtGui.QTextEdit()
        self.home();
    def home(self):

        buttonMerge = PyQt4.QtGui.QPushButton("Merge", self )
        buttonMerge.clicked.connect(self.merge)
        buttonMerge.resize(100,100)
        buttonMerge.move(100,100)

        buttonSplit = PyQt4.QtGui.QPushButton("Split", self )
        buttonSplit.clicked.connect(self.slice)
        buttonSplit.resize(100,100)
        buttonSplit.move(200,100)
        
        
        
        
        self.show()

    def merge(self):
        fileName = QtGui.QFileDialog.getOpenFileNames(self, 'OpenFile','\\',"Image files (*.pdf)",options=QtGui.QFileDialog.DontUseNativeDialog)
        fileName = map(str, fileName)
        pdfs = fileName;
    	merger = PdfFileMerger()
        print pdfs
    	for pdf in pdfs:
    		merger.append(pdf)
    	merger.write('merged_GUI.pdf')
    	merger.close();

    def slice(self):
        fileName = QtGui.QFileDialog.getOpenFileNames(self, 'OpenFile','\\',"Image files (*.pdf)") # gets the name of the file with user selection
        fileName = map(str, fileName) #converts it to a string(it is an object)
        text, ok = PyQt4.QtGui.QInputDialog.getText(self, 'Text Input Dialog', 'Enter pages to be removed, format: \n for single pages ,2,3, for ranges 3-6') ; # a user input form is called, to decide which page has to be removed
        text = map(str,text.split(','));#comma separation
        pages = []
        #os.system(fileName[0] )        # in the for loop the ranges (x-y) are extracted
        for el in text:
            lista = el.split('-');
            for num in range(int(lista[0]),int(lista[-1])+1):
                pages.append(num);
        numbers = map(int, pages);
        infile = PdfFileReader(fileName[0], 'rb')
        output = PdfFileWriter()
        for i in range(infile.getNumPages()):
            if i not in numbers:
                p = infile.getPage(i)
                output.addPage(p)

        with open('newfile.pdf', 'wb') as f:
            output.write(f)
        
        
        
        
        
        
        
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
run()
