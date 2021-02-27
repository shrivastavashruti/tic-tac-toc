try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
import socket
import select
import threading
import time


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.top=top
        top.geometry("600x493+444+109")
        top.title("New Toplevel")
        top.configure(background="#000000")
        top.configure(highlightcolor="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.267, rely=0.446, height=47, width=266)
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
        self.Button1.configure(text='''Host Game (Server)''')
        self.Button1.configure(command=self.host)

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
        self.Button1_4.place(relx=0.267, rely=0.588, height=47, width=266)
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
        self.Button1_4.configure(text='''Connect (Client)''')
        self.Button1_4.configure(command=self.cli)






    def host(self):
    	self.Button1.destroy()
    	self.Button1_4.destroy()
    	self.Label1.destroy()
    	w=multi(self.top)



    def cli(self):
    	self.Button1.destroy()
    	self.Button1_4.destroy()
    	self.Label1.destroy()
    	q=client(self.top)


class multi:
    def __init__(self, top=None):
		font9 = "-family {DejaVu Sans} -size 24 -weight normal -slant roman -underline 0 -overstrike 0"
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85'
		_ana2color = '#ececec' # Closest X11 color: 'gray92'
		self.top=top
		self.acpt=False
		top.geometry("651x668+355+26")
		top.title("New Toplevel")
		top.configure(background="#000000")
		top.configure(highlightcolor="black")

		self.Label1 = tk.Label(top)
		self.Label1.place(relx=0.092, rely=0.06, height=141, width=519)
		self.Label1.configure(activebackground="#f9f9f9")
		self.Label1.configure(background="#000000")
		self.Label1.configure(font="-family {Ani} -size 48 -weight bold -slant italic")
		self.Label1.configure(foreground="#9669ff")
		self.Label1.configure(text='''Tic Tac Toe''')


		self.Label1_5 = tk.Label(top)
		self.Label1_5.place(relx=0.03, rely=0.808, height=61, width=609)
		self.Label1_5.configure(activebackground="#000000")
		self.Label1_5.configure(background="#000000")
		self.Label1_5.configure(borderwidth="0")
		self.Label1_5.configure(font="-family {Ani} -size 48 ")
		self.Label1_5.configure(foreground="#ff0000")
		self.Label1_5.configure(highlightthickness="0")
		self.Label1_5.configure(text='''Waiting for Player''')


		self.Message11 = tk.Message(self.top)
		self.Message11.place(relx=0.15, rely=0.304, relheight=0.355, relwidth=0.687)
		self.Message11.configure(background="#000000")
		self.Message11.configure(borderwidth="0")
		self.Message11.configure(font=font9)
		self.Message11.configure(foreground="#ffffff")
		self.Message11.configure(highlightthickness="0")
		self.Message11.configure(width=412)
		self.t=threading.Thread(target=self.recieve, args=())
		self.t.start()




    def recieve(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.s.bind(('', 6757 ))
		self.Message11.configure(text='''Game Hosted at: ''')
		while True:
			tsoc, _, _=select.select([self.s],[],[],5)
			if (self.acpt):
				self.s.close()
				print('udp soc closed')
				return
			if tsoc:
				for i in tsoc:
					data, addr = i.recvfrom(1024)
					print (data,addr)
					if(addr==None):
						break
					t1 = threading.Thread(target=self.acno, args=(data,addr,))
					t1.setDaemon(True)
					t1.start()

    def acno(self,d,a):
    	if(d=='s'):
        	self.s.sendto('y',a)
        if(d=='j'):
        	self.req(tk.Toplevel(),a)



    def accept(self,a,t):
    	self.s.sendto('yes',a)
    	self.Label1.destroy()
    	self.Label1_5.destroy()
    	self.Message11.destroy()
    	t.destroy()
    	self.acpt=True
    	self.game(a)






    def req(self,top,a):
		print('View')

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


		self.Label1 = tk.Label(top)
		self.Label1.place(relx=0.117, rely=0.081, height=101, width=459)
		self.Label1.configure(activebackground="#f9f9f9")
		self.Label1.configure(background="#000000")
		self.Label1.configure(font="-family {Ani} -size 48 -weight bold -slant italic")
		self.Label1.configure(foreground="#9669ff")
		self.Label1.configure(text='''Tic Tac Toe''')


		font9 = "-family {DejaVu Sans} -size 24 -weight normal -slant roman -underline 0 -overstrike 0"

		self.Button11 = tk.Button(top)
		self.Button11.place(relx=0.083, rely=0.771, height=47, width=226)
		self.Button11.configure(activebackground="#f9f9f9")
		self.Button11.configure(background="#000000")
		self.Button11.configure(borderwidth="0")
		self.Button11.configure(compound='bottom')
		self.Button11.configure(disabledforeground="#08f7ff")
		self.Button11.configure(font="-family {Century Schoolbook L} -size 12 -weight bold -slant italic")
		self.Button11.configure(foreground="#ffff0f")
		self.Button11.configure(highlightbackground="#ffff0f")
		self.Button11.configure(highlightcolor="#00ffff")
		self.Button11.configure(highlightthickness="2")
		self.Button11.configure(state='active')
		self.Button11.configure(text='''Accept''')
		self.Button11.configure(command=lambda:self.accept(a,top) )


		self.Button01 = tk.Button(top)
		self.Button01.place(relx=0.533, rely=0.771, height=47, width=236)
		self.Button01.configure(activebackground="#f9f9f9")
		self.Button01.configure(background="#000000")
		self.Button01.configure(borderwidth="0")
		self.Button01.configure(compound='bottom')
		self.Button01.configure(disabledforeground="#08f7ff")
		self.Button01.configure(font="-family {Century Schoolbook L} -size 12 -weight bold -slant italic")
		self.Button01.configure(foreground="#ff00e6")
		self.Button01.configure(highlightbackground="#ff00e6")
		self.Button01.configure(highlightcolor="#ff3061")
		self.Button01.configure(highlightthickness="2")
		self.Button01.configure(text='''Reject''')
		self.Button01.configure(command=top.destroy)

		self.Message11 = tk.Message(top)
		self.Message11.place(relx=0.15, rely=0.304, relheight=0.355, relwidth=0.687)
		self.Message11.configure(background="#000000")
		self.Message11.configure(borderwidth="4")
		self.Message11.configure(font=font9)
		self.Message11.configure(foreground="#ffffff")
		self.Message11.configure(highlightthickness="1")
		self.Message11.configure(text='Would you like to join :' + str(a[0]))
		self.Message11.configure(width=412)




    def game(self,addr):

		top=self.top


		font9 = "-family {DejaVu Sans} -size 24 -weight normal -slant roman -underline 0 -overstrike 0"
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85'
		_ana2color = '#ececec' # Closest X11 color: 'gray92'
		self.l=[]
		self.temp=0
		for i in range(0,9):
		    self.l.append(-99)

		top.geometry("651x668+355+26")
		top.title("New Toplevel")
		top.configure(background="#000000")
		top.configure(highlightcolor="black")

		self.Label1 = tk.Label(top)
		self.Label1.place(relx=0.092, rely=0.06, height=141, width=519)
		self.Label1.configure(activebackground="#f9f9f9")
		self.Label1.configure(background="#000000")
		self.Label1.configure(font="-family {Ani} -size 48 -weight bold -slant italic")
		self.Label1.configure(foreground="#9669ff")
		self.Label1.configure(text='''Tic Tac Toe''')


		self.Label1_5 = tk.Label(top)
		self.Label1_5.place(relx=0.03, rely=0.808, height=61, width=609)
		self.Label1_5.configure(activebackground="#000000")
		self.Label1_5.configure(background="#000000")
		self.Label1_5.configure(borderwidth="0")
		self.Label1_5.configure(font="-family {Ani} -size 48 ")
		self.Label1_5.configure(foreground="#ff0000")
		self.Label1_5.configure(highlightthickness="0")
		self.Label1_5.configure(text='''Waiting for Player''')



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
		self.Button8.configure(disabledforeground="#ff0000")
		self.Button8.configure(command=self.fire8)
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
		self.Button2_1.configure(command=lambda:self.reset(addr))
		self.Button34 = tk.Button(top)
		self.Button34.place(relx=0.0, rely=0.0, height=29, width=111)
		self.Button34.configure(background="#000000")
		self.Button34.configure(borderwidth="0")
		self.Button34.configure(font="-family {DejaVu Sans} -size 12 -slant italic")
		self.Button34.configure(foreground="#0aff5c")
		self.Button34.configure(highlightthickness="0")
		self.Button34.configure(text='''Main Menu''')
		self.Button34.configure(command=top.destroy)
		self.turn=['ts','tc']
		self.f=[self.fire0,self.fire1,self.fire2,self.fire3,self.fire4,self.fire5,self.fire6,self.fire7,self.fire8]
		self.t=0
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.s.bind(('', 6757)) 
		self.s.listen(1)
		t1 = threading.Thread(target=self.soc, args=())
		t1.setDaemon(True)
		t1.start()




    def soc(self):
		self.c, addr = self.s.accept()
		self.c.send(self.turn[self.t])
		self.go=False
		if(self.t==0):
			self.Label1_5.configure(text='''Your Turn''')
		else:
			self.disbut()
			self.Label1_5.configure(text='''Opponent Turn''')
		self.t=(self.t+1)%2
		
		if(self.t == 1):
			while True:
				self.acpt=True
				self.Label1_5.configure(text='''Your Turn''')
				while True:
					if(self.acpt==False):
						break
				time.sleep(0.1)
				if(self.go==True):
					break
				self.Label1_5.configure(text='''Opponent Turn''')
				self.disbut()
				tr=self.c.recv(1024)
				self.f[int(tr.decode('utf8'))](45)
				if(self.go==True):
					print('break')
					break
				self.enabut()
		if(self.t == 0):
			while True:
				self.Label1_5.configure(text='''Opponent Turn''')
				self.disbut()
				tr=self.c.recv(1024)
				self.f[int(tr.decode('utf8'))](45)
				if(self.go==True):
					print('break')
					break
				self.enabut()
				self.acpt=True
				self.Label1_5.configure(text='''Your Turn''')
				while True:
					if(self.acpt==False):
						break
				time.sleep(0.1)
				if(self.go==True):
					break



    def disbut(self):
            self.Button0.configure(state = "disabled")
            self.Button1.configure(state = "disabled")
            self.Button2.configure(state = "disabled")
            self.Button3.configure(state = "disabled")
            self.Button4.configure(state = "disabled")
            self.Button5.configure(state = "disabled")
            self.Button6.configure(state = "disabled")
            self.Button7.configure(state = "disabled")
            self.Button8.configure(state = "disabled")


    def enabut(self):
            self.Button0.configure(state = "normal")
            self.Button1.configure(state = "normal")
            self.Button2.configure(state = "normal")
            self.Button3.configure(state = "normal")
            self.Button4.configure(state = "normal")
            self.Button5.configure(state = "normal")
            self.Button6.configure(state = "normal")
            self.Button7.configure(state = "normal")
            self.Button8.configure(state = "normal")



	

    def reset(self,a):
    	self.s.close()
        self.game(a)

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


    def fire8(self,a=-1):
        if(self.l[8]==-99):
            if(self.temp%2!=0):
                self.Button8.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button8.configure(foreground="#02e202")
                self.Button8.configure(text='''O''')
                self.Button8.configure(disabledforeground="#02e202")
            else:
                self.Button8.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button8.configure(foreground="#ff0000")
                self.Button8.configure(text='''X''')
                self.Button8.configure(disabledforeground="#ff0000")
            self.temp=self.temp+1
            print(8)
            self.fire(8,a)
            
        
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
            if (b==-1):
            	self.acpt=False
                self.c.send(str(a).encode('utf8'))
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
            self.go=True
            self.Button0.configure(state = "disabled")
            self.Button1.configure(state = "disabled")
            self.Button2.configure(state = "disabled")
            self.Button3.configure(state = "disabled")
            self.Button4.configure(state = "disabled")
            self.Button5.configure(state = "disabled")
            self.Button6.configure(state = "disabled")
            self.Button7.configure(state = "disabled")
            self.Button8.configure(state = "disabled")
        qw=0
        for i in self.l:
        	if (i==-99):
        		qw=qw+1
        if (qw==0):
            self.go=True
            self.Button0.configure(state = "disabled")
            self.Button1.configure(state = "disabled")
            self.Button2.configure(state = "disabled")
            self.Button3.configure(state = "disabled")
            self.Button4.configure(state = "disabled")
            self.Button5.configure(state = "disabled")
            self.Button6.configure(state = "disabled")
            self.Button7.configure(state = "disabled")
            self.Button8.configure(state = "disabled")
            self.Label1_5.configure(text='''Match Draw''')


class client:
    def __init__(self, top=None):
		font9 = "-family {DejaVu Sans} -size 24 -weight normal -slant roman -underline 0 -overstrike 0"
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85'
		_ana2color = '#ececec' # Closest X11 color: 'gray92'
		font11 = "-family {Bitstream Charter} -size 20 -weight normal -slant italic -underline 0 -overstrike 0"
		font12 = "-family {DejaVu Sans} -size 24 -weight normal -slant roman -underline 0 -overstrike 0"
		self.top=top
		self.serli=[]

		top.geometry("651x668+355+26")
		top.title("New Toplevel")
		top.configure(background="#000000")
		top.configure(highlightcolor="black")

		self.Label1 = tk.Label(top)
		self.Label1.place(relx=0.122, rely=0.015, height=141, width=519)
		self.Label1.configure(activebackground="#f9f9f9")
		self.Label1.configure(background="#000000")
		self.Label1.configure(font="-family {Ani} -size 48 -weight bold -slant italic")
		self.Label1.configure(foreground="#9669ff")
		self.Label1.configure(text='''Tic Tac Toe''')


		self.Label1_5 = tk.Label(top)
		self.Label1_5.place(relx=0.03, rely=0.853, height=71, width=609)
		self.Label1_5.configure(activebackground="#f9f9f9")
		self.Label1_5.configure(background="#000000")
		self.Label1_5.configure(borderwidth="0")
		self.Label1_5.configure(font="-family {Ani} -size 48 ")
		self.Label1_5.configure(foreground="#9ad8e2")
		self.Label1_5.configure(highlightthickness="0")
		self.Label1_5.configure(text='''Searching For Players''')

		self.scrollbar = tk.Scrollbar(top)
		self.Listbox1 = tk.Listbox(top, yscrollcommand=self.scrollbar.set, width=50)
		self.Listbox1.place(relx=0.258, rely=0.284, relheight=0.443, relwidth=0.492)
		self.Listbox1.configure(background="#000000")
		self.Listbox1.configure(font=font11)
		self.Listbox1.configure(foreground="#58ff05")
		self.Listbox1.configure(highlightthickness="0")
		self.scrollbar.config(command=self.Listbox1.yview)
		self.Listbox1.bind('<<ListboxSelect>>', self.onselect)

		
		self.Button1 = tk.Button(top)
		self.Button1.place(relx=0.274, rely=0.778, height=31, width=301)
		self.Button1.configure(background="#ff0000")
		self.Button1.configure(borderwidth="0")
		self.Button1.configure(text='''Start Game''')
		self.Button1.configure(command=self.stga)


		self.Button2 = tk.Button(top)
		self.Button2.place(relx=0.0, rely=0.0, height=29, width=111)
		self.Button2.configure(activebackground="#f9f9f9")
		self.Button2.configure(background="#000000")
		self.Button2.configure(borderwidth="0")
		self.Button2.configure(font="-family {DejaVu Sans} -size 12 -slant italic")
		self.Button2.configure(foreground="#0aff5c")
		self.Button2.configure(highlightthickness="0")
		self.Button2.configure(text='''Back''')

		
		self.Message1 = tk.Message(top)
		self.Message1.place(relx=0.243, rely=0.165, relheight=0.082, relwidth=0.535)
		self.Message1.configure(background="#000000")
		self.Message1.configure(font=font12)
		self.Message1.configure(foreground="#eeff00")
		self.Message1.configure(text='''Select a Player  :''')
		self.Message1.configure(width=352)

		self.t=threading.Thread(target=self.recieve, args=())
		self.t.start()



    def onselect(self,evt):
		w = evt.widget
		index = int(w.curselection()[0])
		self.value = w.get(index)
		
    def stga(self):
    	if self.value:
			self.s.sendto('j',self.value)
			print 'yay went'


    def recieve(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.s.bind(('', 6759 ))
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
		self.s.sendto('s',('<broadcast>',6757))

		while True:
			tsoc, _, _=select.select([self.s],[],[],5)
			if tsoc:
				for i in tsoc:
					d, a = i.recvfrom(1024)
					print (d,a)
					if(d=='y'):
						self.Listbox1.insert(tk.END, a)
					if(d=='yes'):
						self.Label1.destroy()
						self.Label1_5.destroy()
						self.Listbox1.destroy()
						self.Button1.destroy()
						self.Button2.destroy()
						self.Message1.destroy()
						self.s.close()
						print('udp soc closed')
						self.game(a)
						return
	

    def game(self,addr):

		top=self.top


		font9 = "-family {DejaVu Sans} -size 24 -weight normal -slant roman -underline 0 -overstrike 0"
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85'
		_ana2color = '#ececec' # Closest X11 color: 'gray92'
		self.l=[]
		self.temp=0
		for i in range(0,9):
		    self.l.append(-99)
		self.top=top

		top.geometry("651x668+355+26")
		top.title("New Toplevel")
		top.configure(background="#000000")
		top.configure(highlightcolor="black")

		self.Label1 = tk.Label(top)
		self.Label1.place(relx=0.092, rely=0.06, height=141, width=519)
		self.Label1.configure(activebackground="#f9f9f9")
		self.Label1.configure(background="#000000")
		self.Label1.configure(font="-family {Ani} -size 48 -weight bold -slant italic")
		self.Label1.configure(foreground="#9669ff")
		self.Label1.configure(text='''Tic Tac Toe''')


		self.Label1_5 = tk.Label(top)
		self.Label1_5.place(relx=0.03, rely=0.808, height=61, width=609)
		self.Label1_5.configure(activebackground="#000000")
		self.Label1_5.configure(background="#000000")
		self.Label1_5.configure(borderwidth="0")
		self.Label1_5.configure(font="-family {Ani} -size 48 ")
		self.Label1_5.configure(foreground="#ff0000")
		self.Label1_5.configure(highlightthickness="0")
		self.Label1_5.configure(text='''Waiting for Player''')



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
		self.Button8.configure(disabledforeground="#ff0000")
		self.Button8.configure(command=self.fire8)
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
		self.Button2_1.configure(command=lambda:self.reset(addr))
		self.Button34 = tk.Button(top)
		self.Button34.place(relx=0.0, rely=0.0, height=29, width=111)
		self.Button34.configure(background="#000000")
		self.Button34.configure(borderwidth="0")
		self.Button34.configure(font="-family {DejaVu Sans} -size 12 -slant italic")
		self.Button34.configure(foreground="#0aff5c")
		self.Button34.configure(highlightthickness="0")
		self.Button34.configure(text='''Main Menu''')
		self.Button34.configure(command=top.destroy)
		self.f=[self.fire0,self.fire1,self.fire2,self.fire3,self.fire4,self.fire5,self.fire6,self.fire7,self.fire8]
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		t1 = threading.Thread(target=self.soc, args=(addr,))
		t1.setDaemon(True)
		t1.start()







    def soc(self,addr):
		self.s.connect(addr)
		self.t=self.s.recv(1024)
		self.go=False
		print(self.t)
		if(self.t=='ts'):
			self.t=0

		else:
			self.t=1

		if(self.t==1):
			self.Label1_5.configure(text='''Your Turn''')
		else:
			self.disbut()
			self.Label1_5.configure(text='''Opponent Turn''')
		
		if(self.t == 1):
			while True:
				self.acpt=True
				self.Label1_5.configure(text='''Your Turn''')
				while True:
					if(self.acpt==False):
						break
				time.sleep(0.1)
				if(self.go==True):
					break
				self.Label1_5.configure(text='''Opponent Turn''')
				self.disbut()
				tr=self.s.recv(1024)
				print (int(tr.decode('utf8')))
				self.f[int(tr.decode('utf8'))](45)
				if(self.go==True):
					print('break')
					break
				self.enabut()
		if(self.t == 0):
			while True:
				self.Label1_5.configure(text='''Opponent Turn''')
				self.disbut()
				tr=self.s.recv(1024)
				print (int(tr.decode('utf8')))
				self.f[int(tr.decode('utf8'))](45)
				if(self.go==True):
					print('break')
					break
				self.enabut()
				self.acpt=True
				self.Label1_5.configure(text='''Your Turn''')
				while True:
					if(self.acpt==False):
						break
				time.sleep(0.1)
				print('done')
				if(self.go==True):
					print('break')
					break
				print('passed')
					



    def disbut(self):
            self.Button0.configure(state = "disabled")
            self.Button1.configure(state = "disabled")
            self.Button2.configure(state = "disabled")
            self.Button3.configure(state = "disabled")
            self.Button4.configure(state = "disabled")
            self.Button5.configure(state = "disabled")
            self.Button6.configure(state = "disabled")
            self.Button7.configure(state = "disabled")
            self.Button8.configure(state = "disabled")


    def enabut(self):
            self.Button0.configure(state = "normal")
            self.Button1.configure(state = "normal")
            self.Button2.configure(state = "normal")
            self.Button3.configure(state = "normal")
            self.Button4.configure(state = "normal")
            self.Button5.configure(state = "normal")
            self.Button6.configure(state = "normal")
            self.Button7.configure(state = "normal")
            self.Button8.configure(state = "normal")
	

    def reset(self,a):
        self.game(a)

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


    def fire8(self,a=-1):
        if(self.l[8]==-99):
            if(self.temp%2!=0):
                self.Button8.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button8.configure(foreground="#02e202")
                self.Button8.configure(text='''O''')
                self.Button8.configure(disabledforeground="#02e202")
            else:
                self.Button8.configure(font="-family {DejaVu Sans} -size 48 -weight bold")
                self.Button8.configure(foreground="#ff0000")
                self.Button8.configure(text='''X''')
                self.Button8.configure(disabledforeground="#ff0000")
            self.temp=self.temp+1
            print(8)
            self.fire(8,a)
            
        
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
            if (b==-1):
            	self.acpt=False
                self.s.send(str(a).encode('utf8'))
        print self.l
        if(self.check()):
            self.go=True
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
        qw=0
        for i in self.l:
        	if(i==-99):
        		qw=qw+1
        if (qw==0):
            self.go=True
            self.Button0.configure(state = "disabled")
            self.Button1.configure(state = "disabled")
            self.Button2.configure(state = "disabled")
            self.Button3.configure(state = "disabled")
            self.Button4.configure(state = "disabled")
            self.Button5.configure(state = "disabled")
            self.Button6.configure(state = "disabled")
            self.Button7.configure(state = "disabled")
            self.Button8.configure(state = "disabled")
            self.Label1_5.configure(text='''Match Draw''')
            print('draw')
            print self.go

root=tk.Tk()
t=Toplevel1(root)

root.mainloop()