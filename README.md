# Projecto Final [Recurso]: Introdução à Matemática e Física Para Videojogos I 

 
## Autores do Projeto "FPS-Like"

### Rafaela Henriques 22005252
Github Username: rafaelahenriques

### Sónia Raposo 22000344
Github Username Sonia-Raposo 

### Steven Hall 22001753
Github Username: bryanb619

---

## Relatório do Projecto

### Movimentos & Rotação do Jogador
Para a criação do jogador foi criado um ficheiro py: *PlayerScript*. 
É neste ficheiro que foi criada uma classe onde foi definida a sua posição em x e y e o seu ângulo.

Foi então criada uma função movimento onde é utilizada a biblioteca **math** para definir o sin e cos do movimento do jogador.

Após isso, foram então definidas as Teclas do teclado que permitem controlar e movimentar o jogador, sendo:

* **Frente:** Tecla W
* **Trás:** Tecla S
* **Esquerda:** Tecla A
* **Direita:** Tecla D

E foram definidos também os controlos de rato para movimentar o jogador:

**TO FILL**



### Cenário
Para a criação do mapa foi criado um ficheiro py: *Map*. O tipo de mapa criado é um **text_map** e foi utilizada a letra I.

Para criar o mapa em si, são detectadas as letras I através de uma *função if* que transforma a letra numa parede.

Sendo assim, foram criados os limites do mapa, colocando W nos cantos superior, inferior e lateral no **text_map**, e colocadas paredes dentro do mapa, intercalando com "." que representa "espaço vazio".




### Implementação 3D


### Configurações



---
## Contribuições individuais
**Rafaela Henriques**
* Organização e correções de código
* Criação do ficheiro *Map*
* Criação do ficheiro *AppSettings*
* Configurações de mapa
* Realização do ficheiro *postmortem*

**Sónia Raposo**
* Organização e correções de código
* Criação do ficheiro *PlayScript*
* Criação do ficheiro *Main*
* Configurações ecrã
* Movimentos básicos do jogador
* Realização do ficheiro *readme*

**Steven Hall**
* Configurações Base
* Criação do ficheiro *Ray*
* Configurações dos Visuais do Jogo em 3D
* Movimentos especiais do jogador (Sprint e Salto)
* Configurações de Cores no Mapa