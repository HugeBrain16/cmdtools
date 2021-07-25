import cmdtools

def e_attrtest(error):
	# attributes also get passed to error callback
	print("in error callback:", e_attrtest.name)

def attrtest():
	print(attrtest.name)
	# 1 / 0 # invoke error callback

cmd = cmdtools.Cmd("/invoke")
cmd.process_cmd(attrtest, e_attrtest,
	# assign attributes
	attrs={
		"name": "Joe"
	}
)