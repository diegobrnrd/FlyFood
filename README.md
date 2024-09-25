# FlyFood
 
Projeto elaborado como componente da disciplina PISI II (Projeto Interdisciplinar de Sistemas de Informação II).

## Parte 1: Implementação do Algoritmo de Força Bruta

Nesta primeira parte do projeto, implementamos o algoritmo de força bruta para resolver o problema proposto. O desafio consiste em desenvolver um algoritmo de roteamento para drones de entrega, que deve determinar a ordem de menor custo para percorrer todos os pontos de entrega em uma cidade, partindo e retornando ao ponto de origem.

A matriz representa os pontos da cidade, e o drone só pode se mover horizontalmente ou verticalmente. Para calcular a distância entre os pontos, utilizamos a **distância de Manhattan**, que é a soma das distâncias absolutas das diferenças nas coordenadas horizontais e verticais. O objetivo é otimizar o trajeto do drone para que ele consiga concluir todas as entregas dentro do ciclo da bateria, minimizando a distância total percorrida.
