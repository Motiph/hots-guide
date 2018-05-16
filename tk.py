import tkinter
from tkinter import ttk

class App(ttk.Frame):
	def __init__(self, parent, *args, **kwargs):
		ttk.Frame.__init__(self, parent, *args, **kwargs)
		self.root = parent
		self.init_gui()
	
	def init_gui(self):
		self.root.title('Guide')
		self.root.geometry('500x50')
		self.root.configure(background='white')
		#Lo mantiene siempre encima de todo
		self.root.attributes('-topmost', True)
		#self.root.attributes('-transparentcolor', 'white')
		self.root.resizable(width=False, height=False)
		self.myinput = ttk.Entry(self.root)
		self.myinput.pack()
		self.myinput.insert(0, "hola")

if __name__ == '__main__':
	root = tkinter.Tk()
	App(root)
	root.mainloop()
		
#root = tk.Tk()
#main = App(root)
#root.mainloop()
#root.mainloop()
	


#WIDTH = 500
#HEIGHT = 50

#window = Tk()

#window.overrideredirect(True) #no usar
#window.configure(background='white')
#window.wm_attributes("-topmost", True)
#window.wm_attributes("-transparentcolor", "white") #pone el bg transparente
#window.title("Welcome to LikeGeeks app")
 
#menu = Menu(window)
 
#new_item = Menu(menu)
 
#new_item.add_command(label='New')
#new_item.add_command(label='Buscar')


#menu.add_cascade(label='File', menu=new_item)

#window.geometry('{}x{}'.format(WIDTH, HEIGHT))
#window.resizable(width=False, height=False)

#window.config(menu=menu)
 
#window.mainloop()