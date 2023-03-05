import cmdtools
from unittest import IsolatedAsyncioTestCase
from cmdtools.ext.command import Group, Command, Container

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


@test.command(name="dectest", aliases=["dt", "decor"])
class DecoratorTest(Command):
    def dectest(self, ctx):
        return ctx


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

    async def test_container(self):
        cont = Container([Command("foo"), Command("bar")])

        self.assertTrue(cont.has_command("foo"))
        self.assertTrue(cont.has_command("bar"))

    async def test_decorator(self):
        cmd = test.get_command("dectest")

        self.assertEqual(cmd.name, "dectest")
        self.assertEqual(cmd.callback.func.__name__, "dectest")
        self.assertIn("dt", cmd.aliases)
        self.assertIn("decor", cmd.aliases)
