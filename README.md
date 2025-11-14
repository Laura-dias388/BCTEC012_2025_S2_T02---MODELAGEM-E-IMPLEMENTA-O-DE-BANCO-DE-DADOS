# 📚 Bacharelado em Ciência e Tecnologia (BCTec)  
## Disciplina: Modelagem e Implementação de Banco de Dados  
**Professor:** Fischer Ferreira

---

## 🗂️ Sobre o Trabalho  
Este repositório contém a implementação do **Trabalho Prático 3**, cujo objetivo é modelar uma rodada do **Brasileirão Série A**, gerar dados aleatórios de gols utilizando Python e preencher estatísticas das partidas em um banco de dados.

O projeto envolve conceitos de **modelagem de banco de dados**, **persistência de dados**, **automação com Python** e posterior uso em **Java** dentro da disciplina.

---

## 🏆 Objetivo Geral  
Modelar, registrar e computar automaticamente dados de uma rodada completa do Brasileirão Série A, incluindo:

- Criação da tabela de partidas  
- Inserção dos times da rodada  
- Sorteio de gols com Python  
- Geração de estatísticas dentro de intervalos de tempo  
- Armazenamento completo no banco de dados  

---

## 🏟️ 1️⃣ Modelagem do Banco de Dados

Crie uma tabela chamada **`partida`** para armazenar as partidas da rodada.

### 📋 Estrutura da Tabela `partida`
- `id` — Identificador único  
- `time_casa` — Nome do time mandante  
- `gols_casa` — Gols do time da casa  
- `time_visitante` — Nome do time visitante  
- `gols_visitante` — Gols do time visitante  

### 📌 Inserção Inicial — Partidas da Rodada

| Time da Casa      | Gols | Time Visitante | Gols |
|-------------------|------|----------------|------|
| Botafogo          | 0    | Palmeiras      | 0    |
| Fortaleza         | 0    | Flamengo       | 0    |
| Vitória           | 0    | Internacional  | 0    |
| São Paulo         | 0    | Cruzeiro       | 0    |
| Bahia             | 0    | Corinthians    | 0    |
| Vasco da Gama     | 0    | Atlético-MG    | 0    |
| Grêmio            | 0    | Fluminense     | 0    |
| Athletico-PR      | 0    | Juventude      | 0    |

Esses valores devem ser inseridos inicialmente com **0 gols** para todos os times.

---

## 🎯 2️⃣ Sorteio de Gols usando Python

Após montar o banco, desenvolva um script em Python que gere gols aleatórios (0 a 7) para cada time.

O script deve realizar **UPDATE** na tabela `partida`, alterando:

- `gols_casa`  
- `gols_visitante`  

de acordo com os valores sorteados.

---

## 📊 3️⃣ Estatísticas das Partidas (Tabela 2)

A rodada deve registrar estatísticas a cada **10 minutos**, dentro dos seguintes intervalos:

- 0 a 10 min  
- 11 a 20 min  
- 21 a 30 min  
- 31 a 40 min  
- 41 a 50 min  
- 51 a 60 min  
- 61 a 70 min  
- 71 a 80 min  
- 81 a 90 min  

---

## 📌 Estatísticas sorteadas por intervalo

| Estatística        | Casa | Visitante | Faixa |
|--------------------|------|-----------|--------|
| Cartões amarelos   | ✔    | ✔         | 0–5    |
| Cartões vermelhos  | ✔    | ✔         | 0–3    |
| Faltas             | ✔    | ✔         | 0–58   |
| Escanteios         | ✔    | ✔         | 0–10   |
| Impedimentos       | ✔    | ✔         | 0–30   |

---

## 🗃️ Tabela sugerida: `estatisticas`

### Campos recomendados:

- `id`  
- `partida_id` (FK → partida.id)  
- `intervalo_tempo`  
- `ca_amarelos`  
- `cv_amarelos`  
- `ca_vermelhos`  
- `cv_vermelhos`  
- `ca_faltas`  
- `cv_faltas`  
- `ca_escanteios`  
- `cv_escanteios`  
- `ca_impedimentos`  
- `cv_impedimentos`  

Cada valor deve ser sorteado usando `random.randrange()` conforme os limites da tabela.

