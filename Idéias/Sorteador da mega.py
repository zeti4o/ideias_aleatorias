from random import randint
print('=' * 20)
print(' ')
print(' Bem vindo ao sorteador de números da mega boa sorte :)\n')
vl5 = str(randint(1,50))
vl6 = str(randint(1,50))
vl7 = str(randint(1,50))
vl8 = str(randint(1,50))
vl1 = str(input(' Digite o primeiro número: ')).strip()
vl2 = str(input(' Digite o segundo número: ')).strip()
vl3 = str(input(' Digite o terceiro número: ')).strip()
vl4 = str(input(' Digite o quarto número: ')).strip()
print(' ')
resultado = [vl5,vl6,vl7,vl8]
aposta = [vl1,vl2,vl3,vl4]
if aposta == resultado:
	print(' Parabéns você ganhou!!!!')
else:
	print(' Pobre é um bicho azarado e por falar em bicho é melhor jogar no bicho')
	print(f' O resultado foi: {resultado}')
print('')
print('=' * 20)
