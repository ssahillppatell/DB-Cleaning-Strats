from tkinter import Tk, Label, Canvas, Entry, Button, ttk, Frame, DISABLED
from utils.checkoutOne import checkoutOne
from utils.checkoutRegularly import checkoutRegularly
from utils.MyNotebook import MyNotebook
from utils.MyTab import MyTab

root = Tk()
root.geometry("400x300")

myNotebook = MyNotebook(root)
tabOne = MyTab(myNotebook.getMyNotebook())
tabRegularly = MyTab(myNotebook.getMyNotebook())

frameOne = tabOne.getFrame()
frameRegularly = tabRegularly.getFrame()

myNotebook.addTab(frameOne, "Checkout One")
myNotebook.addTab(frameRegularly, "Checkout Regularly")

tabOne.getBtn().config(command = lambda:tabOne.setResult(checkoutOne(tabOne.getId().get())))
tabRegularly.getBtn().config(command = lambda:tabRegularly.setResult(checkoutRegularly(tabRegularly.getId().get())))

root.mainloop()