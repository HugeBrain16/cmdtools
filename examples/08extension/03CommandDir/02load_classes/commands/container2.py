from cmdtools.ext import command

class Greet(command.Command):
	def __init__(self):
		super().__init__(name="greet")

	def greet(self):
		print("Hello!")
