import cmdtools
from cmdtools.ext import command

runner = command.CommandDir("commands")
runner.run(
	cmdtools.Cmd("/ping")
)
