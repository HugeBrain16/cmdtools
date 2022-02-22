import cmdtools


@cmdtools.callback.callback_init
def _test_attr(ctx: cmdtools.callback.Context):
    assert ctx.attrs.secret == "1234"


def test_attr():
    cmd = cmdtools.Cmd("/test_attr")
    executor = cmdtools.Executor(cmd, _test_attr, attrs={"secret": "1234"})
    executor.exec()
