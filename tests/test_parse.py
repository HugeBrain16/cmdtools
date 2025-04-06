import unittest
import cmdtools
from cmdtools import Cmd
from cmdtools.callback import Options, Option
from cmdtools.utils.string import PrefixChecker
from cmdtools.ext.param import apply_params


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

    def test_parse_param(self):
        cmd = Cmd('/spawn 101 x=1.0 z=1.0')
        options = Options([
            Option("id"),
            Option("x", default="0.0"),
            Option("y", default="0.0"),
            Option("z", default="0.0")
        ])

        apply_params(cmd, options)

        self.assertEqual(options.id, "101")
        self.assertEqual(options.x, "1.0")
        self.assertEqual(options.y, None)
        self.assertEqual(options.z, "1.0")

    def test_parse_param_with_quotes(self):
        cmd = Cmd('/query user="asdf123" quote=\'"4" is my favorite number\'')
        options = Options([
            Option("user"),
            Option("quote")
        ])

        apply_params(cmd, options)

        self.assertEqual(options.user, "asdf123")
        self.assertEqual(options.quote, '"4" is my favorite number')
