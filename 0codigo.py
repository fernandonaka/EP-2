def cria_mapa(N):
    linha = ["-"]*N
    saida = []

    for i in linha:
        saida.append(linha)
    
    for linha in saida:
        print(" ".join(linha))

cria_mapa(12)
