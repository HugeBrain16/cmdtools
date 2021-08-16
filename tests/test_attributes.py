import cmdtools

def _test_func():
	assert _test_func.test == 20

def test_def_attributes():
	cmd = cmdtools.Cmd("/test")
	setattr(_test_func, "test", 40)
	cmd.process_cmd(_test_func, attrs={"test": 20})

	assert _test_func.test == 40
