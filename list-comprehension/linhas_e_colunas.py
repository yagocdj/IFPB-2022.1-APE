linhas_e_colunas = [
    (x, y)
    if y != 2 else (x, y * 1000)
    for x in range(10)
    for y in range(5)
    if x != 2
]

print(linhas_e_colunas)
