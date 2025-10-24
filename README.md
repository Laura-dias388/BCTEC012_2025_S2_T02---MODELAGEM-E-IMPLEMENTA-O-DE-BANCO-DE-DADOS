# 📚 Bacharelado em Ciência e Tecnologia (BCTec)  
## Disciplina: Modelagem e Implementação de Banco de Dados  
**Professor:** Fischer Ferreira  

# 🌾 Módulo 3 — Aula Prática 2   
**Universidade Federal de Itajubá (UNIFEI)**   
 
---

## 🧠 Descrição

Este projeto tem como objetivo **inserir informações em uma base de dados utilizando Python**, simulando o comportamento da **produtividade agrícola em função da quantidade de fertilizante aplicado**.  

A produtividade segue uma **curva parabólica**, modelada por uma **equação do segundo grau** da forma:

\[
P(x) = ax^2 + bx + c
\]

onde:
- **P(x)** → produtividade (toneladas por hectare)  
- **x** → quantidade de fertilizante (kg/ha)  
- **a, b, c** → coeficientes que determinam a forma da curva  

O desafio consiste em **analisar 10 diferentes equações** e determinar **qual delas apresenta a maior produtividade máxima**, considerando uma faixa sustentável de fertilizante entre **20 e 80 kg/ha**.

---

## 🎯 Objetivos

1. Calcular a produtividade para valores de `x` entre 0 e 80 kg/ha.  
2. Armazenar as coordenadas `(x, y)` no banco de dados `plantacao_agricola`.  
3. Ler os dados da base e plotar as curvas utilizando `matplotlib`.  
4. Identificar:
   - A equação que alcança a **maior produtividade máxima**;
   - A posição do **vértice** da parábola (idealmente entre 20 e 80 kg/ha);
   - A **melhor equação** segundo os critérios definidos.

---

## 🗄️ Estrutura do Banco de Dados

Crie um banco de dados chamado `plantacao_agricola` e execute os comandos SQL abaixo:

```sql
CREATE TABLE coordenada (
  id_coordenada INT(11) NOT NULL AUTO_INCREMENT,
  numero_equacao INT(11) NOT NULL,
  coordenada_x INT(11) NOT NULL,
  coordenada_y INT(11) NOT NULL,
  PRIMARY KEY (id_coordenada)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
