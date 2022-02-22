from gc import callbacks
import unittest
import cmdtools

@cmdtools.callback.callback_init
def sumcmd(ctx: cmdtools.callback.Context):
    args2int = [int(arg) for arg in ctx.command.args]
    
    return sum(args2int)

class TestExec(unittest.TestCase):
    def test_process(self):
        cmd = cmdtools.Cmd("/sum 10 10 10")
        executor = cmdtools.Executor(cmd, sumcmd)
        res = executor.exec()

        self.assertEqual(res, 30)
