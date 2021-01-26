from tkinter import Tk, Label, Canvas, Entry, Button, ttk, Frame, DISABLED
from utils.checkoutOne import checkoutOne
from utils.MyNotebook import MyNotebook
from utils.MyTab import MyTab

root = Tk()
root.geometry("400x300")

myNotebook = MyNotebook(root)
tabOne = MyTab(myNotebook.getMyNotebook())
tabDaily = MyTab(myNotebook.getMyNotebook())

frameOne = tabOne.getFrame()
frameDaily = tabDaily.getFrame()

myNotebook.addTab(frameOne, "Checkout One")
myNotebook.addTab(frameDaily, "Checkout Daily")

tabOne.getBtn().config(command = lambda:tabOne.setResult(checkoutOne(tabOne.getId().get())))

root.mainloop()