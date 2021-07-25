import cmdtools

def ping():
	print("pong!")

cmd = cmdtools.Cmd("/ping")

if cmd.name == "ping":
	cmd.process_cmd(ping)
