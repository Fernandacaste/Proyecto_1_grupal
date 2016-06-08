def prob_4 (n, palabra):
	cas=(n-len(palabra))//2
	cas2 = n - (cas + len(palabra))
	return "*" * cas + palabra + "*" * cas2