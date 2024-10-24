def calcular_valores_geral(x_final):
    ultimov = 1.12
    dif1 = 0.16
    constante = 0.04  

    dif_5 = dif1 - constante  # 0.16 - 0.04 = 0.12
    p2_05 = ultimov - dif_5   # 1.12 - 0.12 = 1.00

    dif_6 = dif_5 - constante  # 0.12 - 0.04 = 0.08
    p2_06 = p2_05 - dif_6      # 1.00 - 0.08 = 0.92

    resultados = {}

    # p/ Valor  >= a 0.5
    if x_final >= 0.5:
        p2_atual = p2_06
        dif1_atual = dif_6
        x_atual = 0.6
        
       
        while x_atual < x_final:
            dif_5 = dif1_atual - constante  
            p2_atual = p2_atual - dif_5   
                   
            dif1_atual =dif_5                   # Atualiza o dif1 para o próximo 
            x_atual += 0.1                           
            resultados[x_atual] = p2_atual          # ARmz

    # P/ valor < 0.5
    else:
        p2_atual = p2_05
        dif1_atual = novo_dif1
        x_atual = 0.5
        
        while x_atual > x_final:
            novo_dif1 = dif1_atual + constante  
            p2_atual = p2_atual + novo_dif1      

            dif1_atual = novo_dif1                  
            x_atual -= 0.1                          
            resultados[x_atual] = p2_atual          
            
    resultados[0.5] = p2_05 
    resultados[0.6] = p2_06 

    # Print baixo
    eixo_x = sorted(resultados.keys())
    eixo_y = [round(resultados[x], 2) for x in eixo_x]

    print(f"\nValores de x: {eixo_x}")
    print(f"Valores de y: {eixo_y}")

    return eixo_x, eixo_y 

def babbage(eixo_y):
    n = len(eixo_y)
    tabela = [eixo_y]
    for i in range(n - 1):  # Itera sobre o número de níveis de diferença
        linha = []
        for j in range(n - i - 1):
            v = tabela[i][j + 1] - tabela[i][j]
            linha.append(v) # Adiciona a diferença L
        tabela.append(linha)  # T
    return tabela

# Vvalores de x grau
def polinomio(x, coeficientes, grau):
    soma = 0
    i = 0
    while i <= grau:
        soma += coeficientes[i] * (x ** (grau - i))
        i += 1
    return soma


x_final = float(input("Insira o valor de x que deseja calcular: "))
valores_x, valores_y = calcular_valores_geral(x_final)

# proximo v de x
resultado_final = valores_y[-1] if valores_y else None
if resultado_final is not None:
    print(f"O proximo valor da sequencia  ({x_final + 0.1 }) é {resultado_final:.2f}")


grau = int(input("Insira o grau do polinômio: "))
coeficientes = []
for i in range(grau + 1):
    coeficiente = float(input(f"Insira o coeficiente do termo de grau {grau - i}: "))
    coeficientes.append(coeficiente)

# lista  polinômio
eixo_x = list(range(10))  # de 0 a 9
eixo_y = [polinomio(x, coeficientes, grau) for x in eixo_x]


diffs_poly = babbage(eixo_y)


print(f"\nValores de x para o polinômio: {eixo_x}")
print(f"Valores de y para o polinômio: {eixo_y}")

print("\nTabela de diferenças do polinômio:")
for c, linha in enumerate(diffs_poly):
    print(f"Nível {c}: {linha}")


