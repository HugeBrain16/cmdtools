import asyncio
import cmdtools
from cmdtools.ext import command

async def main():
	runner = command.CommandDir("commands", search_tree=True)
	await runner.run(
		cmdtools.Cmd("/greet")
	)

asyncio.run(main())
