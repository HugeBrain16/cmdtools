import asyncio
import cmdtools
from cmdtools.ext import command

async def main():
	runner = command.CommandModule("commands.py")
	await runner.run(
		cmdtools.Cmd("/ping")
	)

asyncio.run(main())
