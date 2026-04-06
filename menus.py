#menu inicial
def menuInic ():
    print('''
    1 - Módulo de gerênciamento
    2 - Módulo de votação
    ''')
    escolha = int(input('Qual módulo você deseja entrar? '))
    return escolha

#modulo de gerenciamento
def menuModGere ():
    print('''
    1 - Cadastrar eleitor 
    2 - Editar dados do eleitor
    3 - Todos os eleitores
    4 - Buscar eleitor
    5 - Remover eleitor 
    6 - voltar   
    ''')
    escolha = int(input('Selecione uma das opções acima: '))
    return escolha



#modulo de votação
def menuModVota ():
    print('''
    1 - Abri sistema de votação
    2 - Auditoria da votação
    3 - Resultado da votação
    4 - voltar
    ''')
    escolha = int(input('Selecione uma das opções acima: '))
    return escolha

def menuAudVota ():
    print('''
    1 - Logs da votação
    2 - Protocolos de votação
    ''')
    escolha = int(input('Selecione uma das opções acima: '))
    return escolha

def menuResulVota ():
    print('''
    1 - Boletim de urna
    2 - Estatísticas 
    3 - Votos por partido
    4 - Validação de integridade
    ''')
    escolha = int(input('Selecione uma das opções acima: '))
    return escolha