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

    cmd = cmdtools.Cmd("!mine", prefix='!')

    if cmd.name:
        cmd.process_cmd(mine)
