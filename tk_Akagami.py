from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math


class App(Frame):
    def __init__(self ,master = Tk()):
        self.master = master
        self.bgImg = PhotoImage(file=r'RedHair.png')
        
        
    def settings(self):
        self.master.geometry('280x340')
        self.master.minsize(280,340)
        self.master.maxsize(280,340)
        self.master.title('Akagami Calculator')
        self.master.iconbitmap('icon.ico')
        self.master.configure(bg='black')
        
    def widgets(self):
        self.bg = Label(self.master,image=self.bgImg).place(x=-3,y=-3)
        self.equation = StringVar()
        self.entry = Entry(self.master,textvariable=self.equation,width=46,font='courier 25 bold').place(x=0,y=0)
        def Equals():
            result = ''
            interp = {'^':'**','√':'math.sqrt','%':'/100'}
            for char in self.equation.get():
                result += interp.get(char, char)
            try:
                if len(str(eval(result))) > 14:
                    messagebox.showinfo(title='Result',message=str(eval(result)))
                else:
                    self.equation.set(str(eval(result)))
            except SyntaxError:
                self.equation.set('Error')
        #1st_row
        self.pow = Button(self.master,text='^',command=lambda:self.equation.set(self.equation.get()+'^'),fg='white',bg='gray25',width=3,font='verdana 15 bold',relief='flat').place(x=5,y=50)
        self.brao = Button(self.master,text='(',command=lambda:self.equation.set(self.equation.get()+'('),fg='white',bg='gray25',width=3,font='verdana 15 bold',relief='flat').place(x=60,y=50)
        self.brac = Button(self.master,text=')',command=lambda:self.equation.set(self.equation.get()+')'),fg='white',bg='gray25',width=3,font='verdana 15 bold',relief='flat').place(x=115,y=50)
        self.ae = Button(self.master,text='AC',command=lambda:self.equation.set(''),fg='white',bg='green3',width=3,font='verdana 15 bold',relief='flat').place(x=170,y=50)
        self.ce = Button(self.master,text='CE',command=lambda:self.equation.set(self.equation.get()[:-1]),fg='white',bg='green3',width=3,font='verdana 15 bold',relief='flat').place(x=225,y=50)
        #2nd_Row 
        self.seven = Button(self.master,text='7',command=lambda:self.equation.set(self.equation.get()+'7'),fg='white',bg='gray25',width=3,font='verdana 15 bold',relief='flat').place(x=5,y=100)
        self.eight = Button(self.master,text='8',command=lambda:self.equation.set(self.equation.get()+'8'),fg='white',bg='gray25',width=3,font='verdana 15 bold',relief='flat').place(x=60,y=100)
        self.nine = Button(self.master,text='9',command=lambda:self.equation.set(self.equation.get()+'9'),fg='white',bg='gray25',width=3,font='verdana 15 bold',relief='flat').place(x=115,y=100)
        self.plus = Button(self.master,text='+',command=lambda:self.equation.set(self.equation.get()+'+'),fg='white',bg='royalblue4',width=3,font='verdana 15 bold',relief='flat').place(x=170,y=100)
        self.sqrt = Button(self.master,text='√',command=lambda:self.equation.set(self.equation.get()+'√('),fg='white',bg='gray25',width=3,font='verdana 15 bold',relief='flat').place(x=225,y=100)
        #3rd_Row
        self.four = Button(self.master,text='4',command=lambda:self.equation.set(self.equation.get()+'4'),fg='white',bg='gray25',width=3,font='verdana 15 bold',relief='flat').place(x=5,y=150)
        self.five = Button(self.master,text='5',command=lambda:self.equation.set(self.equation.get()+'5'),fg='white',bg='gray25',width=3,font='verdana 15 bold',relief='flat').place(x=60,y=150)
        self.six = Button(self.master,text='6',command=lambda:self.equation.set(self.equation.get()+'6'),fg='white',bg='gray25',width=3,font='verdana 15 bold',relief='flat').place(x=115,y=150)
        self.sub = Button(self.master,text='-',command=lambda:self.equation.set(self.equation.get()+'-'),fg='white',bg='royalblue4',width=3,font='verdana 15 bold',relief='flat').place(x=170,y=150)
        self.mod = Button(self.master,text='%',command=lambda:self.equation.set(self.equation.get()+'%'),fg='white',bg='gray25',width=3,font='verdana 15 bold',relief='flat').place(x=225,y=150)
        #4th_row
        self.one = Button(self.master,text='1',command=lambda:self.equation.set(self.equation.get()+'1'),fg='white',bg='gray25',width=3,font='verdana 15 bold',relief='flat').place(x=5,y=200)
        self.two = Button(self.master,text='2',command=lambda:self.equation.set(self.equation.get()+'2'),fg='white',bg='gray25',width=3,font='verdana 15 bold',relief='flat').place(x=60,y=200)
        self.three = Button(self.master,text='3',command=lambda:self.equation.set(self.equation.get()+'3'),fg='white',bg='gray25',width=3,font='verdana 15 bold',relief='flat').place(x=115,y=200)
        self.mult = Button(self.master,text='*',command=lambda:self.equation.set(self.equation.get()+'*'),fg='white',bg='royalblue4',width=3,font='verdana 15 bold',relief='flat').place(x=170,y=200)
        self.equals = Button(self.master,text='\n=\n',command=Equals,fg='white',bg='red3',width=3,font='verdana 15 bold',relief='flat').place(x=225,y=200)
        #5th_row
        self.zero = Button(self.master,text='0',command=lambda:self.equation.set(self.equation.get()+'0'),fg='white',bg='gray25',width=7,font='verdana 15 bold',relief='flat').place(x=5,y=250)
        self.dot = Button(self.master,text='.',command=lambda:self.equation.set(self.equation.get()+'.'),fg='white',bg='gray25',width=3,font='verdana 15 bold',relief='flat').place(x=115,y=250)
        self.div = Button(self.master,text='/',command=lambda:self.equation.set(self.equation.get()+'/'),fg='white',bg='royalblue4',width=3,font='verdana 15 bold',relief='flat').place(x=170,y=250)


app = App()
app.settings()
app.widgets()
mainloop()
