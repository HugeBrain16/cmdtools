import unittest
import cmdtools
from cmdtools.utils.string import PrefixChecker


class TestParse(unittest.TestCase):
    def test_parse(self):
        cmd = '/say "hello world"'
        cmd = cmdtools.Cmd(cmd)

        self.assertEqual("say", cmd.name)
        self.assertIn("hello world", cmd.args)

    def test_prefix_checker(self):
        cmd0 = PrefixChecker("!ping", "!")
        cmd1 = PrefixChecker("b!ping", "b!")
        cmd2 = PrefixChecker("zu ping", "zu")

        self.assertEqual(cmd0.strip_prefix, "ping")
        self.assertEqual(cmd1.strip_prefix, "ping")
        self.assertEqual(cmd2.strip_prefix, "ping")
