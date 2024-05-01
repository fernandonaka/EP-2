### codigo 2

def posicao_suporta(mapa,blocos,linha,coluna,orientacao):
   
    n = len(mapa)

    if orientacao == 'h':
        if coluna + blocos > n:
            return False
    if orientacao == 'v':
        if linha + blocos > n:
            return False
    
    for i in range(blocos):
        if orientacao == 'h':
            if mapa[linha][coluna+i] != ' ':
                return False
        if orientacao == 'v':
            if mapa[linha+i][coluna] != ' ':
                return False
    return True


#### codigo 3
import random

def posicao (mapa,blocos,linha,coluna,orientacao):
    n = len(mapa)
    if orientacao == 'h':
        for i in range(coluna, blocos + coluna):
            mapa[linha][i] = 'N'
    if orientacao == 'v':
        for i in range(linha, blocos + linha):
            mapa[i][coluna] = 'N'

    return mapa

def posicao_suporta(mapa,blocos,linha,coluna,orientacao):
   
    n = len(mapa)

    if orientacao == 'h':
        if coluna + blocos > n:
            return False
    if orientacao == 'v':
        if linha + blocos > n:
            return False
    
    for i in range(blocos):
        if orientacao == 'h':
            if mapa[linha][coluna+i] != ' ':
                return False
        if orientacao == 'v':
            if mapa[linha+i][coluna] != ' ':
                return False
    return True
            
def aloca_navios(mapa,lista):
    n = len(mapa)
    linha = random.randint(0, n-1)
    coluna = random.randint(0, n-1)
    orientacao = random.choice(['h', 'v'])

    for blocos in lista:
        aloca = posicao_suporta(mapa,blocos,linha,coluna,orientacao)
        while aloca == False:
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])
            aloca = posicao_suporta(mapa,blocos,linha,coluna,orientacao)
        
        aloca_no_mapa = posicao(mapa,blocos,linha,coluna,orientacao)
        
        

    return aloca_no_mapa


### codigo 4
def foi_derrotado (matriz):

    n = len(matriz)

    for i in range(n):
        for j in range (n):
            if matriz[i][j] == 'N':
                return False


    return True