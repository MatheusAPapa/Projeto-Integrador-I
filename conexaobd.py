import mysql.connector
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '#$Rsac12', # colocar a senha
    database = 'PI'
)
cursor = conexao.cursor()