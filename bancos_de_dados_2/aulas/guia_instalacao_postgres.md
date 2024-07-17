### Tutorial de Instalação e Configuração do PostgreSQL e pgAdmin no Xubuntu
![](./assets/tutorial.jpeg)
#### 1. Instalação do PostgreSQL

**Passo 1:** Adicionar o repositório do PostgreSQL

```bash
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```

**Passo 2:** Importar a chave do repositório

```bash
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```

**Passo 3:** Atualizar a lista de pacotes

```bash
sudo apt-get update
```

**Passo 4:** Instalar o PostgreSQL

```bash
sudo apt-get install postgresql postgresql-contrib
```

**Passo 5:** Verificar o status do PostgreSQL

```bash
sudo systemctl status postgresql
```

#### 2. Configuração do PostgreSQL

**Passo 1:** Acessar o PostgreSQL

```bash
sudo -i -u postgres
```

**Passo 2:** Acessar o terminal psql

```bash
psql
```

**Passo 3:** Alterar a senha do usuário 'postgres'

```sql
\password postgres
```

**Passo 4:** Sair do psql

```sql
\q
```

**Passo 5:** Sair do usuário postgres

```bash
exit
```

#### 3. Instalação do pgAdmin

**Passo 1:** Adicionar o repositório do pgAdmin

```bash
curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/ubuntu `lsb_release -cs` pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
```

**Passo 2:** Instalar o pgAdmin (modo Desktop)

```bash
sudo apt install pgadmin4-desktop
```

#### 4. Configuração de Acesso do PostgreSQL pela Rede Local

**Passo 1:** Editar o arquivo de configuração `postgresql.conf`

```bash
sudo mousepad /etc/postgresql/12/main/postgresql.conf
```

Localize a linha `listen_addresses` e modifique para permitir conexões de todas as interfaces de rede:

```plaintext
listen_addresses = '*'
```

**Passo 2:** Editar o arquivo de configuração `pg_hba.conf`

```bash
sudo mousepad /etc/postgresql/12/main/pg_hba.conf
```

Adicione a seguinte linha no final do arquivo para permitir conexões da rede local:

```plaintext
host    all             all             192.168.1.0/24          md5
```

**Passo 3:** Reiniciar o serviço PostgreSQL

```bash
sudo systemctl restart postgresql
```

**Passo 4:** Configurar o Firewall para permitir conexões no porto 5432

```bash
sudo ufw allow 5432/tcp
```

#### 5. Acesso Remoto ao PostgreSQL via pgAdmin

**Passo 1:** Abrir o pgAdmin

- No Xubuntu, você pode abrir o pgAdmin a partir do menu de aplicativos, na categoria Desenvolvimento.

**Passo 2:** Adicionar um novo servidor no pgAdmin

- Clique com o botão direito em "Servers" e selecione "Create" > "Server...".

**Passo 3:** Configurar a conexão no pgAdmin

- Na aba "General", dê um nome ao servidor.
- Na aba "Connection", preencha os campos:
  - Hostname/address: `endereço_IP_do_servidor_postgresql`
  - Port: `5432`
  - Maintenance database: `postgres`
  - Username: `postgres`
  - Password: `sua_senha`

Clique em "Save" para salvar as configurações e conectar ao servidor PostgreSQL.
