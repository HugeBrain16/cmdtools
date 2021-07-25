import cmdtools

def error_say(error):
	if isinstance(error, cmdtools.MissingRequiredArgument):
		if error.param == "text":
			print("text is required!")

def say(text):
	print(text)

cmd = cmdtools.Cmd("/say Hello")
# cmd = cmdtools.Cmd("/say") # this will call error handler

if cmd.name == "say":
	cmd.process_cmd(say, error_say)

# using python error handler
# try:
# 	cmd.process_cmd(say)
# except cmdtools.ProcessError as error:
# 	if isinstance(error.exception, cmdtools.MissingRequiredArgument):
# 		if error.exception.param == "text":
# 			print("text is required")
