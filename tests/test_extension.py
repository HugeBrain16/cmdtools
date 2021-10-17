import asyncio
import cmdtools
from cmdtools.ext import command
from unittest import IsolatedAsyncioTestCase

group = command.CommandWrapper()


@group.command()
class Cool(command.Command):
    def __init__(self):
        super().__init__(name="cool")

    def cool(self, a, b):
        return a + b


@group.command()
class NotCool(command.Command):
    def __init__(self):
        super().__init__(name="notcool")

    def notcool(self):
        if hasattr(self, "test"):
            if isinstance(self.test, IsolatedAsyncioTestCase):
                self.test.assertEqual(self.num, 10)

    def error_notcool(self, error):
        if hasattr(self, "test"):
            if isinstance(self.test, IsolatedAsyncioTestCase):
                self.test.assertEqual(self.num, 10)

        raise error


class TestExtension(IsolatedAsyncioTestCase):
    async def test_run(self):
        a = 10
        b = 10

        cmd = cmdtools.Cmd(f"/cool {a} {b}", convert_args=True)
        result = await group.run(cmd)
        self.assertEqual(result, a + b)

    async def test_attr(self):
        cmd = cmdtools.Cmd("/notcool")
        await group.run(cmd, attrs={"test": self, "num": 10})
