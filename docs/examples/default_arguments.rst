Default Arguments
=================

.. code:: py
    
    import cmdtools
    
    def say(text, name="Someone"):
        print(f"{name} sez, {text}")
        
    cmd = cmdtools.Cmd("!say '𝒥 𝒶𝓂 𝒶 𝑀𝒶𝓃 𝑜𝒻 𝐹𝑜𝓇𝓉𝓊𝓃𝑒, 𝒶𝓃𝒹 𝒥 𝓂𝓊𝓈𝓉 𝓈𝑒𝑒𝓀 𝓂𝓎 𝐹𝑜𝓇𝓉𝓊𝓃𝑒'", prefix='!')

    if cmd.name:
        cmd.process_cmd(say)
