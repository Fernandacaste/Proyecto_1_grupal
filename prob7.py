def preb_7 (x):
	multiplos=[]
	for x in range(totalva):
		is_multiple = multiple (x)

		if is_multiple	:
			multiplos.append(x)
resultado = eval("+".join(map(str, multiplos)))
print(resultado	)