import cmdtools
from unittest import IsolatedAsyncioTestCase
from cmdtools.ext.command import Group, Command

test = Group("Test")


@test.command()
def sumcmd(ctx):
    args2int = [int(arg) for arg in ctx.command.args]

    return sum(args2int)


@test.command()
class Secret(Command):
    __aliases__ = ["supersecretcommand"]

    def __init__(self):
        super().__init__(name="secret")

    def secret(self, ctx):
        return "1234"


class TestCommandExt(IsolatedAsyncioTestCase):
    async def test_group_wrapper(self):
        cmd1 = cmdtools.Cmd("/sumcmd 10 10 10")
        out = await test.run(cmd1)

        self.assertEqual(out, 30)

    async def test_command_struct(self):
        cmd = cmdtools.Cmd("/secret")
        out = await test.run(cmd)

        self.assertEqual(out, "1234")

    async def test_command_struct_aliases(self):
        cmd = cmdtools.Cmd("/supersecretcommand")
        out = await test.run(cmd)

        self.assertEqual(out, "1234")
