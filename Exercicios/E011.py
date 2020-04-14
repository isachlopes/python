#Faça um programa que leia a altura e a largura de uma parade em metros, Calcule a sua área e a quantidade de tinta necessaria
#sabendo que cada litro de tinta pinta 2m²
larg = float(input('Diga a largura da parede: '))
alt = float(input('Agora diga a altura da parede: '))
área = larg*alt
print('Sua parede tem a dimensão de {}x{} com área de {}m².'.format(larg, alt, área))
tinta = área/2
print('Para pintar essa parede, são necessários {}l de tinta.'.format(tinta))
