# Write a version of the Guess My Number Game frm chapter3 project using GUI

from Tkinter import *
import random

class Application(Frame):
	def __init__(self,master):
		# Initilaize the Frame and also this Application
		Frame.__init__(self,master)
		self.grid()
		self.number=random.randint(1,20)
		self.no_tries=0 
		self.create_widgets()
		
		
	def create_widgets(self):
		# Create a Label widget"
		print self.number
		Label(self,text="I'm thinking of a number between 1 and 20.").grid(row=0, column=0, columnspan=2, sticky=W)
		Label(self, text="Try to guess it in as few attempts as possible.").grid(row=1, column=0, columnspan=2, sticky=W)
		Label(self, text="Take a guess.").grid(row=2, column=0, sticky=W)
		self.g1=Entry(self)
		self.g1.grid(row=2, column=1, sticky=W)
		self.no_tries=self.no_tries+1
		Button(self, text="Check",command=self.check_number).grid(row=3, column=0, sticky=W)
		self.t=Text(self,width=40, height=10, wrap=WORD)
		self.t.grid(row=4,column=0, sticky=W)
		
		
	def check_number(self):
		ans=""
		print self.number
		guess=self.g1.get()
		print guess
		if self.number==guess:
			ans+="Yes, You guessed it and it only took you "+self.no_tries+" tries"
		elif self.number<guess:
			ans+="Lower..."
		elif self.number>guess:
			ans+="Higher..."
			
			
		self.t.delete(0.0,END)
		self.t.insert(0.0,ans)
			
			


# mainloop

root=Tk()
root.title("Guess My Number")
root.geometry("300x200")
app=Application(root)
root.mainloop()