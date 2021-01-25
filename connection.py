from tkinter import Tk, Label, Canvas, Entry, Button, ttk, Frame, DISABLED

from functions.checkoutOne import checkoutOne

transactionData = {}

def printOutput(data):
	customerOutput.config(text = data['full_name'])
	filmOutput.config(text = data['film_title'])
	rentalDateOutput.config(text = data['rental_date'].date())
	rentalPeriodOutput.config(text = f"{data['rental_duration']} days")
	costOutput.config(text = f"$ {data['rental_rate']}")

	if(int(data['rental_date'].strftime("%d")) + int(data['rental_duration']) < 32):
		isLateOutput.config(text = "Yes")
	else:
		isLateOutput.config(text = "No")

def takeInput(id):
	transactionData = checkoutOne(id)
	print(transactionData)
	printOutput(transactionData)

root = Tk()

# Defining Notebook and Frames
myNotebook = ttk.Notebook(root)
frameOne = Frame(myNotebook,  width = 400, height = 300)
frameDaily = Frame(myNotebook,  width = 400, height = 300)

myNotebook.add(frameOne, text = "Checkout One")
myNotebook.add(frameDaily, text = "Checkout Daily")

myNotebook.grid(column = 0, row = 0)

# Widgets of FrameOne
canvas = Canvas(frameOne, width = 400, height = 300)
canvas.grid(columnspan = 8, rowspan = 10)

rentalIdLabel = Label(frameOne, text = "Enter the Rental Id:")
rentalIdLabel.grid(columnspan = 3, column = 0, row = 0)

rentalId = Entry(frameOne, width = 30)
rentalId.grid(columnspan = 3, column = 4, row = 0)

actionBtn = Button(frameOne, text="Checkout", command = lambda:takeInput(rentalId.get()), bg = "#2eac2b", fg = "white")
actionBtn.grid(column = 4, row = 1)

################

detailsLabel = Label(frameOne, text = "Details:")
detailsLabel.grid(column = 0, row = 2)

customerLabel = Label(frameOne, text = "Customer:")
customerLabel.grid(column = 0, row = 3)

filmLabel = Label(frameOne, text = "Film:")
filmLabel.grid(column = 0, row = 4)

rentalDateLabel = Label(frameOne, text = "Rental Date:")
rentalDateLabel.grid(column = 0, row = 5)

rentalPeriodLabel = Label(frameOne, text = "Rental Period:")
rentalPeriodLabel.grid(column = 0, row = 6)

isLateLabel = Label(frameOne, text = "is Late:")
isLateLabel.grid(column = 0, row = 7)

costLabel = Label(frameOne, text = "Cost:")
costLabel.grid(column = 0, row = 8)

#############

global customerOutput
customerOutput = Label(frameOne, text = "-")
customerOutput.grid(columnspan = 2, column = 3, row = 3)

global filmOutput
filmOutput = Label(frameOne, text = "-")
filmOutput.grid(columnspan = 2, column = 3, row = 4)

global rentalDateOutput
rentalDateOutput = Label(frameOne, text = "-")
rentalDateOutput.grid(columnspan = 2, column = 3, row = 5)

global rentalPeriodOutput
rentalPeriodOutput = Label(frameOne, text = "-")
rentalPeriodOutput.grid(columnspan = 2, column = 3, row = 6)

global isLateOutput
isLateOutput = Label(frameOne, text = "-")
isLateOutput.grid(columnspan = 2, column = 3, row = 7)

global costOutput
costOutput = Label(frameOne, text = "-")
costOutput.grid(columnspan = 2, column = 3, row = 8)

printBillButton = Button(frameOne, text = "Print Bill", bg = "#5877C9", fg = "white", width = 50)
printBillButton.grid(columnspan = 8, column = 0, row = 9)

# Widgets of FrameDaily
canvas2 = Canvas(frameDaily, width = 400, height = 300)
canvas2.grid(columnspan = 5, rowspan = 5)

rentalId2 = Entry(frameDaily)
rentalId2.grid(column = 1, row = 0)

actionBtn2 = Button(frameDaily, text="Transact", command = lambda:checkoutOne(rentalId.get()))
actionBtn2.grid(column = 1, row = 1)

root.mainloop()