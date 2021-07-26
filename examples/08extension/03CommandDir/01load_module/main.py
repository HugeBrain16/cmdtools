import asyncio
import cmdtools
from cmdtools.ext import command

async def main():
	runner = command.CommandDir("commands")
	await runner.run(
		cmdtools.Cmd("/ping")
	)

asyncio.run(main())
