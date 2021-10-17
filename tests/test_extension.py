import asyncio
import cmdtools
from cmdtools.ext import command
from unittest import TestCase

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
            if isinstance(self.test, TestCase):
                self.test.assertEqual(self.num, 10)

    def error_notcool(self, error):
        if hasattr(self, "test"):
            if isinstance(self.test, TestCase):
                self.test.assertEqual(self.num, 10)

        raise error


class TestExtension(TestCase):
    async def run_cmd(self):
        a = 10
        b = 10

        cmd = cmdtools.Cmd(f"/cool {a} {b}", convert_args=True)
        result = await group.run(cmd)
        self.assertEqual(result, a + b)

    async def run_attr(self):
        cmd = cmdtools.Cmd("/notcool")
        await group.run(cmd, attrs={"test": self, "num": 10})

    def test_run(self):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self.run_cmd())
        loop.run_until_complete(self.run_attr())
        loop.close()
