import inspect
from typing import Any, Dict, List, Optional, Union

from cmdtools import Cmd, Executor
from cmdtools.callback import Attributes, Callback, ErrorCallback
from cmdtools.callback.option import OptionModifier


class BaseCommand:
    _callback: Callback
    _errcall: ErrorCallback

    def __init__(self, name: str):
        self.name = name

        self._callback = None
        self._errcall = None

    def __getattr__(self, name: str, fallback=None) -> Any:
        return getattr(self, name, fallback)

    @property
    def callback(self) -> Optional[Callback]:
        if not isinstance(self._callback, Callback):
            func: Callable = self.__getattr__(self.name)

            if inspect.ismethod(func):
                self._callback = Callback(func)
                return self._callback
        else:
            return self._callback

    @property
    def error_callback(self) -> Optional[ErrorCallback]:
        if not isinstance(self._errcall, ErrorCallback):
            func: Callable = self.__getattr__("error_" + self.name)

            if inspect.ismethod(func):
                self._errcall = ErrorCallback(func)
                return self._errcall
        else:
            return self._errcall

    def add_option(
        self,
        name: str,
        *,
        default: Any = None,
        modifier: OptionModifier = OptionModifier.NoModifier,
    ):
        self.callback.options.add(name, default, modifier, append=True)


class Command(BaseCommand):
    def __init__(self, name: str, aliases: List[str] = None):
        if aliases is None:
            aliases = []
        self._aliases = aliases
        super().__init__(name)

    @property
    def aliases(self) -> List[str]:
        if self._aliases:
            return self._aliases

        return self.__getattr__("__aliases__", [])


class GroupWrapper(Command):
    def __init__(self, name: str, aliases: List[str] = None):
        super().__init__(name, aliases)

    def __call__(self, *args, **kwargs):
        return self._callback(*args, **kwargs)

    @property
    def error_callback(self) -> Optional[ErrorCallback]:
        return self._callback.errcall


class Group:
    def __init__(self, name: str, commands: List[Command] = None):
        self.name = name

        if commands is None:
            commands = []

        self.commands = []

    def command(self, name: str = None, *, aliases: List[str] = None):
        if aliases is None:
            aliases = []

        def decorator(obj):
            if inspect.isclass(obj) and Command in inspect.getmro(obj):
                self.commands.append(obj())
            else:
                wrapper = GroupWrapper(name or obj.__name__, aliases)
                wrapper._callback = Callback(obj)
                self.commands.append(wrapper)
            return obj

        return decorator

    async def run(
        self, command: Cmd, *, attributes: Union[Attributes, Dict[str, Any]] = None
    ):
        if attributes is None:
            attributes = {}

        for cmd in self.commands:
            if cmd.name == command.name or command.name in cmd.aliases:
                executor = Executor(command, cmd.callback, attributes=attributes)

                if cmd.callback.is_coroutine:
                    return await executor.exec_coro()

                return executor.exec()

        raise NameError(f"Command not found: {command.name}")
