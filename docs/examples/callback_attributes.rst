Callback and Struct Attributes
==============================

You can pass some attributes to command callback or struct

Callback
--------

.. code:: py
    
    import cmdtools
    
    def send(item):
        print(f"Sending {item}...")\
    
        # access passed attributes from function object
        print(send.secret)

    cmd = cmdtools.Cmd("!send chocolate", prefix='!')
    
    if cmd.name:
        # pass some attributes to command processor
        cmd.process_cmd(cmd, attrs={
                "secret": "S9ic9109is90icx9iq"
            }
        )

Struct or Class
---------------

.. code:: py

    import cmdtools
    from cmdtools.ext.command import Command, CommandRunner

    class Send(Command):
        def __init__(self):
            super().__init__(name="send")

        def send(self, item):
            print(f"Sending {item}...")
            
            # access passed attributes from 'self'
            print(self.secret)

    runner = CommandRunner(Send())

    cmd = cmdtools.Cmd("!send chocolate", prefix='!')

    if cmd.name:
        runner.run(cmd, attrs={
                "secret": "S9ic9109is90icx9iq"
            }
        )
