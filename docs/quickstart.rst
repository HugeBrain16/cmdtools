Quickstart
==========

| A quick tutorial to get started
| check out `install <./install.html>`__ if you haven't already installed cmdtools

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

You can specify arguments in the command and access them in the specified callback

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
        asyncio.run(cmdtools.execute(cmd, login))

You can execute a command without defining an async callback with `Executor`

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

You can assign an error callback to a callback to handle a specific exception.

.. code:: py

    import asyncio
    import cmdtools

    @cmdtools.callback.add_option("user")
    @cmdtools.callback.add_option("password")
    def login(ctx):
        print("Login success!")

    @login.error
    def error_login(ctx):
        # handle missing required argument
        if isinstance(ctx.error, cmdtools.NotEnoughArgumentError):
            if ctx.error.option == "user":
                print("user is required!")
            elif ctx.error.option == "password":
                print("password is required!")
        else:
            # raise exception for unhandled error
            raise error

    cmd = cmdtools.Cmd("!login admin", prefix='!')

    if cmd.name == "login":
        asyncio.run(cmdtools.execute(cmd, login))

Parameter arguments
------------------------

As of version 3.1.0, cmdtools supports parameter arguments.

.. code:: py

    import asyncio
    import cmdtools

    @cmdtools.callback.add_option("object_id")
    @cmdtools.callback.add_option("x")
    @cmdtools.callback.add_option("y")
    @cmdtools.callback.add_option("z")
    def spawn(ctx):
        print(f"Spawned {ctx.options.object_id} at ({ctx.options.x}, {ctx.options.y}, {ctx.options.z})")

    cmd = cmdtools.Cmd("/spawn 1001 x=1.0 z=4.0")

    if cmd.name == "spawn":
        asyncio.run(cmdtools.execute(cmd, spawn))
