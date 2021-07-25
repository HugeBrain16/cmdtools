import cmdtools
from cmdtools.ext import command

runner = command.CommandDir("commands", load_classes=True)
runner.run(
	cmdtools.Cmd("/greet")
)