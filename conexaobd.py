import mysql.connector
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '#$Rsac12', # ver com a joice
    database = 'PI'
)
cursor = conexao.cursor()