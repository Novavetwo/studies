# Feito por Paulo Guilherme Schnaufer
from enum import Enum, auto
from dataclasses import dataclass

@dataclass
class Registro:
    '''
    Resume um registro de venda.
    '''
    Tipo_de_Usuario: str
    Quantidade_de_Tiquetes: int
    Forma_de_Pagamento: str

class Usuario(Enum):
    '''
    Categoriza as diferentes possibilidades de relação do usuário com a universidade.
    '''
    ALUNO = auto()
    DOCENTE = auto()
    EXTERNO = auto()
    SERVIDOR_MAIS_QUE_TRES = auto()
    SERVIDOR_MENOS_QUE_TRES = auto()

class Pagamento(Enum):
    '''
    Categoriza as formas de pagamento possíveis.
    '''
    DINHEIRO = auto()
    PIX = auto()
    CARTAO = auto()


def tipo_usuario(n: int) -> Usuario:
    '''
    Assimila um número correspondente a uma categoria de relação do usuário do programa com
    a universidade e a converte em um tipo de usuário manejável para o programador.
    Feito através de listas dos tipos de Usuário.
    Exemplos:
    >>> tipo_usuario(0)
    <Usuario.ALUNO: 1>
    '''
    usuarios: list[Usuario] = [Usuario.ALUNO, Usuario.DOCENTE, Usuario.EXTERNO, Usuario.SERVIDOR_MAIS_QUE_TRES, Usuario.SERVIDOR_MENOS_QUE_TRES]
    return usuarios[n]

def forma_pagamento(n: int) -> Pagamento:
    '''
    Assimila um número correspondente a uma categoria de forma de pagamento e a converte
    em um tipo de usuário manejável para o programador.
    Feito através de listas dos tipos de Pagamento.
    Exemplos:
    >>> forma_pagamento(0)
    <Pagamento.DINHEIRO: 1>
    '''
    pagamentos: list[Pagamento] = [Pagamento.DINHEIRO, Pagamento.PIX, Pagamento.CARTAO]
    return pagamentos[n]

def feedback_usuario(entrada: int, categoria: str) -> str:
    '''
    Retorna um feedback de qual número o usuário selecionou e o que ele representa. 
    Feito através de operações lógicas.
    Exemplos:
    >>> feedback_usuario(1, 'Usuário')
    'Você selecionou 1 - ALUNO'
    >>> feedback_usuario(1, 'Pagamento')
    'Você selecionou 1 - DINHEIRO'
    >>> feedback_usuario(2, 'Tíquetes')
    'Você selecionou 2 - Tíquetes'
    >>> feedback_usuario(1, 'Tíquetes')
    'Você selecionou 1 - Tíquete'
    >>> feedback_usuario(0, 'Tíquetes')
    'Você selecionou 0 - Quantidade inválida para Tíquetes'
    '''
    if categoria == 'Usuário':
        resposta = tipo_usuario(entrada - 1).name
    elif categoria == 'Tíquetes':
        if entrada > 1:
            resposta = 'Tíquetes'
        elif entrada == 1:
            resposta = 'Tíquete'
        else:
            resposta = 'Quantidade inválida para Tíquetes'
    elif categoria == 'Pagamento':
        resposta = forma_pagamento(entrada - 1).name
    frase = 'Você selecionou ' + str(entrada) + ' - ' + resposta
    return frase
def continuar_ou_nao(escolha: str) -> bool:
    '''
    Esta função permite ao usuário decidir se irá ou não continuar seu processo,
    ou se deseja colocar uma nova entrada à função input anterior. Isso é possível
    através de um input definido como resposta positiva ou negativa, o que resultará
    em um loop sendo efetuado ou descontinuado
    Exemplos:
    >>> continuar_ou_nao
    '''

def registrar_venda() -> None:
    '''
    O registro de venda recebe o tipo de usuário, quantos tíquetes estão sendo comprados e
    a forma de pagamento. Em cada um desses recebimentos, mostra ao usuário as opções 
    disponíveis e, também, o que ele está escolhendo, para que possa corrigir, caso 
    necessário. Após, apresenta o valor total da venda e, após a confirmação do operador,
    fica disponível para registrar outra venda.
    '''
    print('Tipo de Usuário')
    print('》 1 - Aluno')
    print('》 2 - Docente')
    print('》 3 - Pessoas da Comunidade Externa')
    print('》 4 - Servidores Públicos com até 3 salários mínimos')
    print('》 5 - Servidores Públicos com mais de 3 salários mínimos')
    entrada_tipo_usuario_str: str = input('》 ')
    entrada_tipo_usuario: int = int(entrada_tipo_usuario_str)
    categoria = 'Usuário'
    print(feedback_usuario(entrada_tipo_usuario, categoria))

    print("Quantidade de tíquetes")
    q_de_tiquetes_str: str = input("》 ")
    q_de_tiquetes: int = int(q_de_tiquetes_str)
    categoria = 'Tíquetes'
    print(feedback_usuario(q_de_tiquetes, categoria))

    print('Forma de pagamento')
    print('》 1 - Dinheiro')
    print('》 2 - PIX')
    print('》 3 - Cartão')
    entrada_forma_pagamento_str: str = input('》 ')
    entrada_forma_pagamento: int = int(entrada_forma_pagamento_str)
    categoria = 'Pagamento'
    print(feedback_usuario(entrada_forma_pagamento, categoria))
    
    resumo = resumo_de_registro(entrada_tipo_usuario, q_de_tiquetes, entrada_forma_pagamento)
    print(resumo[0])
    print(resumo[1])
    print(resumo[2])

def resumo_de_registro(entrada_tipo_usuario: int, q_de_tiquetes: int, entrada_forma_pagamento: int) -> list[str]:
    '''
    Monta uma lista com o resumo de uma venda. Este resumo contém o tipo de usuário, 
    a quantidade de tíquetes vendidos e a forma de pagamento utilizada. O processo é 
    feito através de operações de listas e funções externas.
    A quantidade de tíquetes deve ser positiva.
    Exemplos:
    >>> monta_lista_de_registro(1, 1, 1)
    ['Usuário: ALUNO', 'Tíquete: 1', 'Pagamento: DINHEIRO']
    >>> monta_lista_de_registro(3, 4, 2)
    ['Usuário: EXTERNO', 'Tíquetes: 4', 'Pagamento: PIX']
    '''
    primeira_linha = 'Usuário: ' + tipo_usuario(entrada_tipo_usuario - 1).name
    if q_de_tiquetes > 1:
        segunda_linha = 'Tíquetes: ' + str(q_de_tiquetes)
    elif q_de_tiquetes == 1:
        segunda_linha = 'Tíquete: ' + str(q_de_tiquetes)
    terceira_linha = 'Pagamento: ' + forma_pagamento(entrada_forma_pagamento - 1).name
    lst: list[str] = [primeira_linha, segunda_linha, terceira_linha]
    return lst

def monta_lista_de_registro(entrada_tipo_usuario: int, q_de_tiquetes: int, entrada_forma_pagamento: int) -> Registro:
    '''
    Monta uma lista com o resumo de uma venda. Este resumo contém o tipo de usuário, 
    a quantidade de tíquetes vendidos e a forma de pagamento utilizada. O processo é 
    feito através de operações de listas e funções externas.
    A quantidade de tíquetes deve ser positiva.
    Exemplos:
    >>> monta_lista_de_registro(1, 1, 1)
    ['Usuário: ALUNO', 'Tíquete: 1', 'Pagamento: DINHEIRO']
    >>> monta_lista_de_registro(3, 4, 2)
    ['Usuário: EXTERNO', 'Tíquetes: 4', 'Pagamento: PIX']
    '''
    usuario = tipo_usuario(entrada_tipo_usuario - 1).name
    tiquetes = q_de_tiquetes
    pagamento = forma_pagamento(entrada_forma_pagamento - 1).name
    lst: Registro = Registro(usuario, tiquetes, pagamento)
    return lst

def relatorio_vendas():
    '''

    '''

    return 0

def main() -> None:
    '''
    Fornece uma interface amigável ao usuário e organiza as entradas do usuário,
    relacionando-as com as funções adequadas e integrando o programa como um todo.
    '''
    print('▷ Sistema ◁ Digite o número desejado, sem aspas')
    print('》 1 - Registrar uma venda')
    print('》 2 - Exibir o Relatório das vendas')
    inicializacao_str: str = input('》 ')
    inicializacao: int = int(inicializacao_str)
    
    if inicializacao == 1:
        registrar_venda()
    elif inicializacao == 2:
        relatorio_vendas()

main()