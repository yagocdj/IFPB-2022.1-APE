n = int(input())  # número de mensagens trazidas pelo ancião
mensagens = [input() for i in range(n)]
contador_fada = 0

# percorrendo cada mensagem e verificando se há pelo menos um trecho "fada"
# nelas
for mensagem in mensagens:
    if (mensagem.count('fada') >= 1) or (mensagem.count('fadA') >= 1) or \
            (mensagem.count('faDa') >= 1) or (mensagem.count('faDA') >= 1) or \
            (mensagem.count('fAda') >= 1) or (mensagem.count('fAdA') >= 1) or \
            (mensagem.count('fADa') >= 1) or (mensagem.count('fADA') >= 1) or \
            (mensagem.count('Fada') >= 1) or (mensagem.count('FadA') >= 1) or \
            (mensagem.count('FaDa') >= 1) or (mensagem.count('FaDA') >= 1) or \
            (mensagem.count('FAda') >= 1) or (mensagem.count('FAdA') >= 1) or \
            (mensagem.count('FADa') >= 1) or (mensagem.count('FADA') >= 1):
        contador_fada += 1
print(contador_fada)

# simplificado
n = int(input())  # número de mensagens trazidas pelo ancião
mensagens = [input() for i in range(n)]
contador_fada = 0

# percorrendo cada mensagem e verificando se há pelo menos um trecho "fada"
# nelas
for mensagem in mensagens:
    mensagem.lower()
    if mensagem.count('fada') >= 1:
        contador_fada += 1
print(contador_fada)
