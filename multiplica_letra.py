n = int(input())
contagem = 0
alg = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

while contagem < n:
    contagem += 1
    string = input()
    resultado_linha = ""
    primeiro_carac = ""
    multiplicador = ""
    
    for i in string:
        if i not in alg: 
            if primeiro_carac != "":
                resultado_linha += primeiro_carac * int(multiplicador)
                
            primeiro_carac = i
            multiplicador = ""
            
        else:
            multiplicador += i
            
    if primeiro_carac != "":
        resultado_linha += primeiro_carac * int(multiplicador)
        
    print(resultado_linha)