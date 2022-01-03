Default Arguments
=================

.. code:: py
    
    import cmdtools
    
    def say(text, name="Someone"):
        print(f"{name} sez, {text}")
        
    cmd = cmdtools.Cmd("!say 'Very good!, very good!, yay!'", prefix='!')

    if cmd.name:
        cmd.process_cmd(say)
