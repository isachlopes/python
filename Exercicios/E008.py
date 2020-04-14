#escreva um programa que leia um valor em metros e o exiba convertido em centimentros e milimetros
n = float(input('Digite uma distância em metros: '))
cm = n*100
mm = n*1000
print('O valor de {}m equivale a {:.0f}cm e a {:.0f}mm.'.format(n, cm, mm))
