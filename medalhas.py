import sys

def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)

    if len(sys.argv) > 2:
        print('Muitos parâmetros. Informe apenas um nome de arquivo.')
        sys.exit(1)

    tabela = le_arquivo(sys.argv[1])

    # TODO: computar e exibir o quadro de medalhas
    # TODO: computar e exibir os países que tiverem apenas
    #       atletas de um único gênero premiados


def le_arquivo(nome: str) -> list[list[str]]:
    '''
    Lê o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento é
    uma lista com os valores das colunas de uma linha (valores separados por
    vírgula). A primeira linha do arquivo, que deve conter o nome das
    colunas, é descartado.

    Por exemplo, se o conteúdo do arquivo for

    tipo,cor,ano
    carro,verde,2010
    moto,branca,1995

    a resposta produzida é
    [['carro', 'verde', '2010'], ['moto', 'branca', '1995']]
    '''
    try:
        with open(nome) as f:
            tabela = []
            linhas = f.readlines()
            for i in range(1, len(linhas)):
                tabela.append(linhas[i].split(','))
            return tabela
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.');
        sys.exit(1)

def quadro_medalhas(tabela: list[list[str]]) -> list[list[str]]:
    '''
    Exibe um quadro de medalhas a partir de uma lista de strings denominada tabela.
    Descarta todas as informações irrelevantes ao quadro de medalhas, ou seja, toda informação
    que não tenha algo a ver com o tipo de medalha e o país que a obteve.
    '''
    print('País  Ouro  Prata  Bronze  Total')
    for pais in ranque(tabela):
        print(pais + '  ' + ordena_medalhas(tabela, pais))

    quadro = []
    for linha in tabela:
        pais = linha[4]
        medalha = int(linha[1])
        if verificar_presenca(quadro, pais) == False:
            
    return None

def soma_medalhas(tabela: list[list[str]], categoria: str, pais: str, linha: int) -> int:
    '''
    Soma a quantidade de medalhas de uma determinada categoria a partir de uma tabela e
    de um código de categoria, através de recursividade.
    Requer que a entrada de linha seja len(tabela) - 1.
    '''
    if linha < 0:
        soma = 0
    else:
        if tabela[linha][1] == categoria and tabela[linha][4] == pais:
            soma = 1 + soma_medalhas(tabela, categoria, pais, linha - 1)
        else:
            soma = 0 + soma_medalhas(tabela, categoria, pais, linha - 1)
    return soma

def ordena_medalhas(tabela: list[list[str]]) -> list[int]:
    '''
    Calcula e retorna a quantidade de medalhas de ouro, prata, bronze e o total para cada país.
    '''
    ouro = soma_medalhas(tabela, '1', pais, len(tabela) - 1)
    prata = soma_medalhas(tabela, '2', pais, len(tabela) - 1)
    bronze = soma_medalhas(tabela, '3', pais, len(tabela) - 1)
    total = ouro + prata + bronze
    return [ouro, prata, bronze, total]


def separa_categoria(tabela: list[list[str]]) -> list[str]:
    '''
    '''
def ranque(tabela: list[list[str]], i: int) -> list[str]:
    '''
    Ordena os países de uma lista de acordo com a quantidade de medalhas de ouro que um país possui.
    Caso haja empate, então a ordem é definida pela quantidade de medalhas de prata que o mesmo possui,
    e assim subsequentemente.
    Exige que i seja um número maior que ou igual a zero.
    '''
    medalha = tabela[1]
    paises = categoria_paises(tabela, len(tabela) - 1, [])
    for i in range(len(paises)):
        for j in range(len(paises) - 1):
            if compara_medalhas(tabela, paises[j], paises[j + 1]) < 0:
                troca_lugar(paises, j, j + 1)
    return paises



    if soma_medalhas(tabela, '1', paises[i], len(tabela) - 1) < \
        soma_medalhas(tabela, '1', paises[i + 1], len(tabela) - 1):
        troca_lugar(paises, i, i + 1)
    elif soma_medalhas(tabela, '2', paises[i], len(tabela) - 1) < \
        soma_medalhas(tabela, '2', paises[i + 1], len(tabela) - 1):
        troca_lugar(paises, i, i + 1)
    
def ordena_selecao(lst: list[int]):
    '''
    Ordena os valores de *lst* em ordem não decrescente.

    Exemplos
    >>> lst = [8, 5, 4, 1, 2]
    >>> ordena_selecao(lst)
    >>> lst
    [1, 2, 4, 5, 8]
    '''
    # A sublista lst[:i] está ordenada
    for i in range(len(lst) - 1):
        # Índice do elemento mínimo de lst[i:]
        jmin = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[jmin]:
                jmin = j

        # Troca lst[i] <-> lst[jmin]
        t = lst[i]
        lst[i] = lst[jmin]
        lst[jmin] = t
        
def troca_lugar(lst: list[str], i: int, j: int) -> list[str]:
    '''
    Troca dois elementos nos índices i e j em uma lista entre si.
    '''
    elemento = lst[i]
    lst[i] = lst[j]
    lst[j] = elemento
    return lst

def categoria_paises(tabela: list[list[str]], linha: int, paises: list[str]) -> list[str]:
    '''
    Monta uma lista de elementos de acordo com a lista *tabela* dada, utilizando recursividade.
    Se a linha verificada representa um elemento que já está na lista, esse elemento é ignorado.
    Requer que linha seja len(tabela) - 1 e que paises seja uma lista vazia [] na primeira chamada.   
    '''
    if linha >= 0:
        pais = tabela[linha][4]
        if verificar_presenca(paises, pais) == False:
            paises = categoria_paises(tabela, linha - 1, paises)
            paises.append(pais)
    return paises
    

def verificar_presenca(lst: list[str], elemento: str):
    '''
    Verifica se dado elemento está presente em determinada lista.
    Exemplo:
    >>> verificar_presenca(['1'], '1')
    True
    >>> verificar_presenca(['1'], '2')
    False
    '''
    i = 0
    while i < len(lista):
        if lista[i] == elemento:
            resposta = True
        i = i + 1
    resposta = False
    return resposta

def remove_indice(lst: list[int], i: int):
    '''
    Remove o elemento do índice *i* de *lst* movendo
    os elementos das posições i + 1, i + 2, ..., len(lst)
    para as posições i, i + 1, ..., len(lst) - 1.

    Requer que 0 <= i < len(lst).

    Exemplos
    >>> lst = [7, 1, 8, 9]
    >>> remove_indice(lst, 2)
    >>> lst
    [7, 1, 9]
    >>> remove_indice(lst, 0)
    >>> lst
    [1, 9]
    >>> remove_indice(lst, 1)
    >>> lst
    [1]
    >>> remove_indice(lst, 0)
    >>> lst
    []
    '''
    assert 0 <= i < len(lst)
    while i < len(lst) - 1:
        lst[i] = lst[i + 1]
        i = i + 1
    

if __name__ == '__main__':
    main()