import exmplpckg as ep

P1 = [0,0]
P2 = [10,10]
	
linf = ep.LinearFunction(P1,P2)

print(linf.calc_y(P2[0]))

ep.plot_linf(linf)