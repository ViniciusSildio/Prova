import random

class Dados_Entradas():
    def __init__(self, valor, pesos, valor_ideal):
        self.valor = int(valor)
        self.pesos = dict(pesos)


def somatorio(dados_entradas, peso):
    # Faz a soma entre os valores e os pesos
    print(f'Peso do Somatório selecionado = {peso}')
    constante = 0
    valor_somatorio = 0
    for e in dados_entradas:
        valor_somatorio += e['valor'] * e['pesos'][peso]
    return round(valor_somatorio + constante, 2)

def custo(valor_obitido, valor_ideal):
    # Faz o cálculo entre o valor obtido e o ideal
    return round(((valor_obitido - valor_ideal) ** 2), 2)

def gerar_pesos(qtd_pesos):
    # Gera pesos aleatórios
    pesos = {}
    for n_peso in range(qtd_pesos):
        pesos[f'w{n_peso}'] = round(random.random(), 2)
    return pesos

def gerar_lista_entradas(qtd_entradas, qtd_pesos_por_entradas):
    # Gera a lista de entradas com valores aleatórios
    dados_entradas = []
    for n_dados_entradas in range(qtd_entradas):
        vars()[f'e{str(n_dados_entradas)}'] = {
            "nome": f'Entrada {str(n_dados_entradas)}',
            "valor": round(random.random(), 2),
            "pesos": gerar_pesos(qtd_pesos_por_entradas)
        }
        dados_entradas.append(vars()[f'e{str(n_dados_entradas)}'])
    return dados_entradas

def chamada_peso_randomico(entrada):
    # Chama um número de entrada aleatório
    return f'w{str(random.randint(0, len(entrada["pesos"]) - 1))}'

def chamada_peso_randomico(valor):
    # Chama um valor aleatório
    return f'w{str(random.randint(0, int(valor) - 1))}'

def print_lista_entradas(dados_entradas):
    # Exibe a lista de entradas e de pesos calculada
    for item in dados_entradas:
        print(f'{item["nome"]}: valor = {item["valor"]}, pesos = {item["pesos"]} ')
    print('\n')

def print_lista_entradas_bruta(dados_entradas):
    # Exibe a lista com os numeros de entradas e dos pesos de forma bruta
    for item in dados_entradas:
        print(item)
    print("\n")

def run():
    # Quantidade dos números de entradas e dos pesos
    qtd_entradas = 10
    qtd_pesos = 10

    print('\n=-=-=-=-=-=-=-= Comeco =-=-=-=-=-=-=-=\n')
    print(f'Quantidade de entradas: {qtd_entradas}\nQuantidade de pesos por entrada: {qtd_pesos}\n')

    dados_entradas = gerar_lista_entradas(qtd_entradas, qtd_pesos)
    saidas = gerar_lista_entradas(qtd_entradas, qtd_pesos)
    print(f'\n')
    print(f'Lista aleatótia 1:\n')
    print_lista_entradas(dados_entradas)
    print(f'Lista aleatória 2:')
    print_lista_entradas(saidas)

    print(f'\n')

    somatorios = somatorio(dados_entradas, chamada_peso_randomico(qtd_pesos))
    soma = somatorio(saidas, chamada_peso_randomico(qtd_pesos))

    print(f'Valor da Função de Ativação 1 chamada: {somatorios}')
    print(f'Valor da função de Ativação 2 chamada: {soma}\n')

    custos = custo(somatorios, 1)
    gasto = custo(soma, 1)
    ideal = custos - gasto

    print(f'Valor ideal: 3.95\n')
    print(f'Valor da Função de Custo 1 chamada: {custos}')
    print(f'Valor da Função de Custo 2 chamada: {gasto}\n')

    if ideal < 3.95:
        print(f'Valor encontrado é abaixo do ideal: {ideal}')
    elif ideal > 3.93:
        print(f'Valor encontrado é acima do ideal: {ideal}')    
    else:
        print(f'Valor ideal foi atingido: {ideal}')

    print('\n=-=-=-=-=-=-=-=- Fim -=-=-=-=-=-=-=-=\n')

if __name__ == '__main__':
    run()
