import asyncio
import cmdtools
from cmdtools.ext import command

async def main():
	runner = command.CommandModule("ping.py", load_classes=False) # set load_classes to False to load command module
	await runner.run(
		cmdtools.Cmd("/ping")
	)

asyncio.run(main())
