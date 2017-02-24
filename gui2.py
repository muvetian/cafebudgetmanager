from Tkinter import *
import ttk
import time
import main
import tkFont

class Application(Frame):
	
	
	def __init__(self,master):
		self.first_write = True
		"""Initialize the frame"""
		self.root = master
		Frame.__init__(self,master)

		
		self.grid()
		
		self.menubar = Menu(self.root)
		self.menubar.add_command(label="Hello!", command=self.hello)
		self.root.config(menu=self.menubar)
		filemenu = Menu(self.menubar, tearoff=0)
		filemenu.add_command(label="Open", command=self.hello)
		filemenu.add_command(label="Save", command=self.hello)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.root.quit)
		self.menubar.add_cascade(label="File", menu=filemenu)

		editmenu = Menu(self.menubar, tearoff=0)
		editmenu.add_command(label="Cut", command=self.hello)
		editmenu.add_command(label="Copy", command=self.hello)
		editmenu.add_command(label="Paste", command=self.hello)
		self.menubar.add_cascade(label="Edit", menu=editmenu)

		helpmenu = Menu(self.menubar, tearoff=0)
		helpmenu.add_command(label="About", command=self.hello)
		self.menubar.add_cascade(label="Help", menu=helpmenu)





		self.create_widgets()
		


	def hello():
		print "hello"
	def create_frame_time(self):
		self.frame_time = ttk.LabelFrame(self.root,height = 100, width = 100, text = "System Time")
		self.frame_time.grid(row = 0, column = 0, sticky=W)
		return self.frame_time	
	def create_frame_availability(self):
		self.frame_availability = ttk.LabelFrame(self.root,height = 100, width = 100, text = "                          Meal Plan Availability")
		self.frame_availability.grid(row = 1, column = 0, sticky=W)
		return self.frame_availability
	
	
	def create_frame_options(self):
		self.frame_options = ttk.LabelFrame(self.root,height = 1200, width = 1600	, text = "Options")
		self.frame_options.grid(row = 2, column = 0, sticky=W)
		return self.frame_options

	def create_frame_selection(self):

		self.frame_selection = Frame(self.root,height = 100, width = 100)
		self.frame_selection.grid(row = 3, column = 0, sticky=W)
		return self.frame_selection

	def create_widgets(self):
		
		self.frame_time = self.create_frame_time()
		self.frame_availability = self.create_frame_availability()
		self.frame_options = self.create_frame_options()
		

		self.current_time= Label(self.frame_time, text = "", font = 'Courier')
		self.current_time.pack()
		current_time = self.update_clock()
		str_time = time.localtime()
		
		self.frame_selection = self.create_frame_selection()
		selection_label = Label(self.frame_selection, text = "Your current selection: ")
		selection_label.grid(row=0,column=0,sticky=W)
		T = Text(self.frame_selection, height=2, width=30)
		T.grid(row = 1, column = 0, sticky= W)
		T.config(state=DISABLED)
		
		

		# category = StringVar()

		# combobox = ttk.Combobox(self, textvariable = category)
		# combobox.grid(row = 0, column = 2, sticky=E)
		# combobox.config(values = ('Grill', 'Deli', 'Oven','Breakfast'))
		# print(category.get())



		
		self.meal_plan = Label(self.frame_availability, text = "", font = 'Courier')
		self.meal_plan.pack()
		self.update_mealplan(str_time)


		self.Courier13 = tkFont.Font(family='Courier', size=13)
		self.Courier10 = tkFont.Font(family='Courier', size=10)
		self.Courier8 = tkFont.Font(family='Courier', size=8)
		#family='Helvetica', size=18, weight='bold'
		# Creates all the items buttons
			
		self.create_menu_buttons(T,20)
		print (self.first_write)
		

		#Text box that shows what the user's current selection is 
		


		# self.button1 = Checkbutton(self.frame_options, text = "Wildcat Burger",font = Courier13)
		# self.button1.grid(row = 2, column = 0, sticky = W)

		# self.button2 = Checkbutton(self.frame_options, text = "Cajun Burger",font = Courier13)
		# self.button2.grid(row = 2, column = 3, sticky = E)


		# self.wildcat_burger = PhotoImage(file = main.get_path('1')).subsample(5,5)
		# self.cajun_burger = PhotoImage(file = main.get_path('2')).subsample(5,5)
	

		# self.button1.config(image=self.wildcat_burger, compound = TOP)
		# self.button2.config(image=self.cajun_burger, compound = TOP)
		

		

		#self.password = Entry(self)	
		#self.password.grid(row = 1, column = 1, sticky = W)
		
		
		# self.submit_button = Button(self, text = "submit", command = self.reveal)
		# self.submit_button.grid(row = 2, column = 0, sticky = W)



	# self.favorite = StringVar()
	# self.radiobutton = Radiobutton(self, text = "comedy", variable  = self.favorite)
	# self.checkbutton.grid(row = 2, column = 2, sticky = W)
	
	def update_selection(self,textbox,selection):
		
		print("I did it")
		textbox.config(state=NORMAL)
		textbox.insert(END, selection+"\n")
		textbox.config(state=DISABLED)

	def update_mealplan(self, struct_time):
		hour = struct_time.tm_hour
		message = ""
		if  10 <= hour <= 11 :
			message = "              You just missed the meal plan.                     "
		if  12<=hour<20:
			message = "              Meal plan is available!                            "
		if hour == 20:
			message = "              Meal plan will be up in an hour!                   "
		if 21<=hour<23:
			message = "              Hurry up! Meal Plan ends at 11:00                  "
		# if hour == 12:
		# 	message = "Meal plan is available!"
		if 23 <= hour < 24 or 0 <= hour < 7:
			message = "              For your health, please don't stay up!             "

		self.meal_plan.configure(text = message)
	# def reveal(self):
	# 	content = self.password.get()
	# 	if content == "Password":
	# 		message = "Success"
	# 	else:
	# 		message = "Wrong"

	# 	self.text.insert(0.0,message) #0.0 is the position, row 0 col 0
	def update_clock(self):
	    now = time.strftime("%H:%M:%S        %m/%d/%Y")
	    self.current_time.configure(text=now)
	    self.root.after(1000, self.update_clock)
	    return now
	def create_menu_buttons(self,textbox,num):

		last_column = num % 5;
		num_row = num / 5; 
		self.buttons = []
		self.gifs = []
		index = 0
		item_names = []
		for i in range(num_row):
			for j in range(5):
				item_name = main.get_item_name(index)
				item_names.append(item_name)
				self.gifs.append(PhotoImage(file = main.get_path(str(index+1))).subsample(5,5))
				if len(item_name) > 20:
					new_button = Button(self.frame_options, text= item_name, font = self.Courier10,command = lambda name = item_name: self.update_selection(name))

				if 20 >= len(item_name) > 12:
					self.buttons.append(Button(self.frame_options, text= item_name, font = self.Courier13))
				if len(item_name)<= 12:
					self.buttons.append(Button(self.frame_options, text= item_name, font = self.Courier13))
				
				self.buttons[index].config(height = 100, width = 100,image=self.gifs[index], compound = TOP)
				self.buttons[index].grid(row = i, column = j,sticky = W)

				index = index + 1
		for k in range(last_column):
			
			item_name = main.get_item_name(index)
			self.gifs.append(PhotoImage(file = main.get_path(str(index+1))).subsample(5,5))
			if len(item_name) > 20:
				self.buttons.append(Button(self.frame_options, text= item_name, font = self.Courier10, command = self.update_selection(textbox,item_name) ))
			if 20 >= len(item_name) > 12:
				self.buttons.append(Button(self.frame_options, text= item_name, font = self.Courier13,command = self.update_selection(textbox,item_name) ))
			if len(item_name)<= 12:
				self.buttons.append(Button(self.frame_options, text= item_name, font = self.Courier13,command = self.update_selection(textbox,item_name) ))		
				self.buttons[index].config(image=self.gifs[index], compound = TOP)
				self.buttons[index].grid(row = num_row + 1, column = k,sticky = W)
				index = index + 1

		
		for name in item_names:

			button.config(command = lambda name = name: self.update_selection(textbox,self.update_selection(textbox,item_name)))
		
		return self.buttons
def gify(item):
	return item.text

def windows():
	root = Tk()
	root.title("Union Cafe Budget Manager")
	root.geometry("960x1200")
	app = Application(root) #allows it to hold other widgets
	root.mainloop()
if __name__ == '__main__':
	windows()
