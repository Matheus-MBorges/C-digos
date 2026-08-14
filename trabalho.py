K = int(input())
x, y = input().split()
Ntrain = int(x)
Ntest = int(y)
num_carac = 22

dic_carac_1  = {'b': 0, 'c': 1, 'x': 2, 'f': 3, 'k': 4, 's': 5}
dic_carac_2  = {'f': 0, 'g': 1, 'y': 2, 's': 3}
dic_carac_3  = {'n': 0, 'b': 1, 'c': 2, 'g': 3, 'r': 4, 'p': 5, 'u': 6, 'e': 7, 'w': 8, 'y': 9}
dic_carac_4  = {'t': 0, 'f': 1}
dic_carac_5  = {'a': 0, 'l': 1, 'c': 2, 'y': 3, 'f': 4, 'm': 5, 'n': 6, 'p': 7, 's': 8}
dic_carac_6  = {'a': 0, 'd': 1, 'f': 2, 'n': 3}
dic_carac_7  = {'c': 0, 'w': 1, 'd': 2}
dic_carac_8  = {'b': 0, 'n': 1}
dic_carac_9  = {'k': 0, 'n': 1, 'b': 2, 'h': 3, 'g': 4, 'r': 5, 'o': 6, 'p': 7, 'u': 8, 'e': 9, 'w': 10, 'y': 11}
dic_carac_10 = {'e': 0, 't': 1}
dic_carac_11 = {'b': 0, 'c': 1, 'u': 2, 'e': 3, 'z': 4, 'r': 5, '?': 6}
dic_carac_12 = {'f': 0, 'y': 1, 'k': 2, 's': 3}
dic_carac_13 = {'f': 0, 'y': 1, 'k': 2, 's': 3}
dic_carac_14 = {'n': 0, 'b': 1, 'c': 2, 'g': 3, 'o': 4, 'p': 5, 'e': 6, 'w': 7, 'y': 8}
dic_carac_15 = {'n': 0, 'b': 1, 'c': 2, 'g': 3, 'o': 4, 'p': 5, 'e': 6, 'w': 7, 'y': 8}
dic_carac_16 = {'p': 0, 'u': 1}
dic_carac_17 = {'n': 0, 'o': 1, 'w': 2, 'y': 3}
dic_carac_18 = {'n': 0, 'o': 1, 't': 2}
dic_carac_19 = {'c': 0, 'e': 1, 'f': 2, 'l': 3, 'n': 4, 'p': 5, 's': 6, 'z': 7}
dic_carac_20 = {'k': 0, 'n': 1, 'b': 2, 'h': 3, 'r': 4, 'o': 5, 'u': 6, 'w': 7, 'y': 8}
dic_carac_21 = {'a': 0, 'c': 1, 'n': 2, 's': 3, 'v': 4, 'y': 5}
dic_carac_22 = {'g': 0, 'l': 1, 'm': 2, 'p': 3, 'u': 4, 'w': 5, 'd': 6}

lista_dic = [dic_carac_1,  dic_carac_2,  dic_carac_3,  dic_carac_4,  dic_carac_5, dic_carac_6,  dic_carac_7,  dic_carac_8,  dic_carac_9,  dic_carac_10, dic_carac_11, dic_carac_12, dic_carac_13, dic_carac_14, dic_carac_15, dic_carac_16, dic_carac_17, dic_carac_18, dic_carac_19, dic_carac_20, dic_carac_21, dic_carac_22]

X_train = []
Y_train = []

# leitura características de treino
linha_treino = 0
while linha_treino < Ntrain:
    caracteres = input().split()
    linha_num = []
    coluna = 0
    while coluna < num_carac:
        letra = caracteres[coluna]
        numero = lista_dic[coluna][letra]
        linha_num.append(numero)
        coluna += 1
    X_train.append(linha_num)
    linha_treino += 1

# leitura rotulos treino
rotulo_treino = 0
while rotulo_treino < Ntrain:
    fim_linha = input().strip()
    Y_train.append(fim_linha)
    rotulo_treino += 1

X_test = []

# leitura caracteristicas de teste
t = 0
while t < Ntest:
    caracteres = input().split()
    linha_num = []
    coluna = 0
    while coluna < num_carac:
        letra = caracteres[coluna]
        numero = lista_dic[coluna][letra]
        linha_num.append(numero)
        coluna += 1
    X_test.append(linha_num)
    t += 1

lista_medias = []
coluna = 0
while coluna < num_carac:
    soma_coluna = 0
    linha = 0
    while linha < Ntrain:
        soma_coluna += X_train[linha][coluna]
        linha += 1
    media = soma_coluna / Ntrain
    lista_medias.append(media)
    coluna += 1

lista_desvios = []
coluna = 0

# desvio padrão das variaveis
while coluna < num_carac:
    soma_quadrado = 0
    linha = 0
    while linha < Ntrain:
        diferença = X_train[linha][coluna] - lista_medias[coluna]
        soma_quadrado += diferença * diferença
        linha += 1
    var = soma_quadrado / Ntrain
    desvio = var ** (1/2)
    lista_desvios.append(desvio)
    coluna += 1

# normalização dos casos de treino
linha = 0
while linha < Ntrain:
    coluna = 0
    while coluna < num_carac:
        if lista_desvios[coluna] == 0:
            X_train[linha][coluna] = 0.0
        else:
            X_train[linha][coluna] = (X_train[linha][coluna] - lista_medias[coluna]) / lista_desvios[coluna]
        coluna += 1
    linha += 1

# normalização dos casos de teste
linha = 0
while linha < len(X_test):
    coluna = 0
    while coluna < num_carac:
        if lista_desvios[coluna] == 0:
            X_test[linha][coluna] = 0.0
        else:
            X_test[linha][coluna] = (X_test[linha][coluna] - lista_medias[coluna]) / lista_desvios[coluna]
        coluna += 1
    linha += 1

linha_teste = 0

#função para calcular a distancia euclideana 
def dist_euclid(a, b):
    soma = 0
    i = 0
    while i < num_carac:
        subtraçao = a[i] - b[i]
        soma += subtraçao * subtraçao
        i += 1
    raiz = soma ** (1/2)
    return raiz

# rotulos
while linha_teste < len(X_test):
    lista_dist = []
    num_treino = 0
    while num_treino < Ntrain:
        vetor_teste = list(X_test[linha_teste])
        vetor_treino = list(X_train[num_treino])
        dist = dist_euclid(vetor_teste, vetor_treino)
        lista_dist.append([dist, num_treino])
        num_treino += 1
    lista_dist.sort()
    votos_p = 0
    votos_e = 0
    k_atual = 0


    while k_atual < K:
        vizinho = lista_dist[k_atual]
        posiçao_vizinho = vizinho[1]
        classe = Y_train[posiçao_vizinho]
        if classe == 'p':
            votos_p += 1
        else:
            votos_e += 1
        k_atual += 1

    if votos_p > votos_e:
        print('p')
    else:
        print('e')
    linha_teste += 1
    
