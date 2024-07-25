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
    Recebe um número correspondente a uma categoria de relação do usuário do programa com
    a universidade e a converte em um tipo de usuário manejável para o programador.
    Exemplos:
    >>> tipo_usuario(0)
    <Usuario.ALUNO: 1>
    '''
    usuarios: list[Usuario] = [Usuario.ALUNO, Usuario.DOCENTE, Usuario.EXTERNO, Usuario.SERVIDOR_TRES, Usuario.TRES_SERVIDOR]
    return usuarios[n]

def forma_pagamento(n: int) -> Pagamento:
    '''
    Recebe um número correspondente a uma forma de pagamento e a converte em
    um tipo de usuário manejável para o programador.
    Exemplos:
    >>> forma_pagamento(0)
    <Pagamento.DINHEIRO: 1>
    '''
    pagamentos: list[Pagamento] = [Pagamento.DINHEIRO, Pagamento.PIX, Pagamento.CARTAO]
    return pagamentos[n]

def feedback_usuario(entrada: int, categoria: str) -> str:
    '''
    Retorna um feedback de qual número o usuário selecionou e o que ele representa.
    Exemplos:
    >>> feedback_usuario(1, 'Usuario')
    'Você selecionou 1 - ALUNO'
    >>> feedback_usuario(1, 'Pagamento')
    'Você selecionou 1 - DINHEIRO'
    '''
    if categoria == 'Usuario':
        operacao = tipo_usuario(entrada)
    elif categoria == 'Pagamento':
        operacao = forma_pagamento(entrada)
    frase = 'Você selecionou ' + str(entrada) + ' - ' + (operacao).name
    return frase

def registrar_venda():
    '''
    O registro de venda recebe o tipo de usuário, quantos tíquetes estão sendo comprados e
    a forma de pagamento. Após, apresenta o valor total da venda e, após a confirmação do operador,
    fica disponível para registrar outra venda.
    '''
    entrada_tipo_usuario: int = input("Tipo de Usuário \n\
                                  》 1 - Aluno\n\
                                  》 2 - Docente\n\
                                  》 3 - Pessoas da Comunidade Externa\n\
                                  》 4 - Servidores Públicos com até 3 salários mínimos\n\
                                  》 5 - Servidores Públicos com mais de 3 salários mínimos\n\
                                  》 ")
    categoria = 'Usuario'
    feedback_usuario(entrada_tipo_usuario, categoria)

    q_de_tiquetes: int = input("Quantidade de tíquetes\n\
                               》 ")

    entrada_forma_pagamento: Pagamento = input("Forma de pagamento \n\
                                       》 1 - Dinheiro\n\
                                       》 2 - PIX\n\
                                       》 3 - Cartão\n\
                                       》 ")
    categoria = 'Pagamento'
    feedback_usuario(entrada_forma_pagamento, categoria)

    return 0.0
def relatorio_vendas():
    '''
    
    
    '''

    return 0

def main():
    '''
    Fornece uma interface amigável ao usuário e organiza as entradas do usuário,
    relacionando-as com as funções adequadas e integrando o programa como um todo.
    '''
    inicializacao = input("▷ Sistema ◁ Digite o número desejado, sem aspas:\n\
                          》 1 - Registrar uma venda\n\
                          》 2 - Exibir o Relatório das vendas\n\
                          》 ")
    
    if inicializacao == 1:
        registrar_venda()
    elif inicializacao == 2:
        relatorio_vendas()


    return 0
main()