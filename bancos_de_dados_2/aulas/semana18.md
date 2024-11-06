### Semana 18: Configuração de Segurança, Backup e Recuperação
![](./assets/s18.jpeg)
**Bem-vindos à Semana 18!**

Nesta semana, vamos focar em configurar a segurança do banco de dados, além de estabelecer um plano de **backup e recuperação** para proteger os dados. Essas práticas são essenciais para garantir que as informações do sistema estejam protegidas contra acessos não autorizados e sejam recuperáveis em caso de falhas ou acidentes.

---

### Objetivos da Semana

1. **Configurar a Segurança do Banco de Dados**: Implementar controles de acesso para limitar o que cada usuário pode fazer.
2. **Definir um Plano de Backup**: Criar uma rotina de backup para proteger os dados.
3. **Implementar Procedimentos de Recuperação**: Planejar como restaurar dados a partir dos backups em caso de falhas.

---

### 1. Configuração de Segurança do Banco de Dados

A segurança é uma prioridade em bancos de dados, especialmente onde há dados sensíveis. Garantir que apenas pessoas autorizadas tenham acesso é o primeiro passo para proteger o sistema. Vamos explorar como configurar permissões e criar políticas de segurança.

#### Controle de Acesso com Comandos DCL

- **GRANT**: Concede permissões específicas a um usuário, como permissão de leitura (SELECT) ou modificação (INSERT, UPDATE).
   - **Exemplo**:
   ```sql
   GRANT SELECT, INSERT ON Produtos TO usuario;
   ```

- **REVOKE**: Remove permissões de um usuário.
   - **Exemplo**:
   ```sql
   REVOKE INSERT ON Produtos FROM usuario;
   ```

Esses comandos ajudam a limitar o que cada usuário pode fazer, evitando alterações ou consultas não autorizadas.

#### Práticas de Segurança

1. **Usar Senhas Fortes**: Configure senhas complexas e atualize-as periodicamente.
2. **Criação de Papéis (Roles)**: Em vez de configurar permissões para cada usuário, crie papéis com permissões específicas e atribua os usuários a esses papéis.
3. **Monitoramento de Acesso**: Registre as atividades dos usuários no banco de dados para monitorar acessos suspeitos.

### 2. Plano de Backup

Um **backup** é uma cópia de segurança dos dados, criada para proteger contra perdas. É importante definir uma rotina de backup e escolher o tipo mais adequado.

#### Tipos de Backup

1. **Backup Completo**: Faz uma cópia de todos os dados. É mais seguro, mas também ocupa mais espaço e tempo.
   - **Quando usar**: Geralmente realizado semanalmente ou mensalmente.

2. **Backup Incremental**: Copia apenas os dados alterados desde o último backup. É mais rápido e ocupa menos espaço.
   - **Quando usar**: Ideal para backups diários.

3. **Backup Diferencial**: Copia os dados alterados desde o último backup completo. É mais fácil de restaurar que o incremental.
   - **Quando usar**: Alternativa para backups frequentes, balanceando rapidez e facilidade de restauração.

#### Definindo uma Rotina de Backup

1. **Frequência dos Backups**: Configure backups regulares. Ex.: backups completos semanalmente e incrementais diariamente.
2. **Localização dos Backups**: Armazene as cópias em locais seguros, como servidores externos ou em nuvem.
3. **Automatização**: Use ferramentas do SGBD ou scripts para automatizar o processo de backup.

### 3. Procedimentos de Recuperação

A recuperação é o processo de restaurar dados a partir de um backup. Um bom plano de recuperação ajuda a reduzir o tempo de inatividade e a evitar perda de informações.

#### Tipos de Recuperação

1. **Recuperação Completa**: Restaura todos os dados do backup completo mais recente.
2. **Recuperação Parcial**: Restaura apenas uma parte específica dos dados.
3. **Recuperação Contínua (Point-in-Time Recovery)**: Restaura os dados até um ponto específico no tempo, útil para desfazer erros recentes.

#### Teste de Recuperação

É fundamental testar regularmente o processo de recuperação para garantir que o backup pode ser restaurado com sucesso. Isso ajuda a evitar surpresas caso você precise realizar uma recuperação de emergência.

---

### Exemplo de Script de Backup no PostgreSQL

No PostgreSQL, você pode usar o comando `pg_dump` para criar um backup completo do banco de dados:

```bash
pg_dump -U usuario -F c -b -v -f "backup_banco.sql" nome_do_banco
```

- `-U usuario`: Especifica o usuário do banco.
- `-F c`: Define o formato do backup (c para custom).
- `-b`: Inclui dados em binário.
- `-v`: Mostra o progresso.
- `-f`: Define o nome do arquivo de backup.

Para restaurar o backup, use o comando `pg_restore`:

```bash
pg_restore -U usuario -d nome_do_banco "backup_banco.sql"
```

---

### Atividade da Semana (Prática com Segurança, Backup e Recuperação)

Para praticar, complete as atividades abaixo:

1. Conceda a um usuário permissão para `SELECT` e `INSERT` na tabela **Clientes** e depois revogue o `INSERT`.
2. Crie um plano de backup que inclua:
   - Backups completos uma vez por semana.
   - Backups incrementais diariamente.
3. Realize um teste de backup e recuperação usando comandos `pg_dump` e `pg_restore`.

#### Parte 1: Questões de Revisão

1. Qual é a função do comando `GRANT`?
   - a) Conceder permissões a um usuário.
   - b) Excluir dados de uma tabela.
   - c) Fazer backup dos dados.
   - d) Restaurar dados de um backup.

2. Qual tipo de backup copia todos os dados?
   - a) Incremental
   - b) Diferencial
   - c) Completo
   - d) Contínuo

3. Qual comando é usado para criar um backup no PostgreSQL?
   - a) `GRANT`
   - b) `pg_dump`
   - c) `pg_restore`
   - d) `REVOKE`

4. Qual é o objetivo de um plano de recuperação?
   - a) Melhorar a segurança do banco de dados.
   - b) Restaurar dados a partir de um backup em caso de falhas.
   - c) Configurar permissões de usuários.
   - d) Dividir os dados entre diferentes servidores.

5. Por que é importante testar o processo de recuperação?
   - a) Para excluir backups antigos.
   - b) Para garantir que o backup pode ser restaurado com sucesso.
   - c) Para atualizar permissões de acesso.
   - d) Para realizar um backup completo do banco.

---

**Gabarito**:
1. a) Conceder permissões a um usuário.
2. c) Completo
3. b) `pg_dump`
4. b) Restaurar dados a partir de um backup em caso de falhas.
5. b) Para garantir que o backup pode ser restaurado com sucesso.

---

### Conclusão

A **configuração de segurança, backup e recuperação** é uma etapa essencial para garantir a proteção e disponibilidade dos dados. Com práticas de segurança, um bom plano de backup e recuperação, você minimiza o risco de perda de dados e garante que o banco de dados esteja sempre protegido contra imprevistos.