import asyncio
import cmdtools
from cmdtools.ext.command import CommandWrapper

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


asyncio.run(
    wrapper.run(cmdtools.Cmd("/ping"))
)
