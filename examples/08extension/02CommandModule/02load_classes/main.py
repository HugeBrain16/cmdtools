import cmdtools
from cmdtools.ext import command

runner = command.CommandModule("commands.py")
runner.run(
	cmdtools.Cmd("/ping")
)
