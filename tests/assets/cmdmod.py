import cmdtools
from cmdtools.ext.command import Command


@cmdtools.callback.callback_init
def cmdmod(ctx):
    return 1234


class CmdMod(Command):
    def __init__(self):
        super().__init__("cmdmod")

    def cmdmod(self, ctx):
        return 1234
