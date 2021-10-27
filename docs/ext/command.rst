Command Extension
=================

An extension for command wrappers, containers and runners.

Examples
--------

some basic example of the command extension

Running a command struct
________________________

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
_______________

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

Loading commands from file
__________________________

You can load a single command or even multiple commands from a single file or module

Loading single command from file
++++++++++++++++++++++++++++++++

example of a single command file ``ping.py``

.. code:: py
    
    name = "ping" # name must be defined, to tell the loader which callback should be loaded
    __aliases__ = ["pang", ] # you can also set command aliases

    # overriding error callback
    # def ov_error_ping(error):
    #     print("Yes", error)
    #
    # "error_" + command name
    # error_ping = ov_error_ping

    def error_ping(error):
        print("Error!1122!!121, fix this...", error)

    def ping():
        print("Pong")

and script for loading and running the command

.. code:: py
    
    import asyncio
    import cmdtools
    from cmdtools.ext.command import CommandModule
    
    # set load_classes to false for loading a single command file
    command = CommandModule("ping.py", load_classes=False)
    
    # check if command is loaded or not by checking ``commands`` list property
    if command.commands:
        print("Command loaded!")
    
    async def main():
        cmd = cmdtools.Cmd("!ping", prefix='!')
        
        if cmd.name:
            await command.run(cmd)

    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())

Loading multiple commands from a single file
++++++++++++++++++++++++++++++++++++++++++++

create a command file named ``cool.py`` for example

.. code:: py
    
    from cmdtools.ext.command import Command
    
    # the loader will only load a class that inherits Command class
    class Test1(Command):
        def __init__(self):
            super().__init__(name="test1")
            
        def test1(self):
            print("Test1 OK!")

    class Test2(Command):
        def __init__(self):
            super().__init__(name="test2")
            
        def test2(self):
            print("Test2 OK!")

and loader or runner script

.. code:: py
    
    import asyncio
    import cmdtools
    from cmdtools.ext.command import CommandModule
    
    # set load_classes to true to load multiple commands
    # or just don't set it because the default is True
    command = CommandModule("cool.py")
    
    if command.commands:
        print("Commands loaded!")
    
    async def main():
        cmd1 = cmdtools.Cmd("!test1", prefix='!')
        cmd2 = cmdtools.Cmd("!test2", prefix='!')
        
        await command.run(cmd1)
        await command.run(cmd2)

    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
