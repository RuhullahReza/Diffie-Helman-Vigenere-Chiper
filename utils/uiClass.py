import tkinter

root = tkinter.Tk()
root.title('DIFFIE HELLMAN')
canvas = tkinter.Canvas(root, width=1150,height=600)
canvas.pack()

class InputBox:
    def __init__(self,text,x,y,z=0,w=100):
        self.label = tkinter.Label(root,text=text)
        canvas.create_window(x,y,window=self.label)      
        self.entry = tkinter.Entry(root)
        canvas.create_window(x,y+20,width=w,window=self.entry)

    def getEntry(self):
        return self.entry.get()
    
    def setValue(self,text):
        return self.entry.insert(0, text)

    def clearValue(self):
        return self.entry.delete(0, tkinter.END)

class OutputBox:
    def __init__(self,text,x,y):
        self.label = tkinter.Label(root, text=text)
        canvas.create_window(x,y,window=self.label)

class ProcessButton:
    def __init__(self,text,command,x,y):
        self.button = tkinter.Button(text=text,command=command)
        canvas.create_window(x,y,window=self.button)
