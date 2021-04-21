# cmdtools
[![tests](https://github.com/HugeBrain16/cmdtools/actions/workflows/python-package.yml/badge.svg)](https://github.com/HugeBrain16/cmdtools/actions/workflows/python-package.yml)
  
a module for parsing and processing commands.
  
## Installation
to install this module you can use the methods below 
  
- using pip: 
    + from pypi: `pip install cmdtools-py`  
    + from github repository: `pip install git+https://github.com/HugeBrain16/cmdtools.git`  
  
- from source: `python setup.py install`  
  
## Examples
Basic example
```py
import cmdtools

def ping():
    print("pong.")

_cmd = cmdtools.Cmd('/ping')
_cmd.parse()

cmdtools.ProcessCmd(_cmd, ping)
```
  
Parse command with arguments
```py
import cmdtools

def greet(name):
    print(f"Hello, {name}, nice to meet you")

_cmd = cmdtools.Cmd('/greet "Josh"')
_cmd.parse()

cmdtools.ProcessCmd(_cmd, greet)
```
  
Parsing command with more than one argument and different data types
```py
import cmdtools

def give(name, item_name, item_amount):
    print(f"You gave {item_amount} {item_name}s to {name}")

_cmd = cmdtools.Cmd('/give "Josh" "Apple" 10')
_cmd.parse(eval_args=True) # we're going to use `MatchArgs` function which only supported for `eval` parsed command arguments

# check command
if cmdtools.MatchArgs(_cmd, 'ssi', max_args=3): # format indicates ['str','str','int'], only match 3 arguments
    cmdtools.ProcessCmd(_cmd, give)
else:
    print('Correct Usage: /give <name: [str]> <item-name: [str]> <item-amount: [int]>')
```
  
command with attributes
```py
import cmdtools

def test():
    print(test.text)

_cmd = cmdtools.Cmd('/test')
_cmd.parse()

cmdtools.ProcessCmd(_cmd, test,
    attrs={ # assign attributes to the callback
        'text': "Hello World"
    }
)
```
  
command with error handling example
```py
import cmdtools

def error_add(error):
    if isinstance(error, cmdtools.MissingRequiredArgument):
        if error.param == 'num1':
            print('you need to specify the first number')
        if error.param == 'num2':
            print('you need to specify the second number')

def add(num1, num2):
    print(num1 + num2)

cmd = cmdtools.Cmd('/add')
cmd.parse(eval_args=True)

cmdtools.ProcessCmd(cmd, add, error_add)
```
  
asyncio support
```py
import cmdtools
import asyncio

async def _say(text):
    print(text)

async def main():
    cmd = cmdtools.Cmd('/say "Hello World"')
    cmd.parse()

    await cmdtools.AioProcessCmd(cmd, _say)

asyncio.run(main())
```
  
## Exceptions
- ParsingError
- MissingRequiredArgument
- ProcessError