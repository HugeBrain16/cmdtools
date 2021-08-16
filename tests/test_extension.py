import asyncio
from .. import cmdtools
from ..cmdtools.ext import command


class Add(command.Command):
    def __init__(self):
        self.result = None
        self.name = "add"
        super().__init__(name=self.name)

    def add(self, n1, n2):
        self.result = n1 + n2


async def _test_class_cmd():
    runner = command.CommandRunner(Add())
    await runner.run(
        cmdtools.Cmd("/add 40 40", convert_args=True)
    )

    assert runner.command.result == 80
    assert runner.command.name == "add"


def test_class_cmd_run():
    asyncio.run(_test_class_cmd())


wrapper = command.CommandWrapper()


@wrapper.command(name='add', aliases=['plus'])
def add(n, y):
    return n + y


def test_command_wrapper():
    result = asyncio.run(
        wrapper.run(cmdtools.Cmd('/add 10 10', convert_args=True))
    )

    assert result == 20
    assert 'plus' in add.aliases
