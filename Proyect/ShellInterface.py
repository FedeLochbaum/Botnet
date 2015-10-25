from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from Functions import setMessage
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
        listBoxCpu = self.create_listbox_cpu(self.pw)
        self.pw.add(listBoxCpu)
        
        self.pw.add(Label(self.pw, text="Answers", background='black', foreground='white'))
        listBoxInterruption = self.create_listbox_interruption(self.pw)
        self.pw.add(listBoxInterruption)
        
        self.pw.add(Label(self.pw, text="Connections", background='black', foreground='white'))
        listBoxIO = self.create_listbox_io(self.pw)
        self.pw.add(listBoxIO)
        
            
    def create_listbox_cpu(self, parent):
        f = ttk.Frame(parent)        
        self.listboxCpu = Listbox(f)
        vscroll = ttk.Scrollbar(f, orient=VERTICAL, command=self.listboxCpu.yview)
        self.listboxCpu['yscrollcommand'] = vscroll.set
        vscroll.pack(side=RIGHT, fill=Y)
        self.listboxCpu.pack(fill=BOTH, expand=Y)         
        return f      

    def create_listbox_io(self, parent):
        f = ttk.Frame(parent)        
        self.listboxIo = Listbox(f)
        vscroll = ttk.Scrollbar(f, orient=VERTICAL, command=self.listboxIo.yview)
        self.listboxIo['yscrollcommand'] = vscroll.set
        vscroll.pack(side=RIGHT, fill=Y)
        self.listboxIo.pack(fill=BOTH, expand=Y)         
        return f   
    
    def create_listbox_memory(self, parent):
        f = ttk.Frame(parent)        
        self.listboxMemory = Listbox(f)
        vscroll = ttk.Scrollbar(f, orient=VERTICAL, command=self.listboxMemory.yview)
        self.listboxMemory['yscrollcommand'] = vscroll.set
        vscroll.pack(side=RIGHT, fill=Y)
        self.listboxMemory.pack(fill=BOTH, expand=Y)         
        return f   
    
            
    def create_listbox_interruption(self, parent):        
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
                        
