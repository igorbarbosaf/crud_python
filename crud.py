import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='********',
    database='bdyoutube'
)

cursor = conn.cursor()

nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conn.commit() # Edita o banco de dados



cursor.close()
conn.close()

# CREATE: 
#nome_produto = "chocolate"
#valor = 15
#comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#cursor.execute(comando)
#conn.commit() # Edita o banco de dados


# READ:
#comando = 'SELECT * FROM vendas'
#cursor.execute(comando)
#conn.commit() # Edita o banco de dados
#resultado = cursor.fetchall() # ler o banco de dados
#print(resultado)

# UPDATE:
#nome_produto = "todynho"
#valor = 6
#comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conn.commit() # Edita o banco de dados

# DELETE:
#nome_produto = "todynho"
#comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conn.commit() # Edita o banco de dados