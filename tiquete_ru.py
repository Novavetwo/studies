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
    SERVIDOR_TRES = auto()
    TRES_SERVIDOR = auto()

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
    usuarios: list[Usuario] = [Usuario.ALUNO, Usuario.DOCENTE, Usuario.EXTERNO, Usuario.SERVIDOR_TRES, Usuario.TRES_SERVIDOR]
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
    >>> feedback_usuario(1, 'Usuario')
    'Você selecionou 1 - ALUNO'
    >>> feedback_usuario(1, 'Pagamento')
    'Você selecionou 1 - DINHEIRO'
    >>> feedback_usuario(2, 'Tíquetes')
    'Você selecionou 2 - Tíquetes'
    >>> feedback_usuario(1, 'Tíquetes')
    'Você selecionou 1 - Tíquete'
    >>> feedback_usuario(0, 'Tíquetes')
    'Você selecinou 0 - Quantidade inválida para Tíquetes'
    '''
    if categoria == 'Usuario':
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

def registrar_venda() -> None:
    '''
    O registro de venda recebe o tipo de usuário, quantos tíquetes estão sendo comprados e
    a forma de pagamento. Após, apresenta o valor total da venda e, após a confirmação do operador,
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
    categoria = 'Usuario'
    print(feedback_usuario(entrada_tipo_usuario, categoria))

    print("Quantidade de tíquetes")
    q_de_tiquetes_str: str = input("》 ")
    categoria = 'Tíquetes'
    q_de_tíquetes: int = int(q_de_tiquetes_str)
    print('Forma de pagamento')
    print('》 1 - Dinheiro')
    print('》 2 - PIX')
    print('》 3 - Cartão')
    entrada_forma_pagamento_str: str = input('》 ')
    entrada_forma_pagamento: int = int(entrada_forma_pagamento_str)
    categoria = 'Pagamento'
    feedback_usuario(entrada_forma_pagamento, categoria)

    
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