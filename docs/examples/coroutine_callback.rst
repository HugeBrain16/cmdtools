Coroutine Callback
==================

You can use coroutine callback as a command handler

.. code:: py
    
    import asyncio
    import cmdtools

    async def mine():
        print("Mining...")
        await asyncio.sleep(3)
        print("You mined 3 shungites!")
        
    async def main():
        # create asyncio command instance
        cmd = cmdtools.AioCmd("!mine", prefix='!')
        
        if cmd.name:
            await cmd.process_cmd(mine)

    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
