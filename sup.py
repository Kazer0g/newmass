with open('sup.txt', 'w') as f:
	hv = 18600
	step = 0
	while hv > 12000:
		f.write(str(step**3) + ' ' + str(hv) + '\n')
		step += 1
		hv -= 50