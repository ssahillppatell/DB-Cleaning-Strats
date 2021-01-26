from tkinter import ttk

class MyNotebook:
	def __init__(self, root):
		self.root = root
		self.width = 400
		self.height = 300
		self.notebook = ttk.Notebook(self.root, width = self.width, height = self.height)
		self.notebook.grid(column = 0, row = 0)
	
	def getMyNotebook(self):
		return self.notebook

	def addTab(self, tab, name):
		self.notebook.add(tab, text = name)