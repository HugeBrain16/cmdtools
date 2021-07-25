import cmdtools
from cmdtools.ext import command

runner = command.CommandModule("ping.py", load_classes=False) # set load_classes to False to load command module
runner.run(
	cmdtools.Cmd("/ping")
)