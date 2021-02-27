try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


class Toplevel2:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.l=[]
        self.temp=1
        for i in range(0,9):
            self.l.append(-99)
        
        self.l[8]="X"
        self.top=top
        top.geometry("651x668+355+26")
        top.title("New Toplevel")
        top.configure(background="#000000")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Button0 = tk.Button(top)
        self.Button0.place(relx=0.307, rely=0.344, height=70, width=70)
        self.Button0.configure(activebackground="#000000")
        self.Button0.configure(activeforeground="white")
        self.Button0.configure(background="#000000")
        self.Button0.configure(borderwidth="0")
        self.Button0.configure(command=self.fire0)
        self.Button0.configure(font="-family {DejaVu Sans} -size 48")
        self.Button0.configure(foreground="#ff0000")
        self.Button0.configure(highlightthickness="0")


        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.553, rely=0.344, height=70, width=70)
        self.Button2.configure(activebackground="#000000")
        self.Button2.configure(activeforeground="white")
        self.Button2.configure(background="#000000")
        self.Button2.configure(borderwidth="0")
        self.Button2.configure(command=self.fire2)
        self.Button2.configure(highlightthickness="0")

        self.Button5 = tk.Button(top)
        self.Button5.place(relx=0.553, rely=0.464, height=70, width=70)
        self.Button5.configure(activebackground="#000000")
        self.Button5.configure(activeforeground="white")
        self.Button5.configure(background="#000000")
        self.Button5.configure(borderwidth="0")
        self.Button5.configure(command=self.fire5)
        self.Button5.configure(highlightthickness="0")

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.43, rely=0.464, height=70, width=70)
        self.Button4.configure(activebackground="#000000")
        self.Button4.configure(activeforeground="white")
        self.Button4.configure(background="#000000")
        self.Button4.configure(borderwidth="0")
        self.Button4.configure(command=self.fire4)
        self.Button4.configure(highlightthickness="0")

        self.Button7 = tk.Button(top)
        self.Button7.place(relx=0.43, rely=0.584, height=70, width=70)
        self.Button7.configure(activebackground="#000000")
        self.Button7.configure(activeforeground="white")
        self.Button7.configure(background="#000000")
        self.Button7.configure(borderwidth="0")
        self.Button7.configure(command=self.fire7)
        self.Button7.configure(highlightthickness="0")

        self.Button8 = tk.Button(top)
        self.Button8.place(relx=0.553, rely=0.584, height=70, width=80)
        self.Button8.configure(activebackground="#000000")
        self.Button8.configure(activeforeground="white")
        self.Button8.configure(activeforeground="#ff0000")
        self.Button8.configure(background="#000000")
        self.Button8.configure(borderwidth="0")
        self.Button8.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
        self.Button8.configure(foreground="#ff0000")
        self.Button8.configure(highlightthickness="0")
        self.Button8.configure(text='''X''')
        self.Button8.configure(disabledforeground="#ff0000")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.292, rely=0.449, relheight=0.016, relwidth=0.386)
        self.Canvas1.configure(background="#9669ff")
        self.Canvas1.configure(highlightbackground="#0f1fff")
        self.Canvas1.configure(highlightthickness="0")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectborderwidth="0")

        self.Canvas1_9 = tk.Canvas(top)
        self.Canvas1_9.place(relx=0.292, rely=0.569, relheight=0.016, relwidth=0.386)
        self.Canvas1_9.configure(background="#9669ff")
        self.Canvas1_9.configure(highlightbackground="#0f1fff")
        self.Canvas1_9.configure(highlightthickness="0")
        self.Canvas1_9.configure(relief="ridge")
        self.Canvas1_9.configure(selectbackground="#c4c4c4")
        self.Canvas1_9.configure(selectborderwidth="0")

        self.Canvas2 = tk.Canvas(top)
        self.Canvas2.place(relx=0.415, rely=0.329, relheight=0.376
                , relwidth=0.017)
        self.Canvas2.configure(background="#9669ff")
        self.Canvas2.configure(highlightthickness="0")
        self.Canvas2.configure(relief="ridge")
        self.Canvas2.configure(selectbackground="#c4c4c4")

        self.Canvas2_11 = tk.Canvas(top)
        self.Canvas2_11.place(relx=0.538, rely=0.329, relheight=0.376
                , relwidth=0.017)
        self.Canvas2_11.configure(background="#9669ff")
        self.Canvas2_11.configure(highlightthickness="0")
        self.Canvas2_11.configure(relief="ridge")
        self.Canvas2_11.configure(selectbackground="#c4c4c4")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.092, rely=0.06, height=141, width=519)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(background="#000000")
        self.Label1.configure(font="-family {Ani} -size 48 -weight bold -slant italic")
        self.Label1.configure(foreground="#9669ff")
        self.Label1.configure(text='''Tic Tac Toe''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.43, rely=0.344, height=70, width=70)
        self.Button1.configure(activebackground="#000000")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(background="#000000")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(command=self.fire1)
        self.Button1.configure(font="-family {DejaVu Sans} -size 48")
        self.Button1.configure(foreground="#0011ff")
        self.Button1.configure(highlightthickness="0")

        self.Label1_5 = tk.Label(top)
        self.Label1_5.place(relx=0.215, rely=0.808, height=61, width=369)
        self.Label1_5.configure(activebackground="#000000")
        self.Label1_5.configure(background="#000000")
        self.Label1_5.configure(borderwidth="0")
        self.Label1_5.configure(font="-family {Ani} -size 48 ")
        self.Label1_5.configure(foreground="#02e202")
        self.Label1_5.configure(highlightthickness="0")
        self.Label1_5.configure(text='''Your Turn''')

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.307, rely=0.464, height=70, width=70)
        self.Button3.configure(activebackground="#000000")
        self.Button3.configure(activeforeground="white")
        self.Button3.configure(background="#000000")
        self.Button3.configure(borderwidth="0")
        self.Button3.configure(command=self.fire3)
        self.Button3.configure(highlightthickness="0")

        self.Button6 = tk.Button(top)
        self.Button6.place(relx=0.307, rely=0.584, height=70, width=70)
        self.Button6.configure(activebackground="#000000")
        self.Button6.configure(activeforeground="white")
        self.Button6.configure(background="#000000")
        self.Button6.configure(borderwidth="0")
        self.Button6.configure(command=self.fire6)
        self.Button6.configure(highlightthickness="0")

        self.Button2_1 = tk.Button(top)
        self.Button2_1.place(relx=0.866, rely=0.0, height=29, width=111)
        self.Button2_1.configure(activebackground="#f9f9f9")
        self.Button2_1.configure(background="#000000")
        self.Button2_1.configure(borderwidth="0")
        self.Button2_1.configure(font="-family {DejaVu Sans} -size 12 -slant italic")
        self.Button2_1.configure(foreground="#0aff5c")
        self.Button2_1.configure(highlightthickness="0")
        self.Button2_1.configure(text='''Reset''')
        self.Button2_1.configure(command=self.reset)


        self.Button34 = tk.Button(top)
        self.Button34.place(relx=0.0, rely=0.0, height=29, width=111)
        self.Button34.configure(background="#000000")
        self.Button34.configure(borderwidth="0")
        self.Button34.configure(font="-family {DejaVu Sans} -size 12 -slant italic")
        self.Button34.configure(foreground="#0aff5c")
        self.Button34.configure(highlightthickness="0")
        self.Button34.configure(text='''Main Menu''')
        self.Button34.configure(command=top.destroy)


    def reset(self):
        self.__init__(self.top)

    def fire0(self,a=-1):
        if(self.l[0]==-99):
            if(self.temp % 2 != 0):
                self.Button0.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button0.configure(foreground="#02e202")
                self.Button0.configure(text='''O''')
                self.Button0.configure(disabledforeground="#02e202")
            else:
                self.Button0.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button0.configure(foreground="#ff0000")
                self.Button0.configure(text='''X''')
                self.Button0.configure(disabledforeground="#ff0000")
            self.temp=self.temp+1
            print(0)
            self.fire(0,a)
            
    def fire1(self,a=-1):
        if(self.l[1]==-99):
            if(self.temp%2!=0):
                self.Button1.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button1.configure(foreground="#02e202")
                self.Button1.configure(text='''O''')
                self.Button1.configure(disabledforeground="#02e202")
            else:
                self.Button1.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button1.configure(foreground="#ff0000")
                self.Button1.configure(text='''X''')
                self.Button1.configure(disabledforeground="#ff0000")
            self.temp=self.temp+1
            print(1)
            self.fire(1,a)
            
    def fire2(self,a=-1):
        if(self.l[2]==-99):
            if(self.temp%2!=0):
                self.Button2.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button2.configure(foreground="#02e202")
                self.Button2.configure(text='''O''')
                self.Button2.configure(disabledforeground="#02e202")
            else:
                self.Button2.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button2.configure(foreground="#ff0000")
                self.Button2.configure(text='''X''')
                self.Button2.configure(disabledforeground="#ff0000")
            self.temp=self.temp+1
            print(2)
            self.fire(2,a)
            
    def fire3(self,a=-1):
        if(self.l[3]==-99):
            if(self.temp%2!=0):
                self.Button3.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button3.configure(foreground="#02e202")
                self.Button3.configure(text='''O''')
                self.Button3.configure(disabledforeground="#02e202")
            else:
                self.Button3.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button3.configure(foreground="#ff0000")
                self.Button3.configure(text='''X''')
                self.Button3.configure(disabledforeground="#ff0000")
            self.temp=self.temp+1
            print(3)
            self.fire(3,a)
            
    def fire4(self,a=-1):
        if(self.l[4]==-99):
            if(self.temp%2!=0):
                self.Button4.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button4.configure(foreground="#02e202")
                self.Button4.configure(text='''O''')
                self.Button4.configure(disabledforeground="#02e202")
            else:
                self.Button4.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button4.configure(foreground="#ff0000")
                self.Button4.configure(text='''X''')
                self.Button4.configure(disabledforeground="#ff0000")
            self.temp=self.temp+1
            print(4)
            self.fire(4,a)
            
    def fire5(self,a=-1):
        if(self.l[5]==-99):
            if(self.temp%2!=0):
                self.Button5.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button5.configure(foreground="#02e202")
                self.Button5.configure(text='''O''')
                self.Button5.configure(disabledforeground="#02e202")
            else:
                self.Button5.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button5.configure(foreground="#ff0000")
                self.Button5.configure(text='''X''')
                self.Button5.configure(disabledforeground="#ff0000")
            self.temp=self.temp+1
            print(5)
            self.fire(5,a)
            
    def fire6(self,a=-1):
        if(self.l[6]==-99):
            if(self.temp%2!=0):
                self.Button6.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button6.configure(foreground="#02e202")
                self.Button6.configure(text='''O''')
                self.Button6.configure(disabledforeground="#02e202")
            else:
                self.Button6.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button6.configure(foreground="#ff0000")
                self.Button6.configure(text='''X''')
                self.Button6.configure(disabledforeground="#ff0000")
            self.temp=self.temp+1
            print(6)
            self.fire(6,a)
            
    def fire7(self,a=-1):
        if(self.l[7]==-99):
            if(self.temp%2!=0):
                self.Button7.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button7.configure(foreground="#02e202")
                self.Button7.configure(text='''O''')
                self.Button7.configure(disabledforeground="#02e202")
            else:
                self.Button7.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button7.configure(foreground="#ff0000")
                self.Button7.configure(text='''X''')
                self.Button7.configure(disabledforeground="#ff0000")
            self.temp=self.temp+1
            print(7)
            self.fire(7,a)
            
        
    def check(self):
        if ((self.l[0] == self.l[3] == self.l[6] != -99) or (self.l[1] == self.l[4] == self.l[7]  != -99) or (self.l[2] == self.l[5] == self.l[8]  != -99) or (self.l[0] ==self.l[1] ==self.l[2]  != -99) or (self.l[3] ==self.l[4] == self.l[5]  != -99) or (self.l[6] == self.l[7] == self.l[8]  != -99) or (self.l[0] == self.l[4] == self.l[8]  != -99) or (self.l[2] == self.l[4] ==self.l[6]  != -99) ):
            return True
        else :
            return False

    def fire(self,a,b):
        if(self.l[a]==-99):
            if((self.temp-1)%2!=0):
                self.l[a]='O'
            else:
                self.l[a]='X'
        print self.l
        if(self.check()):
            if(b==-1):
                self.Label1_5.configure(text='''You Won''')
                print("You Won")
            else:
                self.Canvas1.configure(background="#ff0000")
                self.Canvas1_9.configure(background="#ff0000")
                self.Canvas2.configure(background="#ff0000")
                self.Canvas2_11.configure(background="#ff0000")
                self.Label1_5.configure(foreground="#ff088c")
                self.Label1_5.configure(text='''You Lose''')
                print("You Lose")
            self.Button0.configure(state = "disabled")
            self.Button1.configure(state = "disabled")
            self.Button2.configure(state = "disabled")
            self.Button3.configure(state = "disabled")
            self.Button4.configure(state = "disabled")
            self.Button5.configure(state = "disabled")
            self.Button6.configure(state = "disabled")
            self.Button7.configure(state = "disabled")
            self.Button8.configure(state = "disabled")
        if(b==-1):
            self.auto()


    def auto(self):
        print ("enter")
        if((self.l[2]=='O'  or  self.l[6]=='O' ) and self.temp==2):
            self.fire0(12)
            return
        if((self.l[0]=='X' and self.l[4]==-99 and  self.temp==4)):
            self.fire4(12)
            return
        if((self.l[0]=='X' and self.l[4]=='O' and self.temp==4)):
            if(self.l[2]!='O'):
                self.fire2(12)
                return
            else:
                self.fire6(12)
                return
        if((self.l[0]==self.l[6]==self.l[8]=='X' ) and self.temp==6):
            if(self.l[3]==-99):
                self.fire3(12)
                return
            else:
                self.fire7(12)
                return
        if((self.l[0]==self.l[2]==self.l[8]=='X' ) and self.temp==6):
            if(self.l[1]==-99):
                self.fire1(12)
                return
            else:
                self.fire5(12)
                return
        if((self.l[3]=='O' or self.l[5]=='O') and self.temp==2):
            self.fire6(12)
            return
        if((self.l[6]=='X') and (self.l[3]=='O' or self.l[5]=='O') and self.temp==4):
            if(self.l[7]==-99):
                self.fire7(12)
                return
            else:
                self.fire4(12)
                return
        if((self.l[4]==self.l[6]==self.l[8]=='X') and self.temp==6):
            if(self.l[0]==-99):
                self.fire0(12)
                return
            else:
                self.fire2(12)
                return
        if((self.l[1]=='O' or self.l[7]=='O') and self.temp==2):
            self.fire2(12)
            return
        if((self.l[2]=='X') and (self.l[1]=='O' or self.l[7]=='O') and self.temp==4):
            if(self.l[5]==-99):
                self.fire5(12)
                return
            else:
                self.fire4(12)
                return
        if((self.l[4]==self.l[2]==self.l[8]=='X') and (self.l[1]=='O' or self.l[7]=='O') and self.temp==6):
            if(self.l[0]==-99):
                self.fire0(12)
                return
            else:
                self.fire6(12)
                return
        if(self.l[0]=='O' and self.temp==2):
            self.fire6(12)
            return
        if((self.l[6]=='X') and self.l[0]=='O' and self.temp==4):
            if(self.l[7]==-99):
                self.fire7(12)
                return
            else:
                self.fire2(12)
                return
        if((self.l[6]==self.l[2]==self.l[8]=='X') and self.l[0]=='O' and self.temp==6):
            print ("yaya0")
            if(self.l[4]==-99):
                self.fire4(12)
                return
            else:
                self.fire5(12)
                return
        if(self.l[4]=='O' and self.temp==2):
            self.fire0(12)
            return
        if((self.l[0]=='X' and (self.l[4]==self.l[2]=='O' or self.l[4]==self.l[6]=='O'))and self.temp==4):
            if(self.l[2]==-99):
                self.fire2(12)
                return
            else:
                self.fire6(12)
                return
        if((self.l[6]==self.l[0]==self.l[8]=='X') and self.l[4]==self.l[2]=='O' and self.temp==6):
            if(self.l[3]==-99):
                self.fire3(12)
                return
            else:
                self.fire7(12)
                return
        if((self.l[2]==self.l[0]==self.l[8]=='X') and self.l[4]==self.l[6]=='O' and self.temp==6):
            if(self.l[1]==-99):
                self.fire1(12)
                return
            else:
                self.fire5(12)
                return




class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x493+444+109")
        top.title("New Toplevel")
        top.configure(background="#000000")
        top.configure(highlightcolor="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.267, rely=0.385, height=47, width=266)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(background="#000000")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(compound='bottom')
        self.Button1.configure(disabledforeground="#08f7ff")
        self.Button1.configure(font="-family {Century Schoolbook L} -size 12 -weight bold -slant italic")
        self.Button1.configure(foreground="#ffff0f")
        self.Button1.configure(highlightbackground="#ffff0f")
        self.Button1.configure(highlightcolor="#00ffff")
        self.Button1.configure(highlightthickness="2")
        self.Button1.configure(text='''New Game''')
        self.Button1.configure(command=game)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.117, rely=0.081, height=101, width=459)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(background="#000000")
        self.Label1.configure(font="-family {Ani} -size 48 -weight bold -slant italic")
        self.Label1.configure(foreground="#9669ff")
        self.Label1.configure(text='''Tic Tac Toe''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Button1_4 = tk.Button(top)
        self.Button1_4.place(relx=0.267, rely=0.487, height=47, width=266)
        self.Button1_4.configure(activebackground="#f9f9f9")
        self.Button1_4.configure(background="#000000")
        self.Button1_4.configure(borderwidth="0")
        self.Button1_4.configure(compound='bottom')
        self.Button1_4.configure(disabledforeground="#08f7ff")
        self.Button1_4.configure(font="-family {Century Schoolbook L} -size 12 -weight bold -slant italic")
        self.Button1_4.configure(foreground="#ff00e6")
        self.Button1_4.configure(highlightbackground="#ff00e6")
        self.Button1_4.configure(highlightcolor="#ff3061")
        self.Button1_4.configure(highlightthickness="2")
        self.Button1_4.configure(text='''Multi Player''')

        self.Button1_6 = tk.Button(top)
        self.Button1_6.place(relx=0.267, rely=0.69, height=47, width=266)
        self.Button1_6.configure(activebackground="#f9f9f9")
        self.Button1_6.configure(background="#000000")
        self.Button1_6.configure(borderwidth="0")
        self.Button1_6.configure(compound='bottom')
        self.Button1_6.configure(disabledforeground="#08f7ff")
        self.Button1_6.configure(font="-family {Century Schoolbook L} -size 12 -weight bold -slant italic")
        self.Button1_6.configure(foreground="#0000ff")
        self.Button1_6.configure(highlightbackground="#0000ff")
        self.Button1_6.configure(highlightcolor="#0dcfff")
        self.Button1_6.configure(highlightthickness="2")
        self.Button1_6.configure(text='''Exit''')
        self.Button1_6.configure(command=root.destroy)

        self.Button1_3 = tk.Button(top)
        self.Button1_3.place(relx=0.267, rely=0.588, height=47, width=266)
        self.Button1_3.configure(activebackground="#f9f9f9")
        self.Button1_3.configure(background="#000000")
        self.Button1_3.configure(borderwidth="0")
        self.Button1_3.configure(compound='bottom')
        self.Button1_3.configure(disabledforeground="#08f7ff")
        self.Button1_3.configure(font="-family {Century Schoolbook L} -size 12 -weight bold -slant italic")
        self.Button1_3.configure(foreground="#ff0000")
        self.Button1_3.configure(highlightbackground="#ff0000")
        self.Button1_3.configure(highlightcolor="#ff0000")
        self.Button1_3.configure(highlightthickness="2")
        self.Button1_3.configure(text='''High Score''')



def game():
        window=Toplevel2(tk.Toplevel())
    
root=tk.Tk()
t=Toplevel1(root)

root.mainloop()