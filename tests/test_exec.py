import unittest
import cmdtools


@cmdtools.callback.callback_init
def sumcmd(ctx: cmdtools.callback.Context):
    args2int = [int(arg) for arg in ctx.command.args]

    return sum(args2int)


@cmdtools.callback.add_option("num", default=1, type=int)
def retnum(ctx: cmdtools.callback.Context):
    return ctx.options.num


class TestExec(unittest.TestCase):
    def test_process(self):
        cmd = cmdtools.Cmd("/sum 10 10 10")
        executor = cmdtools.Executor(cmd, sumcmd)
        res = executor.exec()

        self.assertEqual(res, 30)

    def test_options(self):
        cmd1 = cmdtools.Cmd("/retnum 2")
        cmd2 = cmdtools.Cmd("/retnum")
        exc1 = cmdtools.Executor(cmd1, retnum)
        exc2 = cmdtools.Executor(cmd2, retnum)

        self.assertEqual(exc1.exec(), 2)
        self.assertEqual(exc2.exec(), 1)
