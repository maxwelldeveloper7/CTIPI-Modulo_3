### Semana 15: Criação do Modelo Lógico e Físico do Banco de Dados
![](./assets/s15.jpeg)
**Bem-vindos à Semana 15!**

Nesta semana, vamos transformar o planejamento do projeto em um **modelo lógico e físico** de banco de dados. Esses modelos são essenciais para organizar e estruturar os dados de forma eficiente, atendendo aos requisitos definidos na fase de planejamento.

---

### Objetivos da Semana

1. **Criar o Modelo Lógico do Banco de Dados**: Organizar as entidades, atributos e relacionamentos entre as tabelas.
2. **Aplicar Normalização**: Melhorar a organização das tabelas, eliminando redundâncias.
3. **Desenvolver o Modelo Físico do Banco de Dados**: Implementar o modelo lógico no sistema de gerenciamento de banco de dados (SGBD) escolhido.
4. **Estabelecer Chaves Primárias e Estrangeiras**: Garantir a integridade dos dados e o relacionamento entre tabelas.

---

### Passos para Criar o Modelo Lógico

O **modelo lógico** é um diagrama que representa a estrutura do banco de dados em termos de entidades (tabelas), atributos (colunas) e relacionamentos. Ele é independente de software e ajuda a visualizar como os dados estão organizados.

#### Etapas da Criação do Modelo Lógico

1. **Identificar as Entidades**:
   - Entidades representam as tabelas principais. Por exemplo, em um sistema de vendas, as entidades podem ser **Clientes**, **Pedidos** e **Produtos**.

2. **Definir os Atributos de Cada Entidade**:
   - Os atributos são as informações que serão armazenadas em cada entidade. Por exemplo, a entidade **Clientes** pode ter os atributos `nome`, `endereço`, `telefone` e `email`.

3. **Estabelecer os Relacionamentos**:
   - Relacionamentos conectam as entidades. Por exemplo, um **Cliente** pode ter muitos **Pedidos**, então temos um relacionamento 1:N entre **Clientes** e **Pedidos**.

4. **Aplicar Normalização**:
   - A normalização organiza as tabelas para evitar redundâncias. As principais formas normais (1ª FN, 2ª FN e 3ª FN) ajudam a garantir que os dados estejam bem estruturados.

---

### Passos para Criar o Modelo Físico

O **modelo físico** é a implementação do modelo lógico no SGBD, onde as tabelas e seus relacionamentos são configurados com tipos de dados específicos e outras configurações.

#### Etapas da Criação do Modelo Físico

1. **Escolha dos Tipos de Dados**:
   - Cada coluna precisa de um tipo de dado adequado, como `VARCHAR` para texto, `INTEGER` para números inteiros e `DATE` para datas. Escolher o tipo de dado correto é importante para a eficiência do banco.

2. **Definição de Chaves Primárias e Estrangeiras**:
   - A **chave primária** é um identificador único para cada registro na tabela (como o `id`). As **chaves estrangeiras** são usadas para conectar as tabelas relacionadas, como o `id_cliente` na tabela de **Pedidos**.

3. **Criação de Tabelas no SGBD**:
   - No SGBD escolhido (como PostgreSQL), crie as tabelas com os atributos e tipos de dados definidos no modelo físico.

4. **Definir Restrições e Índices**:
   - Restrições como `NOT NULL` e `UNIQUE` ajudam a garantir a integridade dos dados, enquanto **índices** aceleram o acesso a colunas específicas.

---

### Exemplo Prático

#### Modelo Lógico

- **Clientes**: id_cliente (PK), nome, endereço, telefone, email
- **Pedidos**: id_pedido (PK), data, total, id_cliente (FK)
- **Produtos**: id_produto (PK), nome, preco, estoque
- **Itens_Pedido**: id_item (PK), quantidade, preco_unitario, id_pedido (FK), id_produto (FK)

#### Modelo Físico

```sql
CREATE TABLE Clientes (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(200),
    telefone VARCHAR(15),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE Pedidos (
    id_pedido SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    total DECIMAL(10, 2),
    id_cliente INTEGER,
    FOREIGN KEY (id_cliente) REFERENCES Clientes (id_cliente)
);

CREATE TABLE Produtos (
    id_produto SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    estoque INTEGER NOT NULL
);

CREATE TABLE Itens_Pedido (
    id_item SERIAL PRIMARY KEY,
    quantidade INTEGER NOT NULL,
    preco_unitario DECIMAL(10, 2),
    id_pedido INTEGER,
    id_produto INTEGER,
    FOREIGN KEY (id_pedido) REFERENCES Pedidos (id_pedido),
    FOREIGN KEY (id_produto) REFERENCES Produtos (id_produto)
);
```

---

### Atividade da Semana (Prática com Modelos Lógico e Físico)

Para praticar, responda às questões e crie um exemplo de modelo lógico e físico para um banco de dados de **Biblioteca**. Identifique as entidades principais (como **Livros**, **Autores** e **Empréstimos**), seus atributos e os relacionamentos.

#### Parte 1: Questões de Revisão

1. Qual é a função do modelo lógico?
   - a) Implementar as tabelas no SGBD.
   - b) Representar a estrutura do banco de dados em termos de entidades, atributos e relacionamentos.
   - c) Criar consultas SQL para o banco de dados.
   - d) Definir os tipos de dados para cada coluna.

2. O que é uma chave estrangeira?
   - a) Uma coluna que identifica exclusivamente cada registro em uma tabela.
   - b) Uma restrição para garantir que um valor seja único.
   - c) Um campo que conecta uma tabela a outra.
   - d) Um índice usado para acelerar consultas.

3. Por que é importante aplicar normalização no modelo lógico?
   - a) Para excluir dados antigos automaticamente.
   - b) Para organizar as tabelas, eliminando redundâncias e garantindo a integridade dos dados.
   - c) Para melhorar a segurança do banco de dados.
   - d) Para dividir o banco em vários servidores.

4. Qual é a principal diferença entre o modelo lógico e o modelo físico?
   - a) O modelo lógico usa índices e o físico não.
   - b) O modelo físico representa a implementação no SGBD, enquanto o lógico é apenas um plano de organização.
   - c) O modelo físico é independente do SGBD.
   - d) O modelo lógico define permissões de acesso.

5. O que significa “normalização” em bancos de dados?
   - a) Um método para dividir tabelas grandes em partes menores.
   - b) Um processo para criar restrições.
   - c) Uma técnica para organizar tabelas, eliminando redundâncias e mantendo a integridade.
   - d) Um tipo de dado para armazenar texto.

---

**Gabarito**:
1. b) Representar a estrutura do banco de dados em termos de entidades, atributos e relacionamentos.
2. c) Um campo que conecta uma tabela a outra.
3. b) Para organizar as tabelas, eliminando redundâncias e garantindo a integridade dos dados.
4. b) O modelo físico representa a implementação no SGBD, enquanto o lógico é apenas um plano de organização.
5. c) Uma técnica para organizar tabelas, eliminando redundâncias e mantendo a integridade.

---

### Conclusão

A criação do **modelo lógico** e do **modelo físico** é uma etapa essencial no desenvolvimento de um banco de dados. Com esses modelos, você garante que os dados estejam bem organizados, com integridade e prontos para serem implementados no SGBD. Esta semana é um grande passo na construção de seu projeto final, onde veremos a estrutura do banco de dados ganhar forma!