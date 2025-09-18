# 📚 Bacharelado em Ciência e Tecnologia (BCTec)  
## Disciplina: Modelagem e Implementação de Banco de Dados  
**Professor:** Fischer Ferreira  

---
# 📂 Branch: python-db-connection

Esta branch tem como objetivo implementar e testar a conexão do **Python** com o banco de dados.  
Aqui serão adicionados os scripts e configurações necessários para estabelecer a comunicação segura e eficiente entre a aplicação e o banco.

---

## 🚀 Objetivo
- Configurar a conexão entre Python e o banco de dados.
- Criar funções básicas de consulta, inserção, atualização e exclusão.
- Garantir boas práticas de segurança (uso de variáveis de ambiente para credenciais).
- Estruturar um modelo inicial para futuras implementações.

---

# CRUD - Create, Read, Update, Delete

CRUD é o acrônimo de quatro operações fundamentais usadas em sistemas de banco de dados e em aplicações que manipulam informações.  
Essas operações são **Criar, Ler, Atualizar e Deletar** registros.

---

## 🔹 Operações CRUD

### 1. Create (Criar)
- Responsável por **inserir novos dados** no sistema/banco de dados.
- Exemplo em SQL:
  ```sql
  INSERT INTO usuarios (nome, email) VALUES ('Jhon', 'jhon@email.com');


## 🛠️ Tecnologias utilizadas
- **Python 3.x**
- **MariaDB / MySQL** (ajuste conforme o banco que estiver usando)
- Biblioteca: `mysql-connector-python` ou `pymysql`

---

## 📦 Como rodar o projeto

1. Clone o repositório e acesse a branch:
   ```bash
   git checkout python-db-connection
