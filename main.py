import mysql.connector
import menus
import os

def iniciar():
    escolha = menus.menuInic()
    #modulo de gerenciamento
    match escolha:
        case 1:
            opcao = menus.menuModGere()
            match opcao:
                #cadastro de novo eleitor
                case 1:
                    pass
                #editar dados do eleitor
                case 2:
                    pass
                #listagem de todos os eleitores
                case 3:
                    pass
                #fazer uma busca por eleitor
                case 4:
                    pass
                #remover um eleitor
                case 5:
                    pass
                #voltar
                case 6:
                    iniciar()
    
        #modulo de votação
        case 2:
            opcao = menus.menuModVota()
            match opcao:
                #abrir sist. de votação
                case 1:
                    pass
                #auditoria
                case 2:
                    opcaoAudVota = menus.menuAudVota()
                    match opcaoAudVota:
                        #logs de ocorrência
                        case 1:
                            pass
                        #protocolos de votação
                        case 2:
                            pass
                        #voltar
                        case 3:
                           menus.menuModVota()

                #resultado
                case 3:
                    opcaoResulVota = menus.menuResulVota()
                    match opcaoResulVota:
                        #boletim de urna
                        case 1:
                            pass
                        #estatísticas do candidato
                        case 2:
                            pass
                        #votos por partido
                        case 3:
                            pass
                        #validação de integridade
                        case 4:
                            pass
                        #voltar
                        case 5:
                            menus.menuModVota()
                            
                #voltar
                case 4:
                    iniciar()
                    
iniciar()