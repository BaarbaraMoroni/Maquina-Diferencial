def calcular_valores_geral(x_final):
    
    ultimov = 1.12
    dif1 = 0.16
    constante = 0.04  

   
    dif_5 = dif1 - constante  # 0.16 - 0.04 = 0.12
    p2_05 = ultimov - dif_5         # 1.12 - 0.12 = 1.00
   
    dif_6= dif_5 - constante  # 0.12 - 0.04 = 0.08
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
            resultados[x_atual] = p2_atual          # Armazena 

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

   
    for x, p2_valor in sorted(resultados.items()): #ret a lista
        print(f"O valor de p2({x:.1f}) é {p2_valor:.2f}")

    return p2_atual

x_final = float(input("Insira o valor de x que deseja calcular : "))
resultado_final = calcular_valores_geral(x_final)
print(f"O valor de p2({x_final:.1f}) é {resultado_final:.2f}")


def babbage(eixo_y):
    n = len(eixo_y)
    tabela = [eixo_y]
    for i in range(n - 1):  # Itera sobre o número de níveis de diferença
        linha = []
        for j in range(n - i - 1):
            v = tabela[i][j + 1] - tabela[i][j]
            linha.append(v) # Adiciona a diferença L
        tabela.append(linha) #T
    return tabela

# próximo valor com base TD
def calcular_proximo_valor(tabela_diferencas):
    prox_valor = tabela_diferencas[0][-1]
    for i in range(1, len(tabela_diferencas)):
        prox_valor += tabela_diferencas[i][-1]
    return prox_valor

# Vvalores de um polinômio de x grau
def polinomio(x, coeficientes, grau):
    soma = 0
    i = 0
    while i <= grau:
        soma += coeficientes[i] * (x ** (grau - i))
        i += 1
    return soma


grau = int(input("Insira o grau do polinômio: "))


coeficientes = []
for i in range(grau + 1):
    coeficiente = float(input(f"Insira o coeficiente do termo de grau {grau - i}: "))
    coeficientes.append(coeficiente)

# Cria a lista de valores de x  y 
eixo_x = list(range(10))  # de 0 a 9
eixo_y = [polinomio(x, coeficientes, grau) for x in eixo_x]

# Calcula a tabela de diferenças
diffs = babbage(eixo_y)


print(f"\nValores de x: {eixo_x}")
print(f"Valores de y: {eixo_y}")
print("\nTabela de diferenças:")
for c, linha in enumerate(diffs):
    print(f"Nível {c}: {linha}")


proximo_valor = calcular_proximo_valor(diffs)
print(f"\nO próximo valor na sequência é: {proximo_valor}")
