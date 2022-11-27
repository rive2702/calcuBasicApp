from tkinter import Label, Entry, Button, Tk, Frame, ttk
from tkinter import messagebox as MessageBox
from tkinter.ttk import*

class Calc(Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.gui()  
        self.__tries = 3

    def add(self):
        self.__n1 = self.__n1_e.get()
        self.__n2 = self.__n2_e.get()
        self.checking()
        self.r = float(self.__n1) + float(self.__n2)
        self.__ans_e.delete(0, 'end')
        self.__ans_e.insert(0, self.r)
        #self.__num1_ent.delete(0, 'end')
        #self.__num2_ent.delete(0, 'end')
        
    def substract(self):
        self.__n1 = self.__n1_e.get()
        self.__n2 = self.__n2_e.get()
        self.checking()
        self.r = float(self.__n1) - float(self.__n2)
        self.__ans_e.delete(0, 'end')
        self.__ans_e.insert(0, self.r)
        #self.__num1_ent.delete(0, 'end')
        #self.__num2_ent.delete(0, 'end')     

    def multi(self):
        self.__n1 = self.__n1_e.get()
        self.__n2 = self.__n2_e.get()
        self.checking()
        self.r = float(self.__n1) * float(self.__n2)
        self.__ans_e.delete(0, 'end')
        self.__ans_e.insert(0, self.r)
        #self.__num1_ent.delete(0, 'end')
        #self.__num2_ent.delete(0, 'end')
        
    def divi(self):
        self.__n1 = self.__n1_e.get()
        self.__n2 = self.__n2_e.get()
        self.checking()
        self.r = float(self.__n1) / float(self.__n2)
        self.__ans_e.delete(0, 'end')
        self.__ans_e.insert(0, self.r)   
        #self.__num1_ent.delete(0, 'end')
        #self.__num2_ent.delete(0, 'end')
  
    def checking(self):
        try:
            float(self.__n1)
            float(self.__n2)
        except:
            if self.__intents > 0:
                MessageBox.showinfo('Invalid characters', f'Try again with numeric characters. Remaining attempts: {self.__intents}')
                self.__tries-=1
            else:
                MessageBox.showerror('ERROR', 'attempt limit exceeded. Closing App')  
                self.quit()   

    def gui(self):
        
        b = ttk.Style()
        b.configure(
            "button.TButton",
            foreground='black',
            font=('Helvetica', 10),
            anchor='center',
        )
        b.map("button.TButton",
            foreground=[('pressed', 'red'), ('active', 'blue')],
            background=[('pressed', 'black'), ('active', 'white')]
        )

        l = ttk.Style()
        l.configure(
            'label.TLabel',
            font=('Helvetica', 10),
            anchor='E'
        )

        e = ttk.Style()
        e.configure(
            'entry.TEntry',
            font=('Helvetica', 10),
            background="#ccd",
        )
            
        #Labels & Entries
        self.__n1_l = ttk.Label(self, text='1st number:', style='label.TLabel')
        self.__n1_e = ttk.Entry(self, width=10, justify='center', style='entry.TEntry')
        self.__n2_l = ttk.Label(self, text='2nd number:', style='label.TLabel')
        self.__n2_e = ttk.Entry(self, width=10, justify='center', style='entry.TEntry')
        self.__ans_l = ttk.Label(self, text='Result:', style='label.TLabel')
        self.__ans_e = ttk.Entry(self, width=15, justify='center', style='entry.TEntry')
        #Operation Buttons
        self.__add_b = ttk.Button(self, text='Add', width=9, command=self.add, cursor='hand2', style='button.TButton')
        self.__subs_b = ttk.Button(self, text='Substract', width=9, command=self.substract, cursor='hand2', style='button.TButton')
        self.__multi_b = ttk.Button(self, text='Multiply', width=9, command=self.multi, cursor='hand2', style='button.TButton')
        self.__divi_b = ttk.Button(self, text='Divide', width=9, command=self.divi, cursor='hand2', style='button.TButton')
        #Labels & Entries pack&grid
        self.__n1_l.grid(column=0, row=0, pady=5)
        self.__n2_l.grid(column=0, row=1, pady=5)
        self.__ans_l.grid(column=0, row=2, columnspan=2)
        self.__n1_e.grid(column=1, row=0, padx=5, pady=5)
        self.__n2_e.grid(column=1, row=1, padx=5, pady=5)
        self.__ans_e.grid(column=0, row=3, padx=5, pady=5, columnspan=2)
        #Operation Buttons grid&pack
        self.__add_b.grid(column=3, row=0, padx=5, pady=0)
        self.__subs_b.grid(column=3, row=1, padx=5, pady=0)
        self.__multi_b.grid(column=3, row=2, padx=5, pady=2)
        self.__divi_b.grid(column=3, row=3, padx=5, pady=2)

if __name__ == '__main__':
    root = Tk(className='Calc POO+Tkinter')
    root.title('Calc POO+Tkinter')
    root.geometry('270x130')
    root.resizable(0, 0)
    root['bg']='#ccd'
    root.bind("<Escape>", lambda e:quit())
    app = Calc(root)
    app.mainloop()