import unittest
import cmdtools


class TestParse(unittest.TestCase):
    def test_parse(self):
        cmd = '/say "hello world"'
        cmd = cmdtools.Cmd(cmd)

        self.assertEqual("say", cmd.name, "boo")
        self.assertIn("hello world", cmd.args, "boo")

    def test_parse_convert(self):
        cmd = "/sum 504 100.0 .54 10."
        cmd = cmdtools.Cmd(cmd, convert_args=True)

        self.assertIsInstance(cmd.args[0], int, "boo")
        self.assertIsInstance(sum(cmd.args[1:]), float, "boo")

    def test_prefix_parser(self):
        cmd0 = cmdtools.Parser("!ping", "!")
        cmd1 = cmdtools.Parser("b!ping", "b!")
        cmd2 = cmdtools.Parser("zu ping", "zu")

        self.assertEqual(cmd0.args, "ping")
        self.assertEqual(cmd1.args, "ping")
        self.assertEqual(cmd2.args, "ping")
