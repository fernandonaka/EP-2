saida = [[" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", " "]]

for i in range(1, 11):
    linha = ["-"] * 12
    linha[0] = str(i)
    linha[11] = str(i)
    saida.append(linha)

saida.append([" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", " "])

for linha in saida:
    print(" ".join(linha))