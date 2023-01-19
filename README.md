# Projeto: Fome Zero
Dataset Zomato: [Zomato Restaurants](https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset?resource=download&select=zomato.csv)

## 1. Problema de negócio

Você acaba de ser contratado como Cientista de Dados da empresa
Fome Zero, e a sua principal tarefa nesse momento é ajudar o CEO Kleiton Guerra
a identificar pontos chaves da empresa, respondendo às perguntas que ele fizer
utilizando dados!

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core
business é facilitar o encontro e negociações de clientes e restaurantes. Os
restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza
informações como endereço, tipo de culinária servida, se possui reservas, se faz
entregas e também uma nota de avaliação dos serviços e produtos do restaurante,
dentre outras informações.

### Visão Geral

1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

### Visão Países

1. Quantidade de restaurantes registrados por país?
2. Quantidade de cidades registradas por país?
3. Média de avaliações feitas por país?
4. Média de preço de um prato para duas pessoas por país?

### Visão Cidades

1. Top 10 cidades com mais restaurantes na base de dados
2. Top 7 restaurantes com nota média acima de 4?
3. Top 7 restaurantes nota média abaixo de 2.5?
4. Top 10 cidades com mais restaurantes com tipos culinários distintos

### Visão Culinárias

1. Melhores restaurantes com os principais tipos culinários:
    1. Americano, Outros, Japonês, Koreano, Latino Americano
2. Top 10 melhores culinárias
3. Top 10 piores culinárias

## 2. Premissas do negócio

1. Conversão dos valores monetários foram convertidos para dólar, a fim de obter um valor padronizado.
2. Marketplace foi o modelo de negócio assumido
3. As 3 principais visões do negócio foram: Visão País, Visão Cidades, Visão Culinárias

## 3. Estratégia da solução

O painel estratégico foi desenvolvido utilizando as métrica que refletem as 4 principais visões do modelo de negócio da empresa

1. Visão geral
2. Visão por países
3. Visão por cidade 
4. Visão por culinária

Cada visão é representada pelo seguinte conjunto de métricas:

### Visão geral

1. Quantos restaurantes únicos estão registrados
2. Quantos restaurantes únicos estão registrados?
3. Quantos países únicos estão registrados?
4. Quantas cidades únicas estão registradas?
5. Qual o total de avaliações feitas?
6. Qual o total de tipos de culinária registrados?

### Visão países

1. Quantidade de restaurantes registrados por país
2. Quantidade de cidades registradas por pais
3. Média de avaliações feitas por país
4. Média de preço de um prato para duas pessoas por país

### Visão cidades

1. Top 10 cidades com mais restaurantes na base de dados
2. Top 7 cidades com restaurantes com média de avaliação acima de 4
3. Top 7 cidades com restaurantes com média de avaliação abaixo de 2.5
4. Top 10 cidades  com mais restaurantes com tipos de culinárias distintas

### Visão culinária

1. Melhores restaurantes dos principais tipos culinários
2. Top 10 restaurantes
3. Top 10 melhores tipos de culinárias
4. Top 10 piores tipos de culinárias

## 4. Top 3 Insights

1. A média de preço para duas pessoas em Singapura é quase 20x a média de preço na ìndia
2. Dos 80 restaurantes em Singapura, todos se concentram em uma cidade.
3. Apesar de possuir a maior quantidade de avaliações, a Índia lidera o rank de piores restaurantes

## 5. O produto final

Painel online hospedada em uma Cloud e disponível para acesso em qualquer dispositivo conectado a internet.
O painel pode ser acessado através do link: [Dashboard - Fome Zero](https://garritanoo-fome-zero.streamlit.app/)

## 6. Conclusão

O objetivo desse projeto foi criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.

Dentre as quatro visões o que podemos destacar é que Singapura, apesar de conter poucos restaurantes, possui boas avaliações e uma distinção culinária ampla.
