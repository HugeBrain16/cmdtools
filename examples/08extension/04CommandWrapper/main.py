import asyncio
import cmdtools
from cmdtools.ext.command import CommandWrapper, Command

wrapper = CommandWrapper()


@wrapper.command(name='ping')
def ping():
    print("Pong!")


@wrapper.command(name='say', aliases=["echo", ])
def say(*text_):
    if text_:
        text = " ".join(text_)
    else:
        raise cmdtools.MissingRequiredArgument("invoke", "text_")

    print(text)


@say.error
def error_say(error):
    if isinstance(error, cmdtools.MissingRequiredArgument):
        if error.param == "text_":
            print("Text is required!")


@wrapper.command()
class Joke(Command):
    def __init__(self):
        super().__init__(name="joke")

    def joke(self):
        print("Your mom 😂👌🔥💯!?!")


asyncio.run(
    wrapper.run(cmdtools.Cmd("/ping"))
)
