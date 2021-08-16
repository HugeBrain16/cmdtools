import unittest
import cmdtools


class TestProcess(unittest.TestCase):
    def test_process(self):
        cmd = "/sum 10 10 10"
        cmd = cmdtools.Cmd(cmd, convert_args=True)

        res = cmd.process_cmd(TestProcess.sum)

        self.assertEqual(res, 30, "boo")

    def test_match(self):
        cmd = '/sell "Gold" 50'
        cmd = cmdtools.Cmd(cmd, convert_args=True)

        match = cmd.match_args("si")

        self.assertTrue(match, "boo")

    def test_match_(self):
        cmd = "/add 10 40 20 59"
        cmd = cmdtools.Cmd(cmd, convert_args=True)

        match = cmd.match_args(("i" * len(cmd.args)))

        self.assertTrue(match, "boo")

    def test_default(self):
        cmd = "/get"
        cmd = cmdtools.Cmd(cmd)

        res = cmd.process_cmd(TestProcess.get)

        self.assertEqual("Hello World", res)

    def get(text="Hello World"):
        return text

    def sum(*args):
        return sum(args)
