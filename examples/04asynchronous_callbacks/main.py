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

# use asyncio instance Cmd for processing coroutine callbacks
cmd = cmdtools.AioCmd("/ping")

if cmd.name == "ping":
    asyncio.run(cmd.process_cmd(ping))
