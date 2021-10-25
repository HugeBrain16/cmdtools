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

    import cmdtools

    # define callback for command handler
    def login(name, password):
        if name == "admin" and password == "admin":
            print("Login success!")
        else:
            print("Invalid login!")
            
    cmd = cmdtools.Cmd("!login admin admin", prefix='!')

    if cmd.name == "login":
        # pass `login` callback to processor
        cmd.process_cmd(login)

Error handling
--------------

if error occurred during command processing, you can specify an error
callback to handle error or exception

.. code:: py

    import cmdtools

    # `error` parameter must exist!
    def error_login(error):
        # check exception instance, in this case it's missing required argument
        if isinstance(error, cmdtools.MissingRequiredArgument):
            if error.param == "user":
                print("user is required!")
            elif error.param == "password":
                print("password is required!")
        else:
            # if other error occured, raise the exception
            # otherwise it would be suppressed by the processor
            raise error

    def login(user, password):
        print("Login success!")

    cmd = cmdtools.Cmd("!login admin", prefix='!')

    if cmd.name == "login":
        # pass `login` callback and `error_login` callback to processor
        cmd.process_cmd(login, error_login)
