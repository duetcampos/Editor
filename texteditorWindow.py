from texteditor import Ui_TextEditor
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox,QFontDialog,QColorDialog,QLabel,QFrame,QSizePolicy
import os
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog,QPrintPreviewDialog
from PyQt5.QtCore import QFileInfo,Qt,QTime,QDate,QTimer,QLine
from PyQt5.QtGui import QFont,QColor
from time import sleep



bold = True
# global italic
#global underline
class EditorWindow(QtWidgets.QMainWindow, Ui_TextEditor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionNew.triggered.connect(self.filenew)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.fileSave)
        self.actionPrint.triggered.connect(self.printfile)
        self.actionPrint_Preview.triggered.connect(self.printPreview)
        self.actionExport_PDF.triggered.connect(self.exportPdf)
        self.actionExit.triggered.connect(self.exitApp)
        self.actionCopy.triggered.connect(self.copy)
        self.actionPaste.triggered.connect(self.paste)
        self.actionCut.triggered.connect(self.cut)
        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)
        self.actionFont.triggered.connect(self.fontdialog)
        self.actionColor.triggered.connect(self.colordialog)
        self.actionBold.triggered.connect(self.textbold)
        self.actionItalic.triggered.connect(self.italic)
        self.actionUnderline.triggered.connect(self.underline)
        self.actionLeft.triggered.connect(self.alignLeft)
        self.actionCenter.triggered.connect(self.alignCenter)
        self.actionRight.triggered.connect(self.alignRight)
        self.actionJustify.triggered.connect(self.alignJustify)
        self.actionTime.triggered.connect(self.showTime)
        self.actionDate.triggered.connect(self.showDate)
        self.actionText_Highlight.triggered.connect(self.highlight)
       
        #self.textEdit.cursorPositionChanged.connect(self.CursorPosition)
        
       
        
        self.textEdit.cursorPositionChanged.connect(self.CursorPosition)
        
        

        self.show()


    def filenew(self):
        self.textEdit.clear()        

    def openFile(self):
        openpth = os.path.dirname(__file__)
        filename = QFileDialog.getOpenFileName(self,'Open File',openpth)
        try:
            if filename[0]:
                f = open(filename[0],'r')

                with f:
                    data = f.read()
                    self.textEdit.setText(data)
                    f.close()
        except FileNotFoundError as err:
            pass             

    def fileSave(self):
        text = self.textEdit.toPlainText()
        if text == '':
            QMessageBox.critical(self,"No text","Please type something then save a file")
        try:
        
            filename = QFileDialog.getSaveFileName(self,'Save File')
            
            f=open(filename[0],'w')
            with f:           
                f.write(text)
                QMessageBox.about(self,"Save File","File Saved Successfully")
                f.close()
        except FileNotFoundError as err:
            pass     

        


    def printfile(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer,self)

        if dialog.exec() == QPrintDialog.Accepted():
            self.textEdit.print(printer)


    def printPreview(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer,self)
        previewDialog.paintRequested.connect(self.preview)
        previewDialog.exec()

    def preview(self,printer):
        self.textEdit.print(printer)  


    def exportPdf(self):
        fn, _ = QFileDialog.getSaveFileName(self,"Export PDF",None,"PDF files (*.pdf) ;; All files (*.*)")
        if fn != "":
            if QFileInfo(fn).suffix() == "":
                fn += '.pdf'
                
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print(printer) 

    def exitApp(self):
        self.close()  


    def copy(self):
        cursor = self.textEdit.textCursor()
        textSelect = cursor.selectedText()
        self.copiedText = textSelect


    def paste(self):
        self.textEdit.append(self.copiedText)  


    def cut(self):
        cursor = self.textEdit.textCursor()
        textSelected = cursor.selectedText()
        self.copyiedText = textSelected
        self.textEdit.cut()

    def fontdialog(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setCurrentFont(font)  # use setFont(font) if you want to change font of all text when you change it from app.

    def colordialog(self):
        color = QColorDialog().getColor()
        
        if QColor.isValid(color):
            self.textEdit.setTextColor(color)
    
    def textbold(self):
        global bold
        if bold == True:
            #font = QFont().se
            #font.setBold(True)
            self.textEdit.setFontWeight(75)
            bold = False
        else:
            # font = QFont()
            # font.setBold(False)
            self.textEdit.setFontWeight(50)
            bold = True    
        
        


    # def italic(self):
    #     global italic
    #     self.textEdit.font
    #     if italic == True:
    #         font = QFont() 
    #         font.setItalic(True)
    #         self.textEdit.setCurrentFont(font)
    #         italic = False
    #     else:
    #         font = QFont() 
    #         font.setItalic(False)
    #         self.textEdit.setCurrentFont(font)
    #         italic = True

    def italic(self):
        #global italic
        i = self.textEdit.fontItalic()
        if i == False:
            self.textEdit.setFontItalic(True)
        elif i == True:
            self.textEdit.setFontItalic(False)    
        



    # def underline(self):
    #     global underline
    #     if underline == True:
    #         font = QFont()
    #         font.setUnderline(True)
    #         self.textEdit.setCurrentFont(font)
    #         underline = False  
    #     else:
    #         font = QFont()
    #         font.setUnderline(False)
    #         self.textEdit.setCurrentFont(font)
    #         underline = True  

    def underline(self):
        #global underline
        i = self.textEdit.fontUnderline()
        if i == False:
            self.textEdit.setFontUnderline(True)
        elif i == True:
            self.textEdit.setFontUnderline(False)     

    def alignLeft(self):
        self.textEdit.setAlignment(Qt.AlignLeft) 

    def alignCenter(self):
        self.textEdit.setAlignment(Qt.AlignCenter)

    def alignRight(self):
        self.textEdit.setAlignment(Qt.AlignRight)

    def alignJustify(self):
        self.textEdit.setAlignment(Qt.AlignJustify) 

    def showTime(self):
        time = QTime.currentTime()
        self.textEdit.setText(time.toString(Qt.DefaultLocaleShortDate))  

    def showDate(self):
        date = QDate().currentDate()
        self.textEdit.setText(date.toString(Qt.DefaultLocaleLongDate))
        
        

        
        
        
            
             
        #self.statusbar.addWidget(label)
        #vv=date.toString(Qt.DefaultLocaleLongDate)
        #print(vv)
    def highlight(self):
        
        color = QColorDialog.getColor()
        if QColor.isValid(color):
            self.textEdit.setTextBackgroundColor(color)
       
    def CursorPosition(self):
       
        #self.textEdit.cursorPositionChanged(self.textEdit.textCursor().blockNumber())
        line = self.textEdit.textCursor().blockNumber()
        col = self.textEdit.textCursor().columnNumber()
        
        
        linecol = "Line: "+str(line)+" | "+"Column: "+str(col)
        
        # date = QDate().getDate()
        # label = QLabel()
        # vvv=str(date)
        # label.setText(vvv)
        # dat = QDate().getDate()
        # labl = QLabel()
        # vv=str(dat)
        # labl.setText(vv)
        
        # self.line = QFrame(self)
        # self.line.setFixedWidth(5)
        # self.line.setMinimumHeight(1)
        # self.line.setFrameShape(self.line.VLine)
        # self.line.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        # self.statusbar.move(100,1)
    
        # if self.width() < 800:
        #     fff = 800 - self.width()
        #     self.statusbar.showMessage(str(int(220-fff)*" ")+linecol)
        # elif self.width() > 800:
        #     fff = 800 + self.width()
        #     self.statusbar.showMessage(str(int(220-fff)*" ")+linecol)
        # elif self.width() == 800:
        #self.statusbar.setFixedWidth(800)
        if self.width() > 800:
            fff = 800 - self.width()
            ffff = abs(fff)
            self.statusbar.showMessage(str(int(220+(ffff/3))*" ")+linecol)
        elif self.width() < 800:
            fff = 800 - self.width()
            ffff = abs(fff)
            self.statusbar.showMessage(str(int(220-(ffff/3))*" ")+linecol)  
        else:
             self.statusbar.showMessage(str(220*" ")+linecol)             
        
        # else:    
        #     self.statusbar.showMessage(linecol)    
        #self.statusbar.showMessage(self.line,3000)

       # self.statusbar.showMessage(linecol)
        
        
        
       
        
        
        
        
        
    
            
               
        
        #self.statusbar.close()
        
        # print(type(vv))
        # if vv == None:
        #     vv = ""
        # else:
        #     self.statusbar.addPermanentWidget(linecol)

        
        
        
            
        #linecol.
        #linecol.setAlignment(Qt.AlignRight)
        
        #self.statusbar.removeWidget(linecol)
        #self.statusbar.addPermanentWidget(linecol.destroy())
        #self.statusbar.addPermanentWidget(linecol)
        
        

        #self.setLayout(QGridLayout)
        #if cc == True:
         #   self.statusbar.addPermanentWidget(linecol)
        
        #    cc = False
        #elif cc == False:
            #self.statusbar.removeWidget(linecol)
        #c= self.statusbar.showMessage("asdsad")   
        #self.statusbar.setStyleSheet("color:red")
       #self.statusbar.showMessage("adssad)
        
        
        
            #self.statusbar.removeWidget(linecol)
         #   cc == True        
        
      
        
           







