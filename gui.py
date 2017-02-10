from Tkinter import *
import ttk
import time
class Application(Frame):
	def __init__(self,master):
		"""Initialize the frame"""
		self.root = master
		Frame.__init__(self,master)
		self.grid()
		self.button_clicks = 0 # count the number of button clicks
		self.create_widgets()

	def create_widgets(self):
		self.frame_time = ttk.LabelFrame(self.root,height = 100, width = 300, text = "System Time")
		self.frame_time.grid(row = 0, column = 0, sticky=W)
		self.frame_availability = ttk.LabelFrame(self.root,height = 100, width = 800, text = "Meal Plan Availability")
		self.frame_availability.grid(row = 0, column = 15, sticky=E)
		
		self.current_time= Label(self.frame_time, text = "", font = 'Courier')
		self.current_time.pack()
		current_time = self.update_clock()
		str_time = time.localtime()
		

		
		self.meal_plan = Label(self.frame_availability, text = "", font = 'Courier')
		self.meal_plan.pack()
		self.update_mealplan(str_time)


		self.frame_options = ttk.LabelFrame(self.root,height = 200, width = 480, text = "Options")
		self.frame_options.grid(row = 3, column = 0, sticky=W)

		self.button1 = Checkbutton(self.frame_options, text = "Wildcat Burger",font = 'Courier')
		self.button1.grid(row = 2, column = 0, sticky = W)


		self.wildcat_burger = PhotoImage(file = '/Users/kyle/Documents/GotBored/UnionBudgetManager/venv/img/burger01.gif').subsample(5,5)

		self.button1.config(image=self.wildcat_burger, compound = TOP)
		

		#self.password = Entry(self)	
		#self.password.grid(row = 1, column = 1, sticky = W)
		
		
		# self.submit_button = Button(self, text = "submit", command = self.reveal)
		# self.submit_button.grid(row = 2, column = 0, sticky = W)

		#self.text = Text(self, width = 35, height = 5, wrap = WORD)
		#self.text.grid(row = 3, column = 0, columnspan = 2, sticky = W)


	# self.favorite = StringVar()
	# self.radiobutton = Radiobutton(self, text = "comedy", variable  = self.favorite)
	# self.checkbutton.grid(row = 2, column = 2, sticky = W)
	def update_mealplan(self, struct_time):
		hour = struct_time.tm_hour
		message = ""
		if  10 <= hour <= 11 :
			message = "You just missed meal plan. Get up early next time, you lazy head."
		if  11<= hour <20 or 7<= hour <= 9:
			message = "Meal plan is available!"
		if hour == 20:
			message = "Meal plan will be up in an hour!"
		if 21<=hour<23:
			message = "Hurry up, you got 2 hours!"
		else:
			message = "For your health, please don't stay up !"
		self.meal_plan.configure(text = message)
	# def reveal(self):
	# 	content = self.password.get()
	# 	if content == "Password":
	# 		message = "Success"
	# 	else:
	# 		message = "Wrong"

	# 	self.text.insert(0.0,message) #0.0 is the position, row 0 col 0
	def update_clock(self):
	    now = time.strftime("%H:%M:%S  %m/%d/%Y")
	    self.current_time.configure(text=now)
	    self.root.after(1000, self.update_clock)
	    return now
def windows():
	root = Tk()
	root.title("Union Cafe Budget Manager")
	root.geometry("480x600")
	app = Application(root) #allows it hold other widgets
	root.mainloop()
if __name__ == '__main__':
	windows()
