from tkinter import Frame, Label, Entry, Button
from utils.printBill import printBill

class MyTab:
	def __init__(self, mount):
		self.data = {}
		self.frame = Frame(mount)

		Label(self.frame, text = 'Enter Rental Id:').grid(column = 0, row = 0, sticky = "we")
		
		self.rentalId = Entry(self.frame)
		self.rentalId.grid(columnspan = 2, column = 1, row = 0)

		self.btn = Button(self.frame, text = "Checkout", bg = "#2eac2b", fg = "white")
		self.btn.grid(column = 2, row = 1, sticky = "we")

		self.details = ['Customer:', 'Film:', 'Rental Date:', 'Rental Duration:', 'is Late?:', 'Cost:']

		Label(self.frame, text = "Details:").grid(column = 0, row = 2)

		for index, i in enumerate(self.details, start = 3):
			Label(self.frame, text = i).grid(column = 0, row = index)
			Label(self.frame, text = "-").grid(column = 1, row = index)
		
		self.printBtn = Button(self.frame, text = "Print the Bill", command = lambda:printBill(self.data), bg = "#5877C9", fg = "white")
		self.printBtn.grid(columnspan = 3, column = 0, row = 9, sticky = "we")
	
	def getFrame(self):
		return self.frame
	
	def getBtn(self):
		return self.btn
	
	def getId(self):
		return self.rentalId
	
	def setResult(self, data):
		self.data = data
		Label(self.frame, text = f"{data['full_name']}").grid(column = 1, row = 3)
		Label(self.frame, text = f"{data['film_title']}").grid(column = 1, row = 4)
		Label(self.frame, text = f"{data['rental_date']}").grid(column = 1, row = 5)
		Label(self.frame, text = f"{data['rental_duration']} days").grid(column = 1, row = 6)
		isLate = "No"
		if(int(data['rental_date'].strftime("%d")) + int(data['rental_duration']) < 32):
			isLate = "Yes"
		Label(self.frame, text = f"{isLate}").grid(column = 1, row = 7)
		Label(self.frame, text = f"$ {data['rental_rate']}").grid(column = 1, row = 8)
