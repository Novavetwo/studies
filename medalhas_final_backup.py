import sys

def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)

    if len(sys.argv) > 2:
        print('Muitos parâmetros. Informe apenas um nome de arquivo.')
        sys.exit(1)

    tabela = le_arquivo(sys.argv[1])
    
    quadro_medalhas(tabela)
    paises_um_genero(tabela)
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
# Criar funções que executem o seguinte:
# 0º - Fazer uma lista dos países. - FEITO
# 1º - Verificar se um determinado país está presente na lista, para auxiliar o *0º* - FEITO
# 2º - Fazer a troca de dois países da lista com passagem de parâmetro. - FEITO
# 3º - Fazer uma chamada recursiva ou com loop de passagem de parâmetro
#      para ordenar a lista de países pela sua quantidade de medalhas. - FEITO
# 4º - Fazer a soma das medalhas de um dado país e de uma dada categoria - FEITO
# 5º - Fazer a comparação entre dois países para executar o *3º* - FEITO
# 6º - Fazer uma identificação do índice que representa o país, na lista de países,
#      que possui a maior quantidade de medalhas, para auxiliar o *3º* - FEITO
# 7º - Fazer a ordenação de medalhas em uma lista, para auxiliar a função principal que produz o quadro e o *5º* - FEITO
# 8º - Fazer a formatação das linhas
def quadro_medalhas(tabela: list[list[str]]) -> None:
    '''
    Gerencia, integra e chama as funções para criar, calcular e exibir um 
    quadro de medalhas a partir de uma lista de strings.
    '''
    paises = categoria_paises(tabela, len(tabela) - 1, [])
    paises_ordenados = ordenar_paises_por_medalhas(tabela, paises, 0)

    print('País    Ouro    Prata   Bronze  Total   ')
    #             '45      2       98      145     ' 
    for pais in paises_ordenados:
        medalhas = lst_int_para_lst_str(ordena_medalhas(tabela, pais), [], 3)
        print(pais + '     ' + formata_linha(medalhas, '', 3))

def formata_linha(medalhas: list[str], linha: str, i: int) -> str:
    '''
    Calcula o espaçamento do quadro de medalhas para que as colunas estejam alinhadas e padronizadas.
    O espaçamento total disponível é de 26 unidades '                                ', sendo 6 para todas
    as categorias, além de 2 unidades entre cada uma delas.
    Requer que *linha* seja uma string vazia ''
    Requer que *i* seja 3 na primeira chamada.
    Exemplo:
    >>> formata_linha(['45', '2', '98', '145'], '', 3)
    '45      2       98      145     '
    '''
    if i >= 0:
        medalha = medalhas[3 - i]
        linha = medalha + (' ' * (8 - len(medalha))) + formata_linha(medalhas, linha, i - 1)
    return linha

def lst_int_para_lst_str(lst_int: list[int], lst_str: list[str], i: int) -> list[str]:
    '''
    Transforma uma lista de inteiros em uma lista de strings, através de recursividade.
    Requer que lst_str seja uma lista vazia [] na primeira chamada.
    Requer que *i* seja len(lst_int) - 1
    Exemplo:
    >>> lst_int_para_lst_str([45, 2, 98, 145], [], 3)
    ['45', '2', '98', '145']
    '''
    if i >= 0:
        n = lst_int[i]
        lst_str = lst_int_para_lst_str(lst_int, lst_str, i - 1)
        lst_str.append(str(n))
    return lst_str

def paises_um_genero(tabela: list[list[str]]) -> None:
    '''
    Gerencia, integra e chama as funções para criar, calcular e exibir uma
    lista de países que tiveram atletas de apenas um gênero premiados.
    '''
    paises = categoria_paises(tabela, len(tabela) - 1, [])
    paises_unico_genero = []
    for pais in paises:
        generos = categoria_generos_do_pais(tabela, len(tabela) - 1, [], pais)
        if len(generos) == 1:
            paises_unico_genero.append(pais)
    print('Estes países tiveram atletas de apenas um gênero premiados.')
    for pais in paises_unico_genero:
        print(pais + ' com o gênero ' + categoria_generos_do_pais(tabela, len(tabela) - 1, [], pais)[0])

def soma_medalhas(tabela: list[list[str]], categoria: str, pais: str, linha: int) -> int:
    '''
    Soma a quantidade de medalhas de uma determinada categoria a partir de uma tabela e
    de um código de categoria, através de recursividade.
    Requer que a entrada de linha seja len(tabela) - 1.
    Exemplo:
    >>> soma_medalhas([['','1','', '', 'BRA'], ['','1','', '', 'BRA']], '1', 'BRA', 1)
    2
    '''
    if linha < 0:
        soma = 0
    else:
        if tabela[linha][1] == categoria and tabela[linha][4] == pais:
            soma = 1 + soma_medalhas(tabela, categoria, pais, linha - 1)
        else:
            soma = 0 + soma_medalhas(tabela, categoria, pais, linha - 1)
    return soma

def ordena_medalhas(tabela: list[list[str]], pais: str) -> list[int]:
    '''
    Calcula e retorna a quantidade de medalhas de ouro, prata, bronze e o total para cada país.
    Exemplo:
    >>> ordena_medalhas([['','1','', '', 'BRA'], ['','2','', '', 'USA']], 'BRA')
    [1, 0, 0, 1]
    '''
    ouro = soma_medalhas(tabela, '1', pais, len(tabela) - 1)
    prata = soma_medalhas(tabela, '2', pais, len(tabela) - 1)
    bronze = soma_medalhas(tabela, '3', pais, len(tabela) - 1)
    total = ouro + prata + bronze
    medalhas = [ouro, prata, bronze, total]
    return medalhas

def ordenar_paises_por_medalhas(tabela: list[list[str]], paises: list[str], i: int) -> list[str]:
    '''
    Ordena os países de uma lista de acordo com a quantidade de medalhas de ouro que um país possui.
    Caso haja empate, então a ordem é definida pela quantidade de medalhas de prata que o mesmo possui,
    e assim subsequentemente.
    Exige que o índice *i* seja igual a zero na primeira chamada recursiva.
    Exemplo:
    >>> ordenar_paises_por_medalhas([['', '1', '', '', 'BRA'], ['','2', '', '', 'USA']], ['USA', 'BRA'], 0)
    ['BRA', 'USA']
    '''
    if i < len(paises) - 1:
        i_maximo = encontra_maximo(tabela, paises, i, i)
        troca_lugar(paises, i, i_maximo)
        paises = ordenar_paises_por_medalhas(tabela, paises, i + 1)
    return paises

def compara_medalhas(tabela: list[list[str]], pais1: str, pais2: str) -> bool:
    '''
    Compara as medalhas entre dois países. Retorna True se a quantidade de 
    medalhas de ouro do *pais1* for maior do que a do *pais2*. Caso a quantidade
    seja a mesma, prossegue-se a comparação para as medalhas de Prata e de Bronze.
    Caso a quantidade seja a mesma em todas as medalhas, retorna-se False.
    Exemplo:
    >>> compara_medalhas([['','1','','','BRA'], ['','2','','','USA']], 'BRA', 'USA')
    True
    '''
    medalhas1 = ordena_medalhas(tabela, pais1)
    medalhas2 = ordena_medalhas(tabela, pais2)
    resposta = False
    if medalhas1[0] != medalhas2[0]:
        resposta = medalhas1[0] > medalhas2[0]
    elif medalhas1[1] != medalhas2[1]:
        resposta = medalhas1[1] > medalhas2[1]
    elif medalhas1[2] != medalhas2[2]:
        resposta = medalhas1[2] > medalhas2[2]
    return resposta

def encontra_maximo(tabela: list[list[str]], paises: list[str], i: int, i_maximo: int) -> int:
   '''
   Encontra o índice do maior valor de uma lista. O maior valor de uma lista é definido pela sua
   quantidade de medalhas de ouro, prata e bronze.
   Exemplo:
   >>> encontra_maximo([['','1','','','BRA'],['','2','','','USA']], ['BRA','USA'], 0, 0)
   0
   '''
   for j in range(i, len(paises)):
       if compara_medalhas(tabela, paises[j], paises[i_maximo]):
           i_maximo = j
   return i_maximo

#def encontra_maximo(tabela: list[list[str]], paises: list[str], i: int, i_maximo: int) -> int:
#    '''
#    Encontra o índice do maior valor de uma lista. O maior valor de uma lista é definido pela sua
#    quantidade de medalhas de ouro, prata e bronze. Exige que i seja igual a zero na primeira chamada.
#    O caso base é retornar o valor máximo *i_maximo* já estabelecido, quando *i* ultrapassar a 
#    quantidade de elementos da lista len(paises).
#    Exemplo:
#    >>> encontra_maximo([['','1','','','BRA'],['','3','','','USA']], [], 0, 0)
#    0
#    
#    if i < len(paises):
#        if compara_medalhas(tabela, paises[i], paises[i_maximo]):
#            i_maximo = i
#        i_maximo = encontra_maximo(tabela, paises, i + 1, i_maximo)
#    return i_maximo

def troca_lugar(lst: list[str], i: int, j: int) -> list[str]:
    '''
    Troca dois elementos nos índices i e j em uma lista entre si.
    Exemplos:
    >>> troca_lugar(['BRA', 'USA'], 0, 1)
    ['USA', 'BRA']
    >>> troca_lugar(['BRA', 'USA'], 0, 0)
    ['BRA', 'USA']
    '''
    elemento = lst[i]
    lst[i] = lst[j]
    lst[j] = elemento
    return lst

def categoria_generos_do_pais(tabela: list[list[str]], linha: int, generos: list[str], pais: str) -> list[str]:
    '''
    Monta uma lista de elementos de acordo com a lista *tabela* dada, utilizando recursividade.
    Se a linha verificada representa um elemento que já está na lista, esse elemento é ignorado.
    Requer que linha seja len(tabela) - 1 e que *generos* seja uma lista vazia [] na primeira chamada.
    Exemplo:
    >>> categoria_generos_do_pais([['','','','','BRA','M'],['','','','','USA','W']], 1, [], 'BRA')
    ['M']
    '''
    if linha >= 0:
        genero = tabela[linha][5]
        if verificar_presenca(generos, genero) == False:
            generos = categoria_generos_do_pais(tabela, linha - 1, generos, pais)
            if tabela[linha][4] == pais:
                generos.append(genero)
    return generos

def categoria_paises(tabela: list[list[str]], linha: int, paises: list[str]) -> list[str]:
    '''
    Monta uma lista de elementos de acordo com a lista *tabela* dada, utilizando recursividade.
    Se a linha verificada representa um elemento que já está na lista, esse elemento é ignorado.
    Requer que linha seja len(tabela) - 1 e que paises seja uma lista vazia [] na primeira chamada. 
    Exemplo:
    >>> categoria_paises([['','1','','', 'BRA'], ['','2','','', 'USA']], 1, [])
    ['USA', 'BRA']
    >>> categoria_paises([['','1','','','BRA'],['','2','','','BRA']], 1, [])
    ['BRA']
    '''
    if linha >= 0:
        pais = tabela[linha][4]
        if verificar_presenca(paises, pais) == False:
            paises.append(pais)
            paises = categoria_paises(tabela, linha - 1, paises)
        else:
            paises = categoria_paises(tabela, linha - 1, paises)
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
    resposta = False
    while i < len(lst):
        if lst[i] == elemento:
            resposta = True
        i = i + 1
    return resposta
#print(categoria_paises([['','1','', '', 'BRA'], ['','2','', '', 'USA'], ['','1','', '', 'BRA'], ['','1','', '', 'BRA']], 3, []))
#quadro_medalhas([['','3','', '', 'BRA'], ['','1','', '', 'USA'], ['','2','', '', 'BRA'], ['','2','', '', 'BRA']])
if __name__ == '__main__':
    main()

