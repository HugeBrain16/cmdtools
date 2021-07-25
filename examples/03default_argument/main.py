import cmdtools

def say(text="No text", name="No name"):
	print(text)

# you can override default argument by providing an argument in an ordered index (???)
"/say \"a text!\"" # to override text default argument

cmd = cmdtools.Cmd("/say")

if cmd.name == "say":
	cmd.process_cmd(say)
