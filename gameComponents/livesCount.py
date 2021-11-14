def playerlivesdisplay(playerLives):
	smile = "\U0001F9E1"
	s = ""
	for i in range(playerLives):
		s = s + smile
	print(s)
	
def computerlivesdisplay(computerLives):
	machine = "\U0001F4BB"
	m = ""
	for i in range(computerLives):
		m = m + machine
	print(m)
	