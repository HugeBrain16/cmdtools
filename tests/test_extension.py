import cmdtools
import unittest
from cmdtools.ext import command

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
            if isinstance(self.test, unittest.TestCase):
                self.test.assertEqual(self.num, 10)

    def error_notcool(self, error):
        if hasattr(self, "test"):
            if isinstance(self.test, unittest.TestCase):
                self.test.assertEqual(self.num, 10)

        raise error


class TestExtension(unittest.TestCase):
    def test_run(self):
        a = 10
        b = 10

        cmd = cmdtools.Cmd(f"/cool {a} {b}", convert_args=True)
        result = group.run(cmd)
        self.assertEqual(result, a + b)

    def test_attr(self):
        cmd = cmdtools.Cmd("/notcool")
        group.run(cmd, attrs={"test": self, "num": 10})
