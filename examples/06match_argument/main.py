import cmdtools

def e_add(error):
	if isinstance(error, cmdtools.MissingRequiredArgument):
		if error.param == "x":
			print("x is required: int")

		if error.param == "y":
			print("y is required: int")

def add(x, y):
	return x + y

cmd = cmdtools.Cmd("/add 1 3", convert_args=True) # `convert_args` argument must be set to true

if cmd.name == "add":
	# 'ii' represent as integer, integer
	# only match 2 arguments
	if cmd.match_args("ii", max_args=2):
		result = cmd.process_cmd(add, e_add)

		if result:
			print("result:", result)
	else:
		print(f"Correct usage: {cmd.prefix}add <x:int> <y:int>")
