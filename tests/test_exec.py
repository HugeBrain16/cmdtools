import unittest
import cmdtools


@cmdtools.callback.callback_init
def sumcmd(ctx: cmdtools.callback.Context):
    args2int = [int(arg) for arg in ctx.command.args]

    return sum(args2int)


@cmdtools.callback.add_option("num", default=1, type=int)
def test(ctx: cmdtools.callback.Context):
    return ctx.options.num


class TestExec(unittest.TestCase):
    def test_process(self):
        cmd = cmdtools.Cmd("/sum 10 10 10")
        executor = cmdtools.Executor(cmd, sumcmd)
        res = executor.exec()

        self.assertEqual(res, 30)

    def test_options(self):
        cmd1 = cmdtools.Cmd("/test 2")
        cmd2 = cmdtools.Cmd("/test")
        exc1 = cmdtools.Executor(cmd1, test)
        exc2 = cmdtools.Executor(cmd2, test)

        self.assertEqual(exc1.exec(), 2)
        self.assertEqual(exc2.exec(), 1)
