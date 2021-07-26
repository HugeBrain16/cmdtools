import asyncio
import cmdtools
from cmdtools.ext import command

class Ping(command.Command):
	_help = "Ping local machine"
	def __init__(self):
		self.name = "ping"
		super().__init__(name=self.name)

	# command callback name must be the same as the command name
	def ping(self):
		print("pong")

async def main():
	runner = command.CommandRunner(Ping()) # class must be initialized

	try:
		await runner.run(
			cmdtools.Cmd("/ping")
		)
	except command.RunnerError as e:
		print(e)

asyncio.run(main())
