import cmdtools
import inspect
import asyncio

# error handler callback needs to be a coroutine as well as the command callback
async def eping(error):
	print(error)

async def ping():
	print("Pinging...")
	await asyncio.sleep(1)
	print("Pong!")

cmd = cmdtools.Cmd("/ping")

if cmd.name == "ping":
	# check if callback is a coroutine function
	if inspect.iscoroutinefunction(ping):
		asyncio.run(cmd.aio_process_cmd(ping))
