import unittest
from .. import cmdtools

class TestError(unittest.TestCase):
	def test_error(self):
		cmd = cmdtools.Cmd('/say')

	def say(text):
		print(text)

	def error_say(self, error):
		if isinstance(error, cmdtools.ArgumentError):
			self.assertEqual(error.param, 'text', 'boo')

			if error.param == 'text':
				print('you need to specify a message to say')