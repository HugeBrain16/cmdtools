from cmdtools.ext import command

class Ping(command.Command):
	_help = "Ping local machine"
	def __init__(self):
		self.name = "ping"
		super().__init__(name=self.name)

	# command callback must be the same as the command name
	def ping(self):
		print("pong")
