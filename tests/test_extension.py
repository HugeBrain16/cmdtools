from .. import cmdtools
from ..cmdtools.ext import command

class Add(command.Command):
	def __init__(self):
		self.result = None
		self.name = "add"
		super().__init__(name=self.name)

	def add(self, n1, n2):
		self.result = n1 + n2

def test_class_cmd():
	runner = command.CommandRunner(Add())
	runner.run(
		cmdtools.Cmd("/add 40 40", convert_args=True)
	)

	assert runner.command.result == 80
	assert runner.command.name == "add"
