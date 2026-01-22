import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='********',
    database='galpao'
)

cursor = conn.cursor()
cursor.execute('DELETE FROM estoques WHERE idestoques = 3')
conn.commit()  # Salva as alterações no banco de dados

# Verifica se a alteração foi feita corretamente
cursor.execute('SELECT nome_produto FROM estoques WHERE idestoques = 1')
resultado = cursor.fetchall()
print(f"Produto atualizado: {resultado}")

cursor.close()
conn.close()