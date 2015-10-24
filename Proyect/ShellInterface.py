from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

   
def build(typeScheduler, typeMemory, ios, configOs):
    ''
    
class Config:

    def __init__(self, parent, app):
        top = self.top = Toplevel(parent)
        top.title("Botnet Server Console")
        top.geometry("300x400")
        self.app = app
        
        self.createFrameForMemory(top)
        self.createFrameForScheduler(top)
        self.createFrameForIO(top)

        b = Button(top, text="Lunch OS!!", command=self.ok)
        b.pack()
    
    def createFrameForMemory(self, parent):
        self.mainFrameMemory = ttk.Frame(parent)
        #Titulo del mainFrame
        Label(self.mainFrameMemory, text="Memory", background='black', foreground='white').pack(fill=BOTH)
        ##Cuerpo
        self.createBodyForMemory()       
        self.mainFrameMemory.pack()
        
    def createBodyForMemory(self):
        # Size Memory
        Label(self.mainFrameMemory, text="Memory Size").pack()
        self.entrySizeMemory = Entry(self.mainFrameMemory)
        self.entrySizeMemory.pack()
        
        # Combobox TypeMemory
        Label(self.mainFrameMemory, text="Memory Type").pack()
        self.createComboboxForMemory()
        
    def createComboboxForMemory(self):
        frmComboboxMemory = ttk.Frame(self.mainFrameMemory)
        self.comboboxMemory = Combobox(frmComboboxMemory, text="Memory Type", values=None )
        self.comboboxMemory.bind("<<ComboboxSelected>>",self.updateMemory)
        self.comboboxMemory.pack()
        
        self.frmForUpdateMemory = ttk.Frame(self.mainFrameMemory)
        self.frmForUpdateMemory.pack(side=BOTTOM)
        
        frmComboboxMemory.pack(fill=BOTH)
    
    def updateMemory(self, event):
        for child in self.frmForUpdateMemory.winfo_children():
            child.destroy()
            
        value = self.comboboxMemory.get()
        
        if value == True:
            self.addToMainFrameMemoryContinuous()
        else:
            self.addToMainFrameMemoryPaging()
    
    def addToMainFrameMemoryContinuous(self):
        Label(self.frmForUpdateMemory, text="Allocation Methods").pack()
        self.comboboxAllocation = Combobox(self.frmForUpdateMemory, text="Fit", values=None)
        self.comboboxAllocation.pack()
    
    def addToMainFrameMemoryPaging(self):
        Label(self.frmForUpdateMemory, text="Page replacement").pack()
        self.comboboxPageReplacement = Combobox(self.frmForUpdateMemory, text="Page replacement", values=None)
        self.comboboxPageReplacement.pack()
        Label(self.frmForUpdateMemory, text="Frame size").pack()
        self.frameSize = Entry(self.frmForUpdateMemory)
        self.frameSize.pack()
    
    def createFrameForScheduler(self, parent):
        self.mainFrameScheduler = ttk.Frame(parent)
        #Titulo del mainFrame
        Label(self.mainFrameScheduler, text="Scheduler", background='black', foreground='white').pack(fill=BOTH)
        ##Cuerpo
        self.createBodyForScheduler()       
        self.mainFrameScheduler.pack()
        
    def createBodyForScheduler(self):
        # Combobox Scheduler
        Label(self.mainFrameScheduler, text="Scheduler Type").pack()
        self.createComboboxForScheduler()
        
    def createComboboxForScheduler(self):
        frmComboboxScheduler = ttk.Frame(self.mainFrameScheduler)
        self.comboboxScheduler = Combobox(frmComboboxScheduler, text="Scheduler Type", values=None)
        self.comboboxScheduler.bind("<<ComboboxSelected>>",self.updateScheduler)
        self.comboboxScheduler.pack()
        
        self.frmForUpdateScheduler = ttk.Frame(self.mainFrameScheduler)
        self.frmForUpdateScheduler.pack(side=BOTTOM)
        
        frmComboboxScheduler.pack(fill=BOTH)
                
    def updateScheduler(self, event):
        for child in self.frmForUpdateScheduler.winfo_children():
            child.destroy()
        value = self.comboboxScheduler.get()
        if value == True:
            self.addToMainFrameSchedulerFifo()
            return
        if value == True:
            self.addToMainFrameSchedulerRoundRobin()
            return
        if value == True:
            self.addToMainFrameSchedulerPriority()
            return
        if value == True:
            self.addToMainFrameSchedulerRRPriority()
            return    

    def addToMainFrameSchedulerFifo(self):
        return
    
    def addToMainFrameSchedulerRoundRobin(self):
        Label(self.frmForUpdateScheduler, text="Quantum").pack()
        self.roundRobinQuantum = Entry(self.frmForUpdateScheduler)
        self.roundRobinQuantum.pack()
        
    def addToMainFrameSchedulerPriority(self):
        Label(self.frmForUpdateScheduler, text="Aging").pack()
        self.aging = Entry(self.frmForUpdateScheduler,)
        self.aging.pack()        
        
    def addToMainFrameSchedulerRRPriority(self):
        Label(self.frmForUpdateScheduler, text="Quantum").pack()
        self.roundRobinQuantum = Entry(self.frmForUpdateScheduler,)
        self.roundRobinQuantum.pack()
        Label(self.frmForUpdateScheduler, text="Aging").pack()
        self.aging = Entry(self.frmForUpdateScheduler,)
        self.aging.pack()   
      
    def createFrameForIO(self, parent):
        self.mainFrameIO = ttk.Frame(parent)
        #Titulo del mainFrame
        Label(self.mainFrameIO, text="IO", background='black', foreground='white').pack(fill=BOTH)

        ##Cuerpo 
        Label(self.mainFrameIO, text= "IOS")
        self.ios = Entry(self.mainFrameIO)
        self.ios.pack()
        
        self.mainFrameIO.pack()
               
    def ok(self):
        self.createKernel()
        self.top.destroy()
        
    def createKernel(self):
        typeScheduler = self.comboboxScheduler.get() 
        typeMemory = self.comboboxMemory.get()
        ios = self.ios.get()
        build(typeScheduler, typeMemory, ios, self)
    
class StdoutRedirector(object):
    def __init__(self,text_widget):
        self.text_space = text_widget

    def write(self,string):
        self.text_space.insert('end', string)
        self.text_space.see('end')

class AppNew:
    
    def __init__(self, master=None):        
        self.titleApp = "Shell"
        self.pwd = "usuario@sistemas:~"
        self.move= "/"
        self.shell = None
        self.sizeWindowX = 1500
        self.sizeWindowY = 300       

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
        d = None
        self.root.wait_window(d)        
    
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
        
        self.pw.add(Label(self.pw, text="", background='black', foreground='white'))
        listBoxMemory = self.create_listbox_memory(self.pw)
        self.pw.add(listBoxMemory)
            
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
 
        top = self.createTextBox(pw)
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
    
    def createTextBox(self, frameParent):
        frmTextBox = ttk.Frame(frameParent)
        labelPwd = Label(frmTextBox, text="ServerConsole", background='black', foreground='white')
        labelPwd.pack(fill=BOTH)
        textBox = Entry(frmTextBox, width=60)
        textBox.bind('<Return>', self.getTextFromTextBox)
        textBox.pack(fill=BOTH)
        return frmTextBox
        
    def getTextFromTextBox(self, event):
        text = event.widget.get() 
        result  = self.shell.execCommand(text)
        print(self.pwd + self.move + text + '\n' + str(result))
        event.widget.delete(0, len(text))
                        
app = AppNew()
app.root.mainloop()