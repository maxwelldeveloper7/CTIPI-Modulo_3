### Semana 16: Implementação das Tabelas, Chaves e Relacionamentos
![](./assets/s16.jpeg)
**Bem-vindos à Semana 16!**

Nesta semana, vamos dar o próximo passo em nosso projeto de banco de dados: a **implementação das tabelas, chaves e relacionamentos**. Esta é a etapa onde transformamos o modelo físico em um banco de dados real, criando tabelas e configurando as chaves primárias e estrangeiras para garantir que os dados estejam organizados e conectados corretamente.

---

### Objetivos da Semana

1. **Criar Tabelas no SGBD**: Implementar as tabelas definidas no modelo físico, configurando suas colunas e tipos de dados.
2. **Definir Chaves Primárias**: Garantir que cada tabela tenha uma coluna ou conjunto de colunas que identifiquem exclusivamente cada registro.
3. **Estabelecer Relacionamentos com Chaves Estrangeiras**: Criar ligações entre tabelas, garantindo que os dados estejam relacionados de maneira lógica e coerente.
4. **Aplicar Restrições de Integridade**: Adicionar restrições que garantam a consistência dos dados, como `NOT NULL` e `UNIQUE`.

---

### Passo a Passo para Implementação das Tabelas

#### 1. Criação das Tabelas

Para começar, você deve criar cada tabela no SGBD (como PostgreSQL), com base no modelo físico. Cada tabela precisa ter suas colunas, tipos de dados e propriedades configuradas.

**Exemplo de criação de uma tabela Clientes:**

```sql
CREATE TABLE Clientes (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(200),
    telefone VARCHAR(15),
    email VARCHAR(100) UNIQUE
);
```

Neste exemplo, estamos criando uma tabela chamada **Clientes** com colunas para `id_cliente`, `nome`, `endereço`, `telefone` e `email`. A coluna `id_cliente` é uma chave primária e será preenchida automaticamente como um número único (usando `SERIAL`).

#### 2. Definição de Chaves Primárias

A **chave primária** é uma coluna (ou conjunto de colunas) que identifica exclusivamente cada registro em uma tabela. Em geral, ela é definida como uma coluna `ID`, mas pode ser qualquer coluna que seja única e obrigatória.

**Exemplo de chave primária:**

```sql
CREATE TABLE Produtos (
    id_produto SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    estoque INTEGER NOT NULL
);
```

Aqui, a coluna `id_produto` é a chave primária da tabela **Produtos**.

#### 3. Estabelecimento de Relacionamentos com Chaves Estrangeiras

As **chaves estrangeiras** permitem que você conecte uma tabela a outra. Elas referenciam a chave primária de outra tabela, criando uma ligação entre os dados.

**Exemplo de chave estrangeira para conectar Pedidos e Clientes:**

```sql
CREATE TABLE Pedidos (
    id_pedido SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    total DECIMAL(10, 2),
    id_cliente INTEGER,
    FOREIGN KEY (id_cliente) REFERENCES Clientes (id_cliente)
);
```

Neste exemplo, a coluna `id_cliente` na tabela **Pedidos** é uma chave estrangeira que se relaciona com a coluna `id_cliente` na tabela **Clientes**. Isso significa que cada pedido está associado a um cliente específico.

#### 4. Aplicação de Restrições de Integridade

Restrições de integridade ajudam a manter a consistência dos dados, garantindo que certas condições sejam respeitadas.

- **NOT NULL**: Garante que a coluna não pode ter valor nulo.
- **UNIQUE**: Garante que todos os valores na coluna são únicos.
- **FOREIGN KEY**: Cria um vínculo entre tabelas, validando que o valor existe na tabela relacionada.

**Exemplo de restrições de integridade:**

```sql
CREATE TABLE Fornecedores (
    id_fornecedor SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(15) UNIQUE,
    email VARCHAR(100),
    id_produto INTEGER,
    FOREIGN KEY (id_produto) REFERENCES Produtos (id_produto)
);
```

Neste exemplo, `telefone` é definido como `UNIQUE`, e `id_produto` é uma chave estrangeira que se conecta à tabela **Produtos**.

---

### Testando as Relações e Integridade

Depois de criar as tabelas, é importante testar os relacionamentos e as restrições de integridade. Você pode inserir dados de teste e verificar se:

1. **Os valores são únicos e obrigatórios** onde aplicável.
2. **Os relacionamentos** entre tabelas estão funcionando corretamente, como ao inserir um pedido que referencia um cliente existente.

**Exemplo de inserção de dados de teste:**

```sql
INSERT INTO Clientes (nome, endereco, telefone, email) VALUES ('João Silva', 'Rua A, 123', '123456789', 'joao@email.com');
INSERT INTO Pedidos (data, total, id_cliente) VALUES ('2024-11-10', 150.00, 1);
```

Esse exemplo insere um cliente e um pedido que se relaciona com o cliente.

---

### Atividade da Semana (Prática com Tabelas e Relacionamentos)

Para praticar o que aprendemos esta semana, complete as seguintes atividades:

1. Crie uma tabela chamada **Funcionários** com as seguintes colunas: `id_funcionario`, `nome`, `cargo`, `salario` e `email`. Defina `id_funcionario` como a chave primária e `email` como `UNIQUE`.

2. Crie uma tabela **Projetos** que tenha uma chave estrangeira `id_funcionario` para conectar cada projeto a um funcionário responsável.

#### Parte 1: Questões de Revisão

1. O que é uma chave primária?
   - a) Uma coluna que permite valores duplicados.
   - b) Uma coluna ou conjunto de colunas que identifica exclusivamente cada registro.
   - c) Uma tabela que conecta duas outras tabelas.
   - d) Um tipo de dado para armazenar texto.

2. Qual é a função de uma chave estrangeira?
   - a) Conectar uma tabela a outra, referenciando a chave primária da tabela relacionada.
   - b) Garantir que uma coluna tenha valores únicos.
   - c) Restringir o número de registros em uma tabela.
   - d) Dividir os dados em partes menores.

3. Qual restrição garante que uma coluna não pode ter valores duplicados?
   - a) NOT NULL
   - b) UNIQUE
   - c) FOREIGN KEY
   - d) SERIAL

4. O que significa SERIAL em uma coluna de chave primária?
   - a) A coluna será automaticamente preenchida com valores únicos.
   - b) A coluna permite valores duplicados.
   - c) A coluna armazena texto.
   - d) A coluna é obrigatória.

5. Qual comando cria um relacionamento entre as tabelas Clientes e Pedidos?
   - a) `JOIN`
   - b) `FOREIGN KEY`
   - c) `UNIQUE`
   - d) `NOT NULL`

---

**Gabarito**:
1. b) Uma coluna ou conjunto de colunas que identifica exclusivamente cada registro.
2. a) Conectar uma tabela a outra, referenciando a chave primária da tabela relacionada.
3. b) UNIQUE
4. a) A coluna será automaticamente preenchida com valores únicos.
5. b) FOREIGN KEY

---

### Conclusão

A **implementação de tabelas, chaves e relacionamentos** é uma etapa crucial para garantir a organização, integridade e conexão dos dados no banco de dados. Com essa estrutura bem configurada, o banco de dados estará preparado para armazenar e relacionar dados de maneira eficiente e segura.