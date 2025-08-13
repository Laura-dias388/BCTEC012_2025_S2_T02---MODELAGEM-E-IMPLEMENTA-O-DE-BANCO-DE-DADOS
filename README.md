# 📚 Bacharelado em Ciência e Tecnologia (BCTec)  
## Disciplina: Modelagem e Implementação de Banco de Dados  
**Professor:** Fischer Ferreira  

---

## 🗂️ Sobre o Repositório
Este repositório reúne anotações, exercícios, exemplos e projetos desenvolvidos durante a disciplina **Modelagem e Implementação de Banco de Dados** no curso de **Bacharelado em Ciência e Tecnologia (BCTec)**.  
O objetivo é registrar todo o conteúdo visto em aula, incluindo conceitos teóricos, práticas com SGBDs e exemplos de aplicações reais.

---

## 📖 Conteúdo do Módulo 1 — Introdução a Banco de Dados

### 1️⃣ Conceitos Iniciais
- O que é um **banco de dados**.
- Diferença entre armazenar dados em arquivos comuns e utilizar um **SGBD**.
- Motivação para estudar bancos de dados.

### 2️⃣ Problemas na Manipulação Direta de Dados
- **Inconsistência de dados**: formatos não respeitados.
- **Redundância de dados**: duplicação desnecessária.
- **Falta de controle de concorrência**: alterações simultâneas.
- **Dificuldade de segurança e privacidade**.
- **Integridade dos dados**: restrições, valores únicos, sem valores nulos.
- **Manutenção complexa** e dificuldade em **backup e recuperação**.

### 3️⃣ Solução: Sistema Gerenciador de Banco de Dados (SGBD)
- Coleção de programas que permite criar, manter e manipular um banco de dados.
- Características:
  - Controle de redundância
  - Compartilhamento multiusuário
  - Controle de acesso
  - Representação de relacionamentos complexos
  - Tolerância a falhas e recuperação
- Exemplos de SGBD:
  - **Relacionais (SQL)**: MySQL, PostgreSQL, Oracle.
  - **NoSQL**: MongoDB, Cassandra.
  - **Embarcados**: SQLite.

### 4️⃣ Quando Usar (ou Não) um SGBD
- **Não usar**:
  - Aplicações simples e estáveis.
  - Sistemas embarcados com pouco armazenamento.
  - Nenhum acesso concorrente.
- **Usar**:
  - Necessidade de múltiplos usuários.
  - Controle de integridade, segurança e concorrência.
  - Estrutura de dados complexa.

### 5️⃣ Exemplo de Aplicação de um SGBD
- **Banco de Dados: UNIVERSIDADE**
  - Registros: ALUNO, DISCIPLINA, TURMA, HISTÓRICO ESCOLAR, PRÉ-REQUISITO.
  - Relacionamentos entre registros.
  - Exemplos de consultas:
    - Listar disciplinas e notas.
    - Listar alunos que fizeram "Banco de Dados".
    - Listar pré-requisitos da disciplina.
  - Exemplos de atualizações:
    - Alterar nome de aluno.
    - Criar nova turma.
    - Inserir nota em uma disciplina.

---

## 🛠️ Tecnologias e Ferramentas
- **SGBD:** MariaDB / MySQL
- **Modelagem:** MySQL Workbench, Draw.io
- **Editor:** VS Code
- **Controle de Versão:** Git e GitHub

---

## 📂 Estrutura Sugerida do Repositório

---

## 📌 Observações
Este repositório é para **fins educacionais** e acompanha o progresso da disciplina.  
Sugestões e melhorias são bem-vindas.

---

## ✍️ Autor
**Laura Dias**  
Estudante de **Bacharelado em Ciência e Tecnologia** na **UNIFEI**  
📍 Itajubá - MG  
