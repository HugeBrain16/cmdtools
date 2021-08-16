import cmdtools


def test_error():
    cmd = cmdtools.Cmd("/say")

    cmd.process_cmd(say, error_say)


def say(text):
    print(text)


def error_say(error):
    if isinstance(error, cmdtools.MissingRequiredArgument):
        assert error.param == "text", "boo"


def test_default_error():
    cmd = cmdtools.Cmd("/say")

    cmd.process_cmd(default_say, error_default_say)


def default_say(text, name="No"):
    print(f"{name} says: {text}")


def error_default_say(error):
    if isinstance(error, cmdtools.MissingRequiredArgument):
        assert error.param == "text", "boo"
