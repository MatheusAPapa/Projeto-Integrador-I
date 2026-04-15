import mysql.connector
import random
import string
import datetime

def gerar_chave_acesso(nome_completo):
    """Gera a chave de acesso no formato solicitado"""
    partes = nome_completo.strip().split()
    
    if len(partes) == 0:
        return "XXX0000"
    
    # Duas primeiras letras do primeiro nome
    primeiro_nome = partes[0][:2].upper()
    
    # Primeira letra do segundo nome (se existir)
    if len(partes) >= 2:
        segunda_letra = partes[1][0].upper()
    else:
        segunda_letra = "X"   # caso tenha apenas um nome
    
    # 4 dígitos aleatórios
    digitos = ''.join(random.choices(string.digits, k=4))
    
    chave = primeiro_nome + segunda_letra + digitos
    return chave

def cadastrar_novo_eleitor():
    print("\n=== CADASTRO DE NOVO ELEITOR ===\n")
    
    # Nome completo 
    while True:
        nome = input("Nome completo: ").strip()
        if nome:
            break
        print("Erro: Nome completo é obrigatório!")
    
    # Título de eleitor 
    while True:
        titulo = input("Título de Eleitor: ").strip()
        if titulo:
            break
        print("Erro: Título de Eleitor é obrigatório!")
    
    # CPF 
    while True:
        cpf_input = input("CPF (apenas números): ").strip()
        cpf = ''.join(filter(str.isdigit, cpf_input))
        if len(cpf) == 11:
            break
        else:
            print("Erro: CPF deve conter exatamente 11 dígitos!")
    
    # Mesário 
    while True:
        mesario_input = input("Atuará como mesário? (S/N): ").strip().upper()
        if mesario_input in ['S', 'SIM', 'N', 'NAO', 'NÃO']:
            mesario = mesario_input in ['S', 'SIM']
            break
        else:
            print("Erro: Responda apenas com S ou N!")
    
    # Inserir no banco de dados
    try:
        conn = mysql.connector.connect(
            host="localhost",      
            user="root",           
            password="#$Rsac12",           
            database="PI"     
        )
        
        cursor = conn.cursor()
        
        sql = """
            INSERT INTO eleitores (nome_completo, titulo_eleitor, cpf, mesario)
            VALUES (%s, %s, %s, %s)
        """
        valores = (nome, titulo, cpf, mesario)
        
        cursor.execute(sql, valores)
        conn.commit()
        
        print("\n" + "="*36)
        print("✅ ELEITOR CADASTRADO COM SUCESSO!")
        print("="*36)
        print(f"Nome:     {nome}")
        print(f"Título:   {titulo}")
        print(f"CPF:      {cpf}")
        print(f"🔑 CHAVE DE ACESSO : {gerar_chave_acesso}")
        print(f"Mesário:  {'Sim' if mesario else 'Não'}")
        print("="*36)

    except mysql.connector.IntegrityError as err:
        if "Duplicate entry" in str(err):
            if "cpf" in str(err).lower():
                print("\n❌ Erro: Este CPF já está cadastrado no sistema!")
        else:
            print(f"\n❌ Erro: {err}")
    except mysql.connector.Error as err:
        print(f"\n❌ Erro ao cadastrar no banco de dados: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
