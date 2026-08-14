PI = float(3.14)
R1 = float(input('Escreva o raio maior do sólido (em cm):'))
R2 = float(input('Escreva o raio menor do sólido(em cm):'))
H = float(input('Escreva a altura do sólido:'))
Volume = (PI * H * (R1 ** 2 + R2 ** 2 + R1 * R2)) / 3
print('O volume do tronco de cone é:', Volume, 'cm³.')