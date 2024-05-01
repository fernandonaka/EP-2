linha = ["-"]*12
saida = [[" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", " "]]

for i in linha:
    saida.append(linha)
    
saida[1][0] = "1"
saida[1][11] = "1"
    
saida[2][0] = "2"
saida[2][11] = "2"
    
saida[3][0] = "3"
saida[3][11] = "3"
    
saida[4][0] = "4"
saida[4][11] = "4"
    
saida[5][0] = "5"
saida[5][11] = "5"

saida[6][0] = "6"
saida[6][11] = "6"

saida[7][0] = "7"
saida[7][11] = "7"

saida[8][0] = "8"
saida[8][11] = "8"

saida[9][0] = "9"
saida[9][11] = "9"

saida[10][0] = "10"
saida[10][11] = "10"

saida.append([" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", " "])


for linha in saida:
    print(" ".join(linha))