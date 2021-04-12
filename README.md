# cmdtools
a module for parsing and processing commands.
  
## Installation
to install this module you can use the methods below 
  
using pip: 
    - from pypi: `pip install cmdtools-py`  
    - from github repository: `pip install git+https://github.com/HugeBrain16/cmdtools.git`  
  
from source: `python setup.py install`  

## Functions
  
#### ParseArgs
Parse text commands into dictionary
  
##### Arguments
- `command_string`
    + command string to parse
- `prefix`
    + prefix of the command, Default: `/`
- `max_args`
    + max arguments, the rest are just empty, Default: `64`
- `eval`
    + eval...? like data types conversion...? yeah, Default: `False` 
  
#### _EvalCmd
Uhh... this does something like data conversion for command arguments
  
##### Arguments
- `parsed_command`
    + parsed command in a `dict` object

#### MatchArgs
Matches arguments by argument data types

##### Arguments
- `parsed_command`
    + parsed command in a `dict` object
- `format`
    + format
- `max_args`
    + max arguments matches, Default: `0`
  
## Examples
Basic example
```py
import cmdtools

def ping(raw_args, args):
    print("pong.")

cmd = '/ping'
_cmd = cmdtools.ParseCmd(cmd)

cmdtools.ProcessCmd(_cmd, ping)
```
  
Parse command with arguments
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
  
Parsing command with more than one argument and different data types
```py
import cmdtools

def give(raw_args, args):
    print(f"You gave {give.item_amount} {give.item_name}s to {give.name}")

cmd = '/give "Josh" "Apple" 10'
_cmd = cmdtools.ParseCmd(cmd, eval=True) # we're going to use `MatchArgs` function which only supported for `eval` parsed command arguments

# check command
if cmdtools.MatchArgs(_cmd, 'ssi', max_args=3): # format indicates ['str','str','int'], only match 3 arguments
    cmdtools.ProcessCmd(_cmd, give,
        attr={
            'name': _cmd['args'][0],
            'item_name': _cmd['args'][1],
            'item_amount': _cmd['args'][2]
        }
    )
else:
    print('Correct Usage: /give <name: [str]> <item-name: [str]> <item-amount: [int]>')
```