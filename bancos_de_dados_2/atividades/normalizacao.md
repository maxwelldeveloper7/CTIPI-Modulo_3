### Atividade de Continuação: Normalização da Tabela `escola_alunos` no PostgreSQL com pgAdmin 4
![](./assets/normalizacao.jpeg)
**Objetivo:**  
Nesta atividade, você vai praticar o conceito de **normalização de dados** no PostgreSQL, utilizando a tabela que criamos anteriormente, `escola_alunos`. O processo de normalização é essencial para melhorar a estrutura do banco de dados, eliminar redundâncias e garantir a integridade dos dados. Você vai identificar os campos candidatos à normalização e dividir os dados em várias tabelas normalizadas.

---

### Passo a Passo

#### **Passo 1: Revisão da Tabela `escola_alunos`**

Vamos revisar a estrutura da tabela `escola_alunos` criada anteriormente:

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

Essa tabela armazena muitas informações em uma única estrutura. No entanto, podemos identificar algumas redundâncias e dependências que podem ser otimizadas através do processo de **normalização**.

#### **Passo 2: Identificando os Campos Candidatos à Normalização**

A tabela `escola_alunos` contém os seguintes campos que podem ser normalizados:

1. **Nome da Escola** e **Código do Censo**: O nome da escola e o código do censo podem ser repetidos várias vezes para diferentes alunos que estudam na mesma escola. Isso indica uma redundância.
2. **Município**: O campo `municipio` também pode se repetir, pois várias escolas podem estar localizadas no mesmo município.
3. **Nome do Pai** e **Nome da Mãe**: Em uma família com mais de um aluno, o nome dos pais pode se repetir.

#### **Passo 3: Primeira Forma Normal (1FN)**

Para aplicar a **Primeira Forma Normal (1FN)**, precisamos garantir que os dados estejam em formato tabular, ou seja, sem valores repetidos ou grupos de dados múltiplos nas colunas. A tabela `escola_alunos` já está em conformidade com a 1FN, pois cada campo contém um único valor por linha.

#### **Passo 4: Segunda Forma Normal (2FN)**

Na **Segunda Forma Normal (2FN)**, eliminamos dependências parciais, ou seja, colunas que dependem apenas de parte da chave primária. Como a chave primária da tabela é o campo `id` (que é único para cada aluno), a dependência parcial não é um problema. Porém, ainda temos redundâncias, como o nome da escola e o município que podem ser normalizados.

##### Passo 4.1: Criar Tabela para Escolas

1. Vamos criar uma tabela separada para armazenar as informações da escola, eliminando a redundância de ter o nome da escola repetido para cada aluno.

```sql
CREATE TABLE escolas (
    codigo_censo VARCHAR(20) PRIMARY KEY,
    nome_escola VARCHAR(100),
    municipio VARCHAR(100)
);
```

2. Agora, vamos inserir os dados da tabela `escola_alunos` na nova tabela `escolas`.

```sql
INSERT INTO escolas (codigo_censo, nome_escola, municipio)
SELECT DISTINCT codigo_censo, nome_escola, municipio
FROM escola_alunos;
```

3. Remover as colunas **codigo_censo**, **nome_escola** e **municipio** da tabela `escola_alunos`:

```sql
ALTER TABLE escola_alunos
DROP COLUMN codigo_censo, DROP COLUMN nome_escola, DROP COLUMN municipio;
```

4. Adicionar a chave estrangeira **codigo_censo** na tabela `escola_alunos`, que agora fará referência à tabela `escolas`:

```sql
ALTER TABLE escola_alunos
ADD codigo_censo VARCHAR(20);

ALTER TABLE escola_alunos
ADD CONSTRAINT fk_codigo_censo FOREIGN KEY (codigo_censo) REFERENCES escolas(codigo_censo);
```

5. Atualizar os registros em `escola_alunos` para associá-los à tabela `escolas`:

```sql
UPDATE escola_alunos
SET codigo_censo = (SELECT codigo_censo FROM escolas WHERE escolas.nome_escola = 'Escola Municipal A');
```

#### **Passo 5: Terceira Forma Normal (3FN)**

Na **Terceira Forma Normal (3FN)**, eliminamos dependências transitivas, ou seja, quando uma coluna depende de outra que não seja a chave primária.

##### Passo 5.1: Criar Tabela para Pais

Os campos **nome_mae** e **nome_pai** podem ser movidos para uma nova tabela, chamada `familia`, para evitar a repetição de nomes nos casos de famílias com mais de um aluno.

1. Criar a tabela `familia`:

```sql
CREATE TABLE familia (
    id_familia SERIAL PRIMARY KEY,
    nome_mae VARCHAR(150),
    nome_pai VARCHAR(150)
);
```

2. Inserir os dados distintos de nomes de pais e mães na nova tabela:

```sql
INSERT INTO familia (nome_mae, nome_pai)
SELECT DISTINCT nome_mae, nome_pai
FROM escola_alunos;
```

3. Adicionar uma chave estrangeira **id_familia** na tabela `escola_alunos`:

```sql
ALTER TABLE escola_alunos
ADD id_familia INT;

ALTER TABLE escola_alunos
ADD CONSTRAINT fk_familia FOREIGN KEY (id_familia) REFERENCES familia(id_familia);
```

4. Atualizar os registros em `escola_alunos` para associá-los à tabela `familia`:

```sql
UPDATE escola_alunos
SET id_familia = (SELECT id_familia FROM familia WHERE familia.nome_mae = escola_alunos.nome_mae AND familia.nome_pai = escola_alunos.nome_pai);
```

5. Remover os campos **nome_mae** e **nome_pai** da tabela `escola_alunos`:

```sql
ALTER TABLE escola_alunos
DROP COLUMN nome_mae, DROP COLUMN nome_pai;
```

---

### Realizando consultas com JOIN utilizando PostgreSQL e pgAdmin 4 (

---

### Passo a Passo

#### **Passo 1: Revisão da Estrutura Após a Normalização**

Com a normalização realizada na atividade anterior, você agora tem três tabelas principais:
1. **`escola_alunos`**: Contém os dados principais dos alunos, como `id`, `nome_completo`, `data_nascimento`, `etapa`, e as chaves estrangeiras para `escolas` e `familia`.
2. **`escolas`**: Armazena os dados sobre as escolas, como `codigo_censo`, `nome_escola`, e `municipio`.
3. **`familia`**: Armazena os nomes dos pais, associando um `id_familia` único para cada conjunto de nomes de mãe e pai.

---

### Parte 1: Consultas com `JOIN`

Agora que temos as tabelas normalizadas, vamos fazer consultas que combinem os dados entre as tabelas usando **`JOIN`**.

#### **Exemplo de Consulta com `INNER JOIN`**

Vamos listar o nome completo dos alunos, o nome da escola, o município, e o nome dos pais. Para isso, vamos relacionar as tabelas `escola_alunos`, `escolas`, e `familia`.

1. **Consulta com `INNER JOIN`** entre `escola_alunos`, `escolas`, e `familia`:

```sql
SELECT 
    ea.nome_completo AS Aluno,
    e.nome_escola AS Escola,
    e.municipio AS Municipio,
    f.nome_mae AS Mae,
    f.nome_pai AS Pai
FROM 
    escola_alunos ea
INNER JOIN 
    escolas e ON ea.codigo_censo = e.codigo_censo
INNER JOIN 
    familia f ON ea.id_familia = f.id_familia;
```

Neste **`JOIN`**:
- **`INNER JOIN escolas`**: Relaciona a tabela `escola_alunos` com a tabela `escolas` através da coluna `codigo_censo`.
- **`INNER JOIN familia`**: Relaciona a tabela `escola_alunos` com a tabela `familia` através da coluna `id_familia`.

**Resultado Esperado**:
- A consulta retornará uma lista com os alunos, o nome da escola onde estudam, o município da escola e os nomes dos pais.

#### **Exemplo de Consulta Filtrada**

Agora, vamos filtrar os alunos que estudam em uma escola específica e exibir suas informações.

2. **Consulta com `JOIN` filtrando por nome da escola**:

```sql
SELECT 
    ea.nome_completo AS Aluno,
    e.nome_escola AS Escola,
    e.municipio AS Municipio,
    f.nome_mae AS Mae,
    f.nome_pai AS Pai
FROM 
    escola_alunos ea
INNER JOIN 
    escolas e ON ea.codigo_censo = e.codigo_censo
INNER JOIN 
    familia f ON ea.id_familia = f.id_familia
WHERE 
    e.nome_escola = 'Escola Municipal A';
```

**Resultado Esperado**:
- A consulta retornará todos os alunos que estudam na **Escola Municipal A** e trará suas informações familiares.

---

### Parte 2: Desafio (Opcional)

Agora que você aprendeu a realizar consultas com `JOIN`, aqui está um desafio para você:

1. **Desafio 1**: Faça uma consulta para listar os alunos que nasceram após o ano 2005, exibindo também o nome da escola e o nome do município.

```sql
SELECT 
    ea.nome_completo AS Aluno,
    e.nome_escola AS Escola,
    e.municipio AS Municipio
FROM 
    escola_alunos ea
INNER JOIN 
    escolas e ON ea.codigo_censo = e.codigo_censo
WHERE 
    ea.data_nascimento > '2005-01-01';
```

2. **Desafio 2**: Modifique a consulta anterior para listar os alunos de uma escola específica, usando o nome do município como critério de filtro.

```sql
SELECT 
    ea.nome_completo AS Aluno,
    e.nome_escola AS Escola,
    e.municipio AS Municipio
FROM 
    escola_alunos ea
INNER JOIN 
    escolas e ON ea.codigo_censo = e.codigo_censo
WHERE 
    e.municipio = 'São Paulo';
```
