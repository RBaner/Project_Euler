#p28

def spiral_sum():
	total = 1
	start = 1
	for diff in range(2,1001,2):
		for i in range(1,5):
			total += start+diff*i
			if i==4:
				start = start+diff*i
	return(total)
