# ***Projeto Game: Dona da Lua***

![Banner Dono da Lua](https://i.imgur.com/NXIbceV.png)

*Alunos:*
- Clara Kenderessy
- Matheus Silva
- Samuel Marsaro
- Roseane Oliveira
- Rafael Baltar
- Beatriz Férre

## Como iniciar o Game
---
Caso for a primeira vez iniciando o projeto, faça um `git clone` siga os seguintes passos:
  - Abra o terminal e vá para a pasta deste projeto.
  - Crie ou inicie sua python venv com os pacotes do `requirements.txt` instalado
  - Insira `python run.py` ou `python -m Game` para inciar o jogo

## Documentação
---
*Estruturação de Repositório:*
Fizemos uma divisão em branches para cada feature, hotfix, bugfix, release que fosse adicionada, 
mantendo a branch main protegida de `git push` sem revisões dos outros integrantes. O repositório também
conta com uma pasta `.github` que contém um template de para abertura de pull request para incetivar que
o integrante escreva o que ele alterou, adicionou ou removeu em seus commits.

*Estruturação de Código:*
Dono da Lua é um jogo essencialmente orientado a objetos, pois para apressar o desenvolvimento de todos
montandos o que chamamos de GameLoop class que implementa todas as fazes do Game Loop descritas na
documentação oficial do Pygame. Desse modo, começamos a pensar em funcionalidades que iam ser
componentes, ou seja, outras classes de objetos que iam ser encaixadas no GameLoop.

*Estruturação de Pastas e arquivos:*
o arquivo "default" de geração do jogo é o __main__.py e pastas com os componentes a serem incrementados pelas features:
 - Components:
   - spawn.py : organização em classe da geração de inimigos (Cebolinhas) e sua formatação básica para inserção no loop.
   - gamester.py : organização em classe para geração do herói (Mônica, user-guided), suas mecânicas com o sansão, e formatação básica para inclusão no loop
   - powerup.py : implementação do mecanismo de coleta dos buffs
   - background.py : 
 - Assets:
   - imagens usadas como sprite e mídia
 - Sounds:
   - arquivos de BGM do jogo

*Ferramentas & Bibliotecas:*
- Bibliotecas:
  - random = usada pra spawnar buffs em intervalos aleatórios e com efeitos distintos
- Módulos:
  - sys : usado para oportunizar o exit
  - pygame : usado 
  - pygame-menu : usado

*Divisão básica do trabalho:*
- Mecânicas da Mônica e dos tiros: Samuel, Clara
- Integração de códigos: Matheus 
- Sistema de coleta de buffs: Rafael
- Sistema de spawning e mecânicas de buffs: Beatriz, Roseane
- Sistema de spawning e mecânicas de Cebolinha: Roseane
- Background e implementação de sprites: Clara e Matheus
- Slides: Clara

*Conceitos apresentados na disciplina que foram aplicados:*

*Desafios & Lições:*
