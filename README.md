# CRUD Python com MySQL

Este projeto demonstra como realizar operações CRUD (Create, Read, Update, Delete) em um banco de dados MySQL usando Python e a biblioteca mysql-connector-python.

## O que é CRUD?

CRUD é um acrônimo para as quatro operações básicas que podem ser realizadas em dados:

- **CREATE (Criar)**: Inserir novos registros no banco de dados
- **READ (Ler)**: Consultar e recuperar dados do banco de dados
- **UPDATE (Atualizar)**: Modificar registros existentes no banco de dados
- **DELETE (Deletar)**: Remover registros do banco de dados

## Requisitos

Para executar este script, você precisa ter instalado:

1. Python 3.x
2. mysql-connector-python (biblioteca para conectar ao MySQL)
3. Servidor MySQL em execução

## Instalação

Para instalar a biblioteca mysql-connector-python, execute o seguinte comando no terminal:

```
pip install mysql-connector-python
```

## Estrutura do Código

### Conexão com o Banco de Dados

O script começa estabelecendo uma conexão com o banco de dados MySQL:

```python
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='********',
    database='bdyoutube'
)

cursor = conn.cursor()
```

**Explicação:**
- `mysql.connector.connect()`: Estabelece a conexão com o servidor MySQL
- `host`: Endereço do servidor MySQL (normalmente 'localhost' para instalações locais)
- `user`: Nome do usuário do banco de dados
- `password`: Senha do usuário
- `database`: Nome do banco de dados a ser utilizado
- `cursor()`: Cria um cursor que permite executar comandos SQL

### Operações CRUD

#### CREATE - Inserir Dados

Para inserir um novo registro na tabela `vendas`:

```python
nome_produto = "chocolate"
valor = 15
comando = f'INSERT INTO vendas (nome_porduto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conn.commit()
```

**Explicação:**
- O comando SQL `INSERT INTO` adiciona um novo registro
- `nome_porduto` e `valor` são as colunas da tabela
- `VALUES` especifica os valores a serem inseridos
- `cursor.execute()` executa o comando SQL
- `conn.commit()` confirma e salva a alteração no banco de dados

**Importante:** Sem o `commit()`, as alterações não serão salvas permanentemente.

#### READ - Ler Dados

Para consultar e recuperar dados da tabela:

```python
comando = 'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)
```

**Explicação:**
- O comando SQL `SELECT * FROM vendas` recupera todos os registros da tabela `vendas`
- `cursor.execute()` executa a consulta
- `cursor.fetchall()` recupera todos os resultados da consulta
- `resultado` contém uma lista de tuplas com os dados

**Observação:** Para operações de leitura (SELECT), o `commit()` não é necessário, pois não há modificação dos dados.

#### UPDATE - Atualizar Dados

Para modificar registros existentes:

```python
nome_produto = "todynho"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conn.commit()
```

**Explicação:**
- O comando SQL `UPDATE` modifica registros existentes
- `SET valor = {valor}` define o novo valor para a coluna `valor`
- `WHERE nome_produto = "{nome_produto}"` especifica qual registro será atualizado (condição)
- `conn.commit()` salva a alteração

#### DELETE - Deletar Dados

Para remover registros do banco de dados:

```python
nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conn.commit()
```

**Explicação:**
- O comando SQL `DELETE FROM` remove registros da tabela
- `WHERE nome_produto = "{nome_produto}"` especifica qual registro será deletado
- `conn.commit()` confirma a exclusão

**Cuidado:** O comando DELETE remove permanentemente os dados. Certifique-se de usar a cláusula WHERE corretamente para evitar deletar todos os registros.

### Fechamento da Conexão

Ao final do script, é importante fechar o cursor e a conexão:

```python
cursor.close()
conn.close()
```

**Explicação:**
- Libera recursos do sistema
- Fecha a conexão com o banco de dados de forma adequada
- Boa prática de programação

## Estrutura da Tabela

O script trabalha com a tabela `vendas` no banco de dados `bdyoutube`. A tabela possui as seguintes colunas:

- `idVendas`: Inteiro, chave primária, auto incremento
- `nome_porduto`: Texto (VARCHAR 45 caracteres)
- `valor`: Inteiro

**Observação:** A coluna `nome_porduto` possui um erro de digitação no banco de dados (deveria ser `nome_produto` com "u"), mas o código usa o nome correto conforme está na estrutura da tabela.

## Como Usar

1. Configure as credenciais do banco de dados no início do arquivo:
   - Altere `host`, `user`, `password` e `database` conforme necessário

2. Escolha qual operação CRUD deseja executar:
   - Descomente o bloco de código correspondente (CREATE, READ, UPDATE ou DELETE)
   - Ajuste os valores das variáveis conforme necessário

3. Execute o script:
   ```
   python crud.py
   ```

## Segurança e Boas Práticas

**Importante:** Este código usa interpolação de strings (f-strings) diretamente no SQL, o que pode ser vulnerável a ataques de SQL Injection. Para aplicações reais em produção, é recomendado usar:

- Prepared statements com parâmetros
- Validação de entrada do usuário
- Uso de bibliotecas ORM (Object-Relational Mapping) como SQLAlchemy

Exemplo de uso mais seguro:

```python
comando = 'INSERT INTO vendas (nome_porduto, valor) VALUES (%s, %s)'
valores = (nome_produto, valor)
cursor.execute(comando, valores)
conn.commit()
```

## Solução de Problemas

- **Erro de conexão:** Verifique se o servidor MySQL está em execução e se as credenciais estão corretas
- **Erro de tabela não encontrada:** Verifique se o banco de dados e a tabela existem
- **Erro de coluna não encontrada:** Verifique se os nomes das colunas estão corretos na estrutura da tabela
- **Alterações não salvas:** Certifique-se de chamar `conn.commit()` após operações que modificam dados (INSERT, UPDATE, DELETE)
