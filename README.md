# ***Projeto Game: Dona da Lua***
 
![Banner Dono da Lua](https://i.imgur.com/NXIbceV.png)

<p align="center">
    <img src="https://img.shields.io/github/issues-pr-raw/claraabk/projetoIP">
    <img src="https://img.shields.io/github/issues-pr-closed-raw/claraabk/projetoIP">
    <img src="https://img.shields.io/github/issues/claraabk/projetoIP">
    <img src="https://img.shields.io/github/issues-closed-raw/claraabk/projetoIP">
    <img src="https://img.shields.io/github/license/claraabk/projetoIP">
    <img src="https://img.shields.io/github/repo-size/claraabk/projetoIP">
    <img src="https://img.shields.io/github/stars/claraabk/projetoIP?style=social">
</p>


---

*Alunos:*
- Beatriz Férre
- Clara Kenderessy
- Matheus Silva
- Rafael Baltar
- Roseane Oliveira
- Samuel Marsaro

## Sinopse
O Cebolinha aprontou de novo! Dessa vez, o mestre dos planos infalíveis roubou a máquina de clonagem do Franjinha em uma tentativa desesperada de se tornar o dono da rua... Mas a Mônica não vai deixar barato! Com ajuda do Franjinha, nossa golducha favorita clonou seu coelhinho Sansão e fará de tudo para impedir o Cebolinha de roubar seu título. Ande pelo mapa, pegue os power-ups e atire nos Cebolinhas antes que eles alcancem a lua para manter a Mônica em seu pedestal!
 
</br>

## Como iniciar o Game
Caso for seja primeira vez iniciando o projeto, faça um `git clone` e siga os seguintes passos:
  - Abra o terminal e vá para a pasta deste projeto
  - Crie ou inicie sua python venv com os pacotes do `requirements.txt` instalado
  - Insira `python run.py` ou `python -m Game` para iniciar o jogo

*OS suportado: Windows*
 
</br>

## Documentação
*Estruturação de Repositório:* </br>
Fizemos uma divisão em branches para cada feature, hotfix, bugfix, ou release que fosse adicionada, 
mantendo a branch main protegida de `git push` sem revisões dos outros integrantes. O repositório também
conta com uma pasta `.github` que contém um template para a abertura de pull request para incentivar que
o integrante escreva o que ele alterou, adicionou ou removeu em seus commits.
 
*Estruturação de Código:* </br>
Dono da Lua é um jogo essencialmente orientado a objetos, pois para apressar o desenvolvimento de todos
montandos o que chamamos de GameLoop class que implementa todas as fazes do Game Loop descritas na
documentação oficial do Pygame. Desse modo, começamos a pensar em funcionalidades que iam ser
componentes, ou seja, outras classes de objetos que iam ser encaixadas no GameLoop.
 
*Estruturação de Pastas e arquivos:* </br>
o arquivo "default" de geração do jogo é o __main__.py e pastas com os componentes a serem incrementados pelas features:
 - Components:
   - spawn.py : organização em classe da geração de inimigos (Cebolinhas) e sua formatação básica para inserção no loop.
   - gamester.py : organização em classe para geração do herói (Mônica, user-guided), suas mecânicas com o sansão, e formatação básica para inclusão no loop
   - powerup.py : implementação do mecanismo de coleta dos buffs de vida, velocidade e debuff
   - background.py : geração do cenário, transformação da imagem e estrutura básica do display 
 - Assets:
   - imagens usadas como sprite e mídia
 - Sounds:
   - arquivos de BGM do jogo
 
*Ferramentas & Bibliotecas:* </br>
- Bibliotecas:
  - pygame : usado pra importar configurações próprias de jogo
- Módulos Nativos do Python:
  - sys : usado pra oportunizar o exit
  - random : usada pra spawnar buffs em intervalos aleatórios e com efeitos distintos
 
*Divisão básica do trabalho:* </br>
- Mecânicas da Mônica e dos tiros: Samuel, Clara
- Integração de códigos: Matheus 
- Sistema de coleta de buffs: Rafael e Roseane
- Sistema de spawning e mecânicas de buffs: Beatriz
- Sistema de spawning e mecânicas de Cebolinha: Roseane
- Arte do background e implementação de sprites: Clara e Matheus
- Slides: Clara
- Relatório: Beatriz e Matheus
 
*Conceitos apresentados na disciplina que foram aplicados:* </br>
- Listas: geração de Cebolinhas no spawn.py, geração de Sansão no gamester.py
- Tuplas: identificação de coordenadas para implementação de coleta no powerup.py
- Orientação a Objetos: estruturação completa dos componentes do jogo (presente em todos os subcódigos)
- Condicionais: essencial na colisão dos elementos e regras do jogo
- Laços: o jogo ocorre dentro de um `while True:`
 
*Desafios & Lições:* </br>
Desafios:
- Lidar com divergências de código e programação em paralelo;
- Estudar P.O.O on-demand;
- Implementar um módulo novo (pygame);
- Aprender a utilizar a ferramenta Git e GitHub.
 
*Lições:*
- Adaptação ao ritmo on-demand de aprendizagem e implementação;
- Conhecimento de P.O.O adquirido;
- Modularizar é sempre melhor!

---
<p align="center">
    made with <\> and <3 by Ratos do CIn
</p>

---
