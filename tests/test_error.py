import cmdtools

@cmdtools.callback.add_option("message")
def _test_error(ctx: cmdtools.callback.Context):
    ...

@_test_error.error
def error_test_error(ctx: cmdtools.callback.ErrorContext):
    if isinstance(ctx.error, cmdtools.NotEnoughArgumentError):
        assert ctx.error.option == "message"

def test_error():
    cmd = cmdtools.Cmd("/test_error")
    executor = cmdtools.Executor(cmd, _test_error)
    executor.exec()
