### Atividade: Criação e Manipulação de Dados no Banco de Dados PostgreSQL com pgAdmin 4 e SQL (DDL e DML)

**Objetivo:**  
Nesta atividade, você vai praticar tanto a **DDL (Data Definition Language)** quanto a **DML (Data Manipulation Language)** no PostgreSQL, usando o **pgAdmin 4** e comandos SQL. Você criará uma tabela (DDL) e depois manipulará os dados (DML) inserindo, atualizando e deletando registros.

---

### Parte 1: Criação de Estrutura de Dados (DDL)

Nesta primeira parte, vamos usar comandos DDL para criar a estrutura da tabela no banco de dados.

---

### Passo a Passo

#### **Passo 1: Acessar o pgAdmin 4**

1. Abra o **pgAdmin 4** no seu computador.
2. Conecte-se ao seu servidor PostgreSQL. Se você ainda não configurou uma conexão, siga estes passos:
   - Clique com o botão direito em **Servers** no menu à esquerda.
   - Selecione **Connect** e insira as credenciais do servidor PostgreSQL (usuário e senha).

#### **Passo 2: Criar o Banco de Dados com Suporte a UTF-8**

1. Com o servidor conectado, clique com o botão direito sobre **Databases** no menu à esquerda.
2. Selecione **Create -> Database**.
3. No campo **Database Name**, digite **escola_db**.
4. Clique na aba **Definition**.
5. No campo **Encoding**, selecione **UTF-8** para garantir que o banco de dados suporte caracteres especiais, como acentos e símbolos de outros idiomas.
6. Clique em **Save** para criar o banco de dados.

#### **Passo 3: Criar a Tabela (DDL)**

1. No menu à esquerda, clique no nome do banco de dados **escola_db** que você acabou de criar.
2. No topo da janela, clique no ícone de **Query Tool** (ícone de documento com lápis) para abrir a ferramenta de consultas SQL.
3. Na área de consultas, insira o código SQL abaixo para criar a tabela **escola_alunos**:

    ```sql
    CREATE TABLE escola_alunos (
        id SERIAL PRIMARY KEY,
        municipio VARCHAR(100),
        codigo_censo VARCHAR(20),
        nome_escola VARCHAR(100),
        etapa VARCHAR(50),
        nome_completo VARCHAR(150),
        data_nascimento DATE,
        nome_mae VARCHAR(150),
        nome_pai VARCHAR(150)
    );
    ```

4. Após inserir o código, clique no ícone **Execute** (ícone de raio) para executar o comando SQL.
5. A tabela **escola_alunos** será criada com as seguintes colunas:
   - **id**: Um identificador único para cada aluno.
   - **municipio**: Nome do município.
   - **codigo_censo**: Código do censo escolar.
   - **nome_escola**: Nome da escola do aluno.
   - **etapa**: A etapa de ensino (Fundamental, Médio, etc.).
   - **nome_completo**: Nome completo do aluno.
   - **data_nascimento**: Data de nascimento do aluno.
   - **nome_mae**: Nome da mãe do aluno.
   - **nome_pai**: Nome do pai do aluno.

---

### Parte 2: Manipulação de Dados (DML)

Agora, vamos usar comandos DML para **inserir, atualizar e deletar** dados da tabela que você criou.

---

#### **Passo 4: Inserir Dados na Tabela (DML - INSERT)**

1. No **Query Tool**, insira o seguinte comando SQL para adicionar registros à tabela **escola_alunos**:

    ```sql
    INSERT INTO escola_alunos (municipio, codigo_censo, nome_escola, etapa, nome_completo, data_nascimento, nome_mae, nome_pai)
    VALUES ('São Paulo', '123456', 'Escola Municipal A', 'Fundamental', 'Maria Silva', '2010-05-12', 'Ana Silva', 'João Silva');
    ```

2. Clique em **Execute** para adicionar o registro.
3. Adicione outro registro:

    ```sql
    INSERT INTO escola_alunos (municipio, codigo_censo, nome_escola, etapa, nome_completo, data_nascimento, nome_mae, nome_pai)
    VALUES ('Rio de Janeiro', '789101', 'Escola Municipal B', 'Médio', 'Pedro Santos', '2009-09-20', 'Carla Santos', 'Carlos Santos');
    ```

4. Verifique os registros inseridos com o comando **SELECT**:

    ```sql
    SELECT * FROM escola_alunos;
    ```

#### **Passo 5: Atualizar Dados (DML - UPDATE)**

1. Agora, vamos atualizar um dos registros. Suponha que o aluno **Maria Silva** mudou de escola. Vamos alterar o nome da escola dela:

    ```sql
    UPDATE escola_alunos
    SET nome_escola = 'Escola Municipal C'
    WHERE nome_completo = 'Maria Silva';
    ```

2. Execute a consulta e, em seguida, verifique a atualização:

    ```sql
    SELECT * FROM escola_alunos;
    ```

#### **Passo 6: Deletar Dados (DML - DELETE)**

1. Por fim, vamos deletar um registro. Suponha que o registro de **Pedro Santos** foi inserido erroneamente e precisa ser removido:

    ```sql
    DELETE FROM escola_alunos
    WHERE nome_completo = 'Pedro Santos';
    ```

2. Execute o comando e verifique se o registro foi removido:

    ```sql
    SELECT * FROM escola_alunos;
    ```

---

### Parte 3: Desafio (Opcional)

Agora que você aprendeu a criar e manipular dados em uma tabela, aqui está um desafio para você:

1. **Adicionar uma nova coluna para telefone**:
    ```sql
    ALTER TABLE escola_alunos
    ADD telefone VARCHAR(20);
    ```

2. **Atualizar os registros para incluir o telefone dos alunos**:
    ```sql
    UPDATE escola_alunos
    SET telefone = '11999999999'
    WHERE nome_completo = 'Maria Silva';
    ```

---

### Conclusão:

Nesta atividade, você praticou tanto a criação de estrutura de dados (DDL) quanto a manipulação de dados (DML) no PostgreSQL usando o pgAdmin 4. Você aprendeu a criar uma tabela, inserir dados, atualizar registros e deletar entradas. Esses conceitos são fundamentais para trabalhar com bancos de dados de forma eficiente.