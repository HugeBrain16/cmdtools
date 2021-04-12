# cmdtools
module for parsing and processing commands.

### Example
```py
import cmdtools

def greet(raw_args, args):
    print(f"Hello, {greet.name}, nice to meet you")

cmd = '/greet "Josh"'
_cmd = cmdtools.ParseCmd(cmd)

cmdtools.ProcessCmd(_cmd, greet,
    attr= { # assign attributes to the callback
        'name': _cmd['args'][0]
    }
)
```
