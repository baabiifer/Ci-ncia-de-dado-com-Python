# ETL com Python – Santander Dev Week 

## 📌 Contexto
Este projeto foi desenvolvido como parte de um desafio prático de Ciência de Dados
com foco na construção de um pipeline ETL em Python.

Durante o desenvolvimento, a API originalmente proposta no desafio estava
indisponível. Diante disso, foi adotada uma abordagem alternativa utilizando
arquivos CSV como fonte de dados, simulando uma decisão comum em ambientes reais.

## 🎯 Objetivo
Demonstrar domínio do fluxo ETL (Extração, Transformação e Carregamento),
boas práticas de organização de código e aplicação de regras de negócio.

## 🧱 Arquitetura do Pipeline
- **Extração**: Leitura de dados estruturados a partir de arquivo CSV  
- **Transformação**:
  - Classificação de clientes por perfil financeiro
  - Geração de mensagens personalizadas
  - Registro da data de processamento
- **Carregamento**: Persistência dos dados processados em novo arquivo CSV

## 🛠️ Tecnologias Utilizadas
- Python 3
- Pandas

## 📂 Estrutura do Projeto
