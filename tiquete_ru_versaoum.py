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
# Tíquetes totais e dinheiro total são, essencialmente, a mesma função, devo generalizá-las e utilizar
#seleção?
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

@dataclass
class Soma_Pagamento:
    '''
    A soma total de vendas por Pagamento.
    '''
    Dinheiro: int
    Pix: int
    Cartao: int

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
    print('Bem vindo ao sistema de vendas de tíquetes do RU')
    continuar = True
    vendas: list[Registro] = []
    while continuar:
        print('▷ Sistema ◁ Digite o número desejado, sem aspas')
        print('》 1 - Registrar uma venda')
        print('》 2 - Exibir o Relatório das vendas')
        print('》 0 - Sair e Apagar Relatório')
        inicializacao_str: str = input('》 ')
        inicializacao: int = int(inicializacao_str)
    
        if inicializacao == 0:
            continuar = False
        elif inicializacao == 1:
            registrar_venda(vendas)
        elif inicializacao == 2:
            relatorio_vendas(vendas)
        else:
            print('Entrada inválida, tente novamente')

    print('Até logo!')

def registrar_venda(vendas: list[Registro]) -> list[Registro]:
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

    registro: Registro = monta_registro(usuario, tiquetes, pagamento)
    total = str(total_da_venda(registro))
    print('Total:  ' + total + ' reais')

    print('Pressione Enter para registrar venda ou Espaço + Enter para descartá-la')
    entrada_confirmar = input('》 ')
    if entrada_confirmar == '':
        print('Venda registrada!')
        vendas.append(registro)
        print('Pressione Enter para registrar outra venda ou pressione Espaço + Enter para voltar à Tela Inicial')
        entrada_decisao = input('》 ')
        if entrada_decisao == '':
            registrar_venda(vendas)
    elif entrada_confirmar == ' ':
        print('Venda descartada! Voltando à Tela Inicial!')

    return vendas

def total_da_venda(registro: Registro) -> int:
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
    usuario = registro.Tipo_de_Usuario
    tiquete = registro.Quantidade_de_Tiquetes # para programador entender, utiliza-se classe Registro
    if usuario == 'ALUNO' or usuario == 'SERVIDOR_MENOS_QUE_TRES':
        valor_tiquete = 5
    elif usuario == 'DOCENTE' or usuario == 'SERVIDOR_MAIS_QUE_TRES':
        valor_tiquete = 10
    elif usuario == 'EXTERNO':
        valor_tiquete = 19
    valor_da_venda = tiquete * valor_tiquete
    return valor_da_venda

def loop_de_confirmacao(categoria: str) -> int:
    '''
    Fornece um loop genérico por while {condição} para quaisquer menus que 
    necessitem de confirmação do usuário. Indica qual foi a opção escolhida pelo usuário
    através de funções externas e retorna um inteiro que representa qual opção do menu foi escolhida.
    As entradas para a função feedback_entrada devem ser respeitadas.
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
        entrada_usuario_str = input('》 ')
        entrada_usuario = int(entrada_usuario_str)
        print(feedback_entrada(entrada_usuario, categoria))
        print('Pressione Enter para confirmar ou Espaço + Enter para digitar novamente')
        entrada_confirmar = input('》 ')
        if entrada_confirmar == '':
            reescrever = False
            opcao_escolhida = entrada_usuario
    return opcao_escolhida

def relatorio_vendas(vendas: list[Registro]) -> None:
    '''
    Apresenta as vendas.
    '''
    tiquetes = tiquetes_totais(vendas)
    print('Tíquetes vendidos: ', tiquetes)
    receita = receita_total(vendas)
    print('Receita do dia: ', receita)
    print(grafico(vendas, tiquetes, receita))
    menu_inicial = input('Pressione Enter para ir ao Menu Principal ou Espaço + Enter para ver os créditos')
    if menu_inicial == ' ':
        creditos()

def vendas_por_pagamento(vendas: list[Registro]) -> list[Soma_Pagamento]:
    '''
    Soma a quantidade de vendas por categoria de pagamento, de acordo com a
    quantidade de tíquetes vendidos em cada venda.
    Exemplo:
    >>> vendas_por_pagamento(Registro(Tipo_de_Usuario='ALUNO', Quantidade_de_Tiquetes=1,
    Forma_de_Pagamento='DINHEIRO')]))
    [1, 0, 0]
    '''
    

def creditos() -> None:
    '''
    Exibe os créditos do programa.
    Exemplo:
    >>> credito()
    Toda a glória seja a Deus
    Feito por Paulo Guilherme Schnaufer
    Com colaboração de Paulo Guilherme Schnaufer
    Dublagem feita por Paulo Guilherme Schnaufer (Dublagem ainda não implementada)
    Código feito por Paulo Guilherme Schnaufer
    Créditos feitos por Paulo Guilherme Schnaufer
    Toda a glória seja a Deus
    '''
    print('Toda a glória seja a Deus')
    print('Feito por Paulo Guilherme Schnaufer')
    print('Com colaboração de Paulo Guilherme Schnaufer')
    print('Dublagem feita por Paulo Guilherme Schnaufer (Dublagem ainda não implementada)')
    print('Código feito por Paulo Guilherme Schnaufer')
    print('Créditos feitos por Paulo Guilherme Schnaufer')
    print('Toda a glória seja a Deus')

def tiquetes_totais(vendas: list[Registro], categoria: str) -> int:
    '''
    Soma todos os tíquetes de todas as vendas registradas.
    Exemplos:
    >>> tiquetes_totais([Registro(Tipo_de_Usuario='ALUNO', Quantidade_de_Tiquetes=1, Forma_de_Pagamento='DINHEIRO')])
    1
    '''
    lst_tiquetes = []
    for registro in vendas:
        tiquetes = registro.Quantidade_de_Tiquetes
        lst_tiquetes.append(tiquetes)
    total_de_tiquetes = soma_ints(lst_tiquetes)
    return total_de_tiquetes

def receita_total(vendas: list[Registro]) -> int:
    '''
    Soma todo o dinheiro de todas as vendas registradas.
    Exemplos:
    >>> receita_total([Registro(Tipo_de_Usuario='ALUNO', Quantidade_de_Tiquetes=1, Forma_de_Pagamento='DINHEIRO')])
    5
    '''
    lst_dinheiro = []
    for registro in vendas:
        dinheiro = registro.Forma_de_Pagamento
        lst_dinheiro.append(dinheiro)
    receita_total = soma_ints(lst_dinheiro)
    return receita_total

def soma_ints(lst_ints: list[int]) -> int:
    '''
    Soma todos os números inteiros de uma lista de números inteiros.
    A entrada deve ser uma lista de números inteiros positivos.
    Exemplo:
    >>> soma_ints([1, 2, 3, 4,])
    10
    '''
    soma = 0
    for n in lst_ints:
        soma = soma + n
    return soma

def grafico(vendas: list[Registro]) -> str:
    '''
    Cria um gráfico vertical em unicode de acordo com a porcentagem relativa de
    cada categoria nas vendas totais.
    Exemplo:
    >>> grafico([Registro(Tipo_de_Usuário='ALUNO', Quantidade_de_Tiquetes=1, Forma_de_Pagamento='DINHEIRO'), Registro(
    Tipo_de_Usuário='DOCENTE', Quantidade_de_Tiquetes=3, Forma_de_Pagamento='CARTAO')])

                                             75%
                                             ███
        1%                                   ███
        ███          0%           0%         ███         0%     
    |   Aluno   |Servidor<=3| Servidor>3|  Docente  |  Externo  |

        75%
        ███
        ███              25%
        ███              ███
    | Cartão |  PIX   |Dinheiro|
    '''
    bloco_cheio = '    ███     '
    bloco_vazio = '            '
    bloco_numerico_dois_digitos = '      ', dois_digitos,'%     '
    bloco_numerico_um_digito = '     ', um_digito,'%      '
    base_usuario = '|   Aluno   |Servidor<=3| Servidor>3|  Docente  |  Externo  |'
    base_pagamento = '|  Cartão  | PIX  |  Dinheiro  |'
    total_da_venda

    return ''

def tipo_usuario(n: int) -> Usuario:
    '''
    Assimila um número correspondente a uma categoria de relação do usuário do programa com
    a universidade e a converte em um tipo de usuário manejável para o programador.
    Feito através de listas dos tipos de Usuário.
    Exemplos:
    >>> tipo_usuario(0)
    <Usuario.ALUNO: 1>
    '''
    usuarios: list[Usuario] = [Usuario.ALUNO, Usuario.DOCENTE, Usuario.EXTERNO, \
                               Usuario.SERVIDOR_MAIS_QUE_TRES, Usuario.SERVIDOR_MENOS_QUE_TRES]
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
    Para a categoria 'Usuário', a entrada deve ser um número inteiro de 1 a 5,
    para a categoria 'Tíquetes', a entrada deve ser um número,
    para a categoria 'Pagamento', a entrada deve ser um número inteiro de 1 a 3.
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
