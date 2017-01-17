from Tkinter import * 
import csv

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.output()
    def output(self):
        Label(text='Name:').pack    (side=LEFT,padx=5,pady=5)
        self.e = Entry(root, width=10)
        self.e.pack(side=LEFT,padx=5,pady=5)
        Label(text='Age:').pack    (side=LEFT,padx=5,pady=5)
        self.e1 = Entry(root, width=10)
        self.e1.pack(side=LEFT,padx=5,pady=5)
        Label(text='Gender:').pack    (side=LEFT,padx=5,pady=5)
        self.e2 = Entry(root, width=10)
        self.e2.pack(side=LEFT,padx=5,pady=5)
        Label(text='Education level:').pack    (side=LEFT,padx=5,pady=5)
        self.e3 = Entry(root, width=10)
        self.e3.pack(side=LEFT,padx=5,pady=5)
        Label(text='Social network name:').pack    (side=LEFT,padx=5,pady=5)
        self.e4 = Entry(root, width=10)
        self.e4.pack(side=LEFT,padx=5,pady=5)
        self.b = Button(root, text='Submit',command=self.writeToFile)
        self.b.pack(side=LEFT,padx=5,pady=5)
       
    def writeToFile(self):
        with open("Output.txt", "w") as text_file:
            text_file.write("%s " % self.e.get())
            text_file.write("%s " % self.e1.get())
            text_file.write("%s " % self.e2.get())
            text_file.write("%s " % self.e3.get())
            text_file.write("%s " % self.e4.get())
            root.destroy()
        
        #with open('WorkOrderLog.csv', 'w') as f:
         #   w=csv.writer(f, delimiter=',')
          #  w.writerow([self.e.get()])
           # w.writerow([self.e1.get()])
            #w.writerow([self.e2.get()])
            #w.writerow([self.e3.get()])
           # w.writerow([self.e4.get()])

if __name__ == "__main__":
    root=Tk()
    root.title('Sentiment Analysis')
    root.geometry('900x200')
    ms = "WELCOME"
    msg = Message(root, text = ms)
    msg.config(font = ('times', 19, 'italic'))
    msg.pack()
    app=App(master=root)
    app.mainloop()
    root.mainloop()
