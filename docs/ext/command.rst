Command Extension
=================

An extension for command wrappers, containers and runners.

Examples
--------

some basic example of the command extension

Running a command struct
------------------------

.. code:: py

    import asyncio
    import cmdtools
    from cmdtools.ext.command import Command, CommandRunner

    # define command struct
    class Ping(Command):
        def __init__(self):
            super().__init__(name="ping")
        
        # callback handler is automatically assigned
        # the container will try to get a method according to the command name
        def ping(self):
            print("Pong!")
            
        # you can manually re-assign the callback by overriding callback property
        # @property
        # def callback(self):
        #     return self.re_ping

        # def re_ping(self):
        #     print("Pong!")

    # pass the command struct instance to a container
    # command struct must be initialized
    runner = CommandRunner(Ping())
    
    # command container's runner will return a coroutine object
    # run inside a coroutine function
    async def main():
        cmd = cmdtools.Cmd("!ping", prefix='!')
        
        if cmd.name:
            await runner.run(cmd)

    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())

Command wrapper
---------------

some kind of command container or wrapper

.. code:: py
    
    import asyncio
    import cmdtools
    from cmdtools.ext.command import Command, CommandWrapper
    
    wrapper = CommandWrapper()
    
    # assign command object to the container (or wrapper...)
    @wrapper.command(name="ping")
    def ping():
        print("pong!")

    # you can also assign a command struct
    @wrapper.command()
    class Say(Command):
        def __init__(self):
            super().__init__(name="say")

        def say(self, text):
            print("U sez,", text)
            
    async def main():
        cmd = cmdtools.Cmd("!say 'hello world!'", prefix='!')
        
        if cmd.name:
            await wrapper.run(cmd)

    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
