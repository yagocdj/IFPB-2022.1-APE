"""Um motorista anota a marcação do hodômetro do seu veículo antes e após uma viagem,
bem como o número de litros de combustível gastos.
Escreva um programa que leia os 3 dados acima, o preço do litro de combustível, a
capacidade do tanque e mostre:
a) Quilometragem rodada.
b) Quantos quilômetros por litro faz o veículo.
c) Autonomia do veículo.
d) Custo da viagem.
"""

hodometroInicial = float(input('Informe o quilometragem assinalada no hodômetro do seu veículo no início da viagem:'))
hodometroFinal = float(input('Agora indique a quilometragem ao final da viagem:'))
combustivelGasto = float(input('Informe o quanto você gastou de combustível em litros:'))
capacidadeTanque = float(input('Infome a capacidade máxima do tanque do seu veículo:'))
precoCombustivel = float(input('Informe o preço atual do combustível em reais por litro:'))

quilometragemRodada = hodometroFinal - hodometroInicial
consumoMedio = quilometragemRodada / combustivelGasto
autonomia = consumoMedio * capacidadeTanque
custoViagem = precoCombustivel * combustivelGasto

print(f'Você rodou {quilometragemRodada}km.')
print(f'Seu veículo faz {consumoMedio:.2f}km/L.')
print(f'A autonomia do seu veículo é de {autonomia:.2f}km.')
print(f'O custo da sua viagem foi de R${custoViagem:.2f}.')
