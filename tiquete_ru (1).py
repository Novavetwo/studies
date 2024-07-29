# Feito por Paulo Guilherme Schnaufer
# Perguntas para Professor Doutor Malbarbo na segunda:
# Devo trocar forma_pagamento para tipo_pagamento e padronizar a função similar? Ou não?
#Tem a opção de transformar a função forma_pagamento e tipo_pagamento em apenas uma,
#através de Seleção.
#
# Perguntar o que fazer em relaçao aos exemplos extra-longos da função menu_usuarios(categoria: str).
#
# Perguntar se vale a pena continuar utilizando a função menu_usuarios ou se livrar dela para
#ter melhor entendimento visual do código.
#
# Perguntar se vale a pena dividir a função sem parâmetros registrar_venda() em mais funções
#sem parâmetros, para que se elimine a necessidade da indentação provocada pelos loops de while
#e ifs.
#
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

def main() -> None:
    '''
    Fornece uma interface amigável ao usuário e organiza as entradas do usuário,
    relacionando-as com as funções adequadas e integrando o programa como um todo.
    '''
    continuar = True
    while continuar:
        print('▷ Sistema ◁ Digite o número desejado, sem aspas')
        print('》 1 - Registrar uma venda')
        print('》 2 - Exibir o Relatório das vendas')
        print('》 0 - Sair')
        inicializacao_str: str = input('》 ')
        inicializacao: int = int(inicializacao_str)
    
        if inicializacao == 0:
            continuar = False
        elif inicializacao == 1:
            registrar_venda()
        elif inicializacao == 2:
            relatorio_vendas()
    print('Até logo!')

def registrar_venda() -> None:
    '''
    O registro de venda recebe o tipo de usuário, quantos tíquetes estão sendo comprados e
    a forma de pagamento. Em cada um desses recebimentos, mostra ao usuário as opções 
    disponíveis e, também, o que ele está escolhendo, para que possa corrigir, caso 
    necessário. Após, apresenta o valor total da venda e, após a confirmação do operador,
    fica disponível para registrar outra venda.
    '''
    menu_usuario()
    

    
    
        
    
    
    

def menu_usuario() -> bool:
    categoria = 'Usuário'
    print('Tipo de Usuário')
    print('》 1 - Aluno')
    print('》 2 - Docente')
    print('》 3 - Pessoas da Comunidade Externa')
    print('》 4 - Servidores Públicos com até 3 salários mínimos')
    print('》 5 - Servidores Públicos com mais de 3 salários mínimos')
    print('》 0 - Voltar para Tela Inicial')
    reescrever = True
    while reescrever:
        entrada_tipo_usuario_str = input('》 ')
        entrada_tipo_usuario = int(entrada_tipo_usuario_str)
        if entrada_tipo_usuario == 0:
            decisao = main()
            reescrever = False
        elif entrada_tipo_usuario != 0:
            print(feedback_usuario(entrada_tipo_usuario, categoria))
            print('Digite s para confirmar ou n para reescrever')
            entrada_confirmar = input('》 ')
            if entrada_confirmar == 's':
                reescrever = False
    return decisao

def menu_tiquete():
    voltar = True
    while voltar:
        categoria = 'Tíquetes'
        menu = opcoes_de_registro(categoria)
        for n in menu:
            print(n)
        reescrever = True
        while reescrever:
            q_de_tiquetes_str: str = input('》 ')
            q_de_tiquetes: int = int(q_de_tiquetes_str)
            if q_de_tiquetes == 0:
                registrar_venda()
                reescrever == False
                voltar = False
            print(feedback_usuario(q_de_tiquetes, categoria))
            print('Digite s para confirmar ou n para reescrever')
            entrada_confirmar = input('》 ')
            if entrada_confirmar == 's':
                reescrever = False

def menu_pagamento():
    categoria = 'Pagamento'
        menu = opcoes_de_registro(categoria)
        for n in menu:
            print(n)
        reescrever = True
        while reescrever:
            entrada_forma_pagamento_str: str = input('》 ')
            entrada_forma_pagamento: int = int(entrada_forma_pagamento_str)
            if entrada_forma_pagamento == 0:
                reescrever = False
            else:
                print(feedback_usuario(entrada_forma_pagamento, categoria))
                print('Digite s para confirmar ou n para reescrever')
                entrada_confirmar = input('》 ')
                if entrada_confirmar == 's':
                    reescrever = False
                    voltar = False

def resumo():
    categoria = 'Resumo'
    resumo = resumo_de_registro(entrada_tipo_usuario, q_de_tiquetes, entrada_forma_pagamento)
    for n in resumo:
        print(n)
    reescrever = True
    while reescrever:
        print('Digite s para registrar venda ou n para descartá-la')
        entrada_confirmar = input('》 ')
        if entrada_confirmar == 's':
            resetar = False

    
def relatorio_vendas():
    '''

    '''

def opcoes_de_registro(categoria: str) -> list[str]:
    '''
    Coloca as opcões de alguma etapa do registro de uma venda (tipo de usuário ou 
    quantidade de tíquetes ou forma de pagamento) em uma lista, de acordo com a categoria
    selecionada no momento.
    Exemplos:
    >>> opcoes_de_registro('Usuário')
    ['Tipo de Usuário', '》 1 - Aluno', '》 2 - Docente', '》 3 - Pessoas da Comunidade Externa', '》 4 - Servidores Públicos com até 3 salários mínimos', '》 5 - Servidores Públicos com mais de 3 salários mínimos', '》 0 - Voltar para Tela Inicial']
    >>> opcoes_de_registro('Tíquetes')
    ['Insira a quantidade de tíquetes', '》 0 - Voltar']
    >>> opcoes_de_registro('Pagamento')
    ['Forma de pagamento', '》 1 - Dinheiro', '》 2 - PIX', '》 3 - Cartão', '》 0 - Voltar']
    '''
    if categoria == 'Usuário':
        titulo = 'Tipo de Usuário'
        op_um = '》 1 - Aluno'
        op_dois = '》 2 - Docente'
        op_tres = '》 3 - Pessoas da Comunidade Externa'
        op_quatro = '》 4 - Servidores Públicos com até 3 salários mínimos'
        op_cinco = '》 5 - Servidores Públicos com mais de 3 salários mínimos'
        op_zero = '》 0 - Voltar para Tela Inicial'
        opcoes = [titulo, op_um, op_dois, op_tres, op_quatro, op_cinco, op_zero]
    elif categoria == 'Tíquetes':
        titulo = 'Insira a quantidade de tíquetes'
        op_zero = '》 0 - Voltar'
        opcoes = [titulo, op_zero]
    elif categoria == 'Pagamento':
        titulo = 'Forma de pagamento'
        op_um = '》 1 - Dinheiro'
        op_dois = '》 2 - PIX'
        op_tres = '》 3 - Cartão'
        op_zero = '》 0 - Voltar'
        opcoes = [titulo, op_um, op_dois, op_tres, op_zero]
    return opcoes

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
    em um loop sendo efetuado ou descontinuado.
    Exemplos:
    >>> continuar_ou_nao('S')
    True
    >>> continuar_ou_nao('n')
    False
    '''
    escolha_minuscula = escolha.lower()
    if escolha_minuscula == 's':
        continuar = True
    elif escolha_minuscula == 'n':
        continuar = False
    return continuar

def resumo_de_registro(entrada_tipo_usuario: int, q_de_tiquetes: int, entrada_forma_pagamento: int) -> list[str]:
    '''
    Monta uma lista com o resumo de uma venda. Este resumo contém o tipo de usuário, 
    a quantidade de tíquetes vendidos e a forma de pagamento utilizada. O processo é 
    feito através de operações de listas e funções externas.
    A quantidade de tíquetes deve ser positiva.
    Exemplos:
    >>> resumo_de_registro(1, 1, 1)
    ['Usuário: ALUNO', 'Tíquete: 1', 'Pagamento: DINHEIRO']
    >>> resumo_de_registro(3, 4, 2)
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
    Registro(Tipo_de_Usuario='ALUNO', Quantidade_de_Tiquetes=1, Forma_de_Pagamento='DINHEIRO')
    >>> monta_lista_de_registro(3, 4, 2)
    Registro(Tipo_de_Usuario='EXTERNO', Quantidade_de_Tiquetes=4, Forma_de_Pagamento='PIX')
    '''
    usuario = tipo_usuario(entrada_tipo_usuario - 1).name
    tiquetes = q_de_tiquetes
    pagamento = forma_pagamento(entrada_forma_pagamento - 1).name
    lst: Registro = Registro(usuario, tiquetes, pagamento)
    return lst

if __name__ == '__main__':
    main()
