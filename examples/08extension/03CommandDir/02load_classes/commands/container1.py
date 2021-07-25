from cmdtools.ext import command

class Ping(command.Command):
	def __init__(self):
		super().__init__(name="ping")

	def ping(self):
		print("Pong!")

class Say(command.Command):
	def __init__(self):
		super().__init__(name="say")

	def say(self, text):
		print(text)

	def error_say(self, error):
		print(error)
