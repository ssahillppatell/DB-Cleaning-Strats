from tkinter import Tk, Label, Canvas, Entry, Button, ttk, Frame, DISABLED

from functions.checkoutOne import checkoutOne

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

actionBtn = Button(frameOne, text="Checkout", command = lambda:checkoutOne(rentalId.get()), bg = "#2eac2b", fg = "white")
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

customerOutput = Label(frameOne, text = "-")
customerOutput.grid(column = 3, row = 3)

filmOutput = Label(frameOne, text = "-")
filmOutput.grid(column = 3, row = 4)

rentalDateOutput = Label(frameOne, text = "-")
rentalDateOutput.grid(column = 3, row = 5)

rentalPeriodOutput = Label(frameOne, text = "-")
rentalPeriodOutput.grid(column = 3, row = 6)

isLateOutput = Label(frameOne, text = "-")
isLateOutput.grid(column = 3, row = 7)

costOutput = Label(frameOne, text = "-")
costOutput.grid(column = 3, row = 8)

printBillButton = Button(frameOne, text = "Print Bill", bg = "#5877C9", fg = "white", width = 50)
printBillButton.grid(columnspan = 8, column = 0, row = 9)

# Widgets of FrameDaily
canvas = Canvas(frameDaily, width = 400, height = 300)
canvas.grid(columnspan = 5, rowspan = 5)

rentalId = Entry(frameDaily)
rentalId.grid(column = 1, row = 0)

actionBtn = Button(frameDaily, text="Transact", command = lambda:checkoutOne(rentalId.get()))
actionBtn.grid(column = 1, row = 1)

root.mainloop()