import cmdtools
from cmdtools.ext import command

runner = command.CommandDir("commands", search_tree=True)
runner.run(
	cmdtools.Cmd("/greet")
)
