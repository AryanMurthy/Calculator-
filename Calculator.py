from tkinter import *
def Calci(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="AntiqueWhite2")
    storeObj.pack(side=side, expand =YES, fill =BOTH)
    return storeObj
 
def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand = YES, fill=BOTH)
    return storeObj

class app(Frame):
    
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'TimesNewRoman 20 bold')
        self.pack(expand = YES, fill =BOTH)
        self.master.title('Sahu_Calculator')
 
        display = StringVar()
        Entry(self, relief=RAISED, textvariable=display,justify='left', bd=30, bg="AntiqueWhite2").pack(side=TOP,expand=YES, fill=BOTH)
 
        for clearButton in (["C"]):
            erase = Calci(self, TOP)
            for char in clearButton:
                button(erase, LEFT, char, lambda
                    storeObj=display, q=char: storeObj.set(""))
 
        for numButton in ("789/", "456*", "123-", "0.+"):
         FunctionNum = Calci(self, TOP)
         for Equals in numButton:
            button(FunctionNum, LEFT, Equals, lambda
                storeObj=display, q=Equals: storeObj
                   .set(storeObj.get() + q))
 
        EqualButton = Calci(self, TOP)
        for Equals in "=":
            if Equals == '=':
                btnEquals = button(EqualButton, LEFT, Equals)
                btnEquals.bind('<ButtonRelease-1>', lambda e,s=self,
                                storeObj=display: s.calc(storeObj), '+')
 
 
            else:
                btnEquals = button(EqualButton, LEFT, iEquals,
                                    lambda storeObj=display, s=' %s ' % Equals: storeObj.set
                                    (storeObj.get() + s))
 
    def calc(self, display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("ERROR")
 
 
if __name__=='__main__':
 app().mainloop()