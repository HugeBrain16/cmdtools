Quickstart
==========

| A quick tutorial to get started
| check out `install <./install.html>`__ if you haven't already installed cmdtools library

Basic command
-------------

A basic ping pong command

.. code:: py

    import cmdtools

    cmd = cmdtools.Cmd("!ping", prefix='!')

    if cmd.name == "ping":
        print("Pong!")

Callbacks and Arguments
-----------------------

you can pass arguments to the command and handle it in specified
callback

.. code:: py

    import asyncio
    import cmdtools

    @cmdtools.callback.add_option("name")
    @cmdtools.callback.add_option("password")
    def login(ctx):
        if ctx.options.name == "admin" and ctx.options.password == "admin":
            print("Login success!")
        else:
            print("Invalid login!")
            
    cmd = cmdtools.Cmd("!login admin admin", prefix='!')

    if cmd.name == "login":
        asyncio.run(cmdtools.exec(cmd, login))

you can execute a command without using an event loop by
creating your own executor

.. code:: py
    
    import cmdtools

    @cmdtools.callback.add_option("name")
    @cmdtools.callback.add_option("password")
    def login(ctx):
        if ctx.options.name == "admin" and ctx.options.password == "admin":
            print("Login success!")
        else:
            print("Invalid login!")
            
    cmd = cmdtools.Cmd("!login admin admin", prefix='!')

    if cmd.name == "login":
        executor = cmdtools.Executor(cmd, login)
        executor.exec()

Error handling
--------------

if error occurred during command execution, you can specify an error
callback to handle the error or the exception

.. code:: py

    import asyncio
    import cmdtools

    @cmdtools.callback.add_option("user")
    @cmdtools.callback.add_option("password")
    def login(ctx):
        print("Login success!")

    @login.error
    def error_login(ctx):
        # check exception instance, in this case it's missing required argument
        if isinstance(ctx.error, cmdtools.NotEnoughArgumentError):
            if ctx.error.option == "user":
                print("user is required!")
            elif ctx.error.option == "password":
                print("password is required!")
        else:
            # if other error occured, raise the exception
            # otherwise it would be suppressed by the processor
            raise error

    cmd = cmdtools.Cmd("!login admin", prefix='!')

    if cmd.name == "login":
        asyncio.run(cmdtools.exec(cmd, login))
