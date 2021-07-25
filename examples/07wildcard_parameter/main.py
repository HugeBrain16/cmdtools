import cmdtools

def e_say(error):
	if isinstance(error, cmdtools.MissingRequiredArgument):
		if error.param == "text_":
			print("text is required")

def say(*text_):
	text = None

	# arguments are splitted by whitespace
	# if not surrounded by quotes or double quotes
	
	# join them together to actual string (???)
	if text_:
		text = " ".join(text_)

	print(text)

cmd = cmdtools.Cmd("/say hey this is actually works!")

cmd.process_cmd(say, e_say)
