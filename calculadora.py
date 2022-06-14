a = int(input('Qual é o "a" dessa equação?'))
b = int(input('Qual é o "b" dessa equação?'))
c = int(input('Qual é o "c" dessa equação?'))
delta1 = b ** 2
delta2 = 4 * a * c
delta3 = delta1 - delta2
print('O seu ∆ vale:')
print(delta3)
print('')
if delta3 >= 0 :
	import math
	raiz_delta = math.sqrt(delta3)
	x_1 = -b + raiz_delta
	x1 = x_1 / 2
	x_2 = -b - raiz_delta
	x2 = x_2 / 2
	if delta3 == 0 :
		print("Já que o delta tem valor nulo a equação tem apenas uma raiz.")
		print('x =', x1)
	else:
		print("x'=", x1)
		print('x"=', x2)
else:
	print('Como o seu delta é negativo o resultado da sua equação não está nos reais e essa calculadora não foi progamada pra isso ainda!')