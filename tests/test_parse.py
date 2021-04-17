import unittest
from .. import cmdtools


class TestParse(unittest.TestCase):
    def test_parse(self):
        cmd = '/say "hello world"'
        cmd = cmdtools.Cmd(cmd)
        cmd.parse()

        self.assertEqual("say", cmd.name, "boo")
        self.assertIn("hello world", cmd.args, "boo")

    def test_parse_eval(self):
        cmd = "/sum 504 100.0 .54 10."
        cmd = cmdtools.Cmd(cmd)
        cmd.parse(eval_args=True)

        self.assertIsInstance(cmd.args[0], int, "boo")
        self.assertIsInstance(sum(cmd.args[1:]), float, "boo")
