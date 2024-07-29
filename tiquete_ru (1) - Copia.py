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
# Como fazer o teste do loop de confirmação?
#
'''
O programa apresenta um menu que pode ser escolhido para ir a duas seções - a de registro de vendas e
a de relatório de vendas. A seção de registro de vendas permite ao usuário registrar uma venda com três
informações: tipo de usuário, quantidade de tíquetes e forma de pagamento. Esse resumo será armazenado em 
uma lista e poderá ser verificado na seção de relatório de vendas, onde haverá um total de dinheiro feito 
e também gráficos mostrando as porcentagens que cada categoria de informação compartilha de todas as vendas.
'''
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
    relacionando-as com as funções adequadas, inicializando e integrando o programa como um todo.
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
        else:
            print('Entrada inválida, tente novamente')
    print('Até logo!')

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
    usuario = loop_de_confirmacao('Usuário')

    print('Insira a quantidade de tíquetes')
    tiquetes = loop_de_confirmacao('Tíquetes')
    
    print('Forma de pagamento')
    print('》 1 - Dinheiro')
    print('》 2 - PIX')
    print('》 3 - Cartão')
    pagamento = loop_de_confirmacao('Pagamento')
   
    resumo: list[str] = resume_registro(usuario, tiquetes, pagamento)
    for opcao in resumo:
        print(opcao)

    lst_registro: Registro = monta_registro(usuario, tiquetes, pagamento)
    total = str(total_da_venda(lst_registro))
    print('Total:  ' + total + ' reais')


    print('Digite s para registrar venda ou n para descartá-la')
    entrada_confirmar = input('》 ').lower()
    if entrada_confirmar == 's':
        guarda_vendas(lst_registro)
        print('Venda registrada')
        print('Pressione Enter para registrar outra venda ou pressione Espaço + Enter para voltar à Tela Inicial')
        entrada_decisao = input('》 ')
        if entrada_decisao == '':
            registrar_venda()
        elif entrada_decisao == ' ':
            main()
    elif entrada_confirmar == 'n':
        main()

def total_da_venda(lst_registro: Registro) -> int:
    '''
    Converte um Registro em um valor correspondente ao total da compra através de operações
    matemáticas.
    Exemplos:
    >>> total_da_venda(Registro(Tipo_de_Usuario='ALUNO', Quantidade_de_Tiquetes=1, Forma_de_Pagamento='DINHEIRO'))
    5
    >>> total_da_venda(Registro(Tipo_de_Usuario='DOCENTE', Quantidade_de_Tiquetes=3, Forma_de_Pagamento='CARTAO'))
    30
    >>> total_da_venda(Registro(Tipo_de_Usuario='EXTERNO', Quantidade_de_Tiquetes=2, Forma_de_Pagamento='PIX'))
    38
    '''
    usuario = lst_registro.Tipo_de_Usuario
    tiquete = lst_registro.Quantidade_de_Tiquetes # para programador entender, utiliza-se classe Registro
    if usuario == 'ALUNO' or usuario == 'SERVIDOR_MENOS_QUE_TRES':
        valor_tiquete = 5
    elif usuario == 'DOCENTE' or usuario == 'SERVIDOR_MAIS_QUE_TRES':
        valor_tiquete = 10
    elif usuario == 'EXTERNO':
        valor_tiquete = 19
    valor_da_venda = tiquete * valor_tiquete
    return valor_da_venda

def guarda_vendas(lst_registro: Registro) -> None:
    '''
    Guarda a lista de resumo da venda em uma lista de resumos de venda para 
    ser utilizada como parâmetro da função exibir relatório.
    '''
    

def loop_de_confirmacao(categoria: str) -> int:
    '''
    Fornece um loop genérico por while {condição} para quaisquer menus que 
    necessitem de confirmação do usuário. Indica qual foi a opção escolhida pelo usuário
    através de funções externas e retorna um inteiro que representa qual opção do menu foi escolhida.
    Exemplo: 
    >>> loop_de_confirmacao('Usuário')
    》 Você selecionou 1 - ALUNO
    Pressione Enter para confirmar ou Espaço + Enter para digitar novamente
    》 》 Você selecionou 1 - ALUNO
    Pressione Enter para confirmar ou Espaço + Enter para digitar novamente
    》 1
    '''
    reescrever = True
    while reescrever:
        if categoria == 'Usuário':
            entrada_usuario_str = input('》 ')
            if entrada_usuario_str == '1' or entrada_usuario_str == '2' or entrada_usuario_str == '3'\
                  or entrada_usuario_str == '4' or entrada_usuario_str == '5':
                entrada_usuario = int(entrada_usuario_str)
                print(feedback_entrada(entrada_usuario, categoria))
                print('Pressione Enter para confirmar ou Espaço + Enter para digitar novamente')
                entrada_confirmar = input('》 ')
                if entrada_confirmar == '':
                    reescrever = False
                    opcao_escolhida = entrada_usuario
            else:
                print('Entrada inválida, por favor, tente novamente!')
        elif categoria == 'Tíquetes':
            entrada_usuario_str = input('》 ')
            if int(entrada_usuario_str) > 0:
                entrada_usuario_str = input('》 ')
                entrada_usuario = int(entrada_usuario_str)
                print(feedback_entrada(entrada_usuario, categoria))
                print('Pressione Enter para confirmar ou Espaço + Enter para digitar novamente')
                entrada_confirmar = input('》 ')
                if entrada_confirmar == '':
                    reescrever = False
                    opcao_escolhida = entrada_usuario
            else:
                print('Entrada inválida, por favor, tente novamente!')
        elif categoria == 'Pagamento':
            entrada_usuario_str = input('》 ')
            if entrada_usuario_str == '1' or entrada_usuario_str == '2' or entrada_usuario_str == '3':
                entrada_usuario_str = input('》 ')
                entrada_usuario = int(entrada_usuario_str)
                print(feedback_entrada(entrada_usuario, categoria))
                print('Pressione Enter para confirmar ou Espaço + Enter para digitar novamente')
                entrada_confirmar = input('》 ')
                if entrada_confirmar == '':
                    reescrever = False
                    opcao_escolhida = entrada_usuario
            else:
                print('Entrada inválida, por favor, tente novamente!')
    return opcao_escolhida
    
def relatorio_vendas():
    return 0

def exibir_grafico():
    return 0

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

def feedback_entrada(entrada: int, categoria: str) -> str:
    '''
    Retorna um feedback da entrada de qual número o usuário 
    selecionou e o que ele representa. Feito através de operações lógicas.
    Exemplos:
    >>> feedback_entrada(1, 'Usuário')
    'Você selecionou 1 - ALUNO'
    >>> feedback_entrada(1, 'Pagamento')
    'Você selecionou 1 - DINHEIRO'
    >>> feedback_entrada(2, 'Tíquetes')
    'Você selecionou 2 - Tíquetes'
    >>> feedback_entrada(1, 'Tíquetes')
    'Você selecionou 1 - Tíquete'
    >>> feedback_entrada(0, 'Tíquetes')
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

def resume_registro(usuario: int, tiquetes: int, pagamento: int) -> list[str]:
    '''
    Monta uma lista com o resumo de uma venda. Este resumo contém o tipo de usuário, 
    a quantidade de tíquetes vendidos e a forma de pagamento utilizada. O processo é 
    feito através de operações de listas e funções externas.
    A quantidade de tíquetes deve ser positiva.
    Exemplos:
    >>> resume_registro(1, 1, 1)
    ['Usuário: ALUNO', 'Tíquete: 1', 'Pagamento: DINHEIRO']
    >>> resume_registro(3, 4, 2)
    ['Usuário: EXTERNO', 'Tíquetes: 4', 'Pagamento: PIX']
    '''
    primeira_linha = 'Usuário: ' + tipo_usuario(usuario - 1).name
    if tiquetes > 1:
        segunda_linha = 'Tíquetes: ' + str(tiquetes)
    elif tiquetes == 1:
        segunda_linha = 'Tíquete: ' + str(tiquetes)
    terceira_linha = 'Pagamento: ' + forma_pagamento(pagamento - 1).name
    return [primeira_linha, segunda_linha, terceira_linha]

def monta_registro(usuario: int, tiquetes: int, pagamento: int) -> Registro:
    '''
    Monta um Registro com o resumo de uma venda. Este resumo contém o tipo de usuário, 
    a quantidade de tíquetes vendidos e a forma de pagamento utilizada. O processo é 
    feito através de operações de listas e funções externas.
    A quantidade de tíquetes deve ser positiva.
    Exemplos:
    >>> monta_registro(1, 1, 1)
    Registro(Tipo_de_Usuario='ALUNO', Quantidade_de_Tiquetes=1, Forma_de_Pagamento='DINHEIRO')
    >>> monta_registro(3, 4, 2)
    Registro(Tipo_de_Usuario='EXTERNO', Quantidade_de_Tiquetes=4, Forma_de_Pagamento='PIX')
    '''
    usuario_tipo = tipo_usuario(usuario - 1).name
    pagamento_tipo = forma_pagamento(pagamento - 1).name
    return Registro(usuario_tipo, tiquetes, pagamento_tipo)

if __name__ == '__main__':
    main()
