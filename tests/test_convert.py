import unittest
import cmdtools


@cmdtools.callback.add_option("num1", type=int)
@cmdtools.callback.add_option("num2", type=int)
def add(ctx):
    return ctx.options.num1 + ctx.options.num2


class TestConverter(unittest.TestCase):
    def test_convert(self):
        executor = cmdtools.Executor(cmdtools.Cmd("/add 1 1"), add)
        out = executor.exec()

        self.assertEqual(out, 2)
