import mysql.connector
import menus

print('''
1 - Módulo de gerênciamento
2 - Módulo de votação
''')
escolha = int(input('Qual módulo você deseja entrar? '))
opcao = 0
match escolha:
    case 1:
        menus.menuModGere()
        match escolha:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                menus.menuInic()
            case _:
                print('Opção inválidada')
    case 2:
        menus.menuModVota()
        match escolha:
            #abrir sist de votação
            case 1:
                pass
            #auditoria
            case 2:
                pass
            #resultado
            case 3:
                menus.menuResulVota()
            #voltar
            case 4:
                menus.menuInic()
            case _:
                print('Opção inválida')
    case _:
        print('Opção inválida')