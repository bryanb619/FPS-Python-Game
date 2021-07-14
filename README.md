<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
</head>
<body>

<h1><center>Relatório do Projecto Final [Recurso] </center></h1>

<h2><center> Introdução à Matemática e Física Para Videojogos I </center></h2>  

<center><p><img src="https://i.ibb.co/ZVnHHPH/unknown.png" width="650"  /></p></center>

<h4><center>Projecto de Recurso IMFJ1 "FPS-Like" </center></h4>


<center>Versão # 1.0</center>

<center>Terça, Julho 13, 2021</center>

<div style="page-break-after:always"></div>


<h2>Tabela de Conteúdos</h2>

<ol>
<li><a href="#informaçãobase">Informação Base</a></li>
<li><a href="#sumario">Sumário do Projecto</a>
<li><a href="#movimentos">Movimentos & Rotação do Jogador</a>
<li><a href="#cenario">Cenário e Implementação 3D</a>
<li><a href="#configuraçoes">Configurações do Jogo</a></li>
<li><a href="#contribuiçoes">Contribuições individuais</a></li>
</ol></li>


<div style="page-break-after: always"></div>


<h3>1. Informação Base <a name="informaçãobase"></a></h3>

<p> 

**Nome do Projecto**

Projecto de Recurso IMFJ1 "FPS-Like"


**Membros do Projecto**

Rafaela Henriques 22005252
`Github Username: rafaelahenriques`

Sónia Raposo 22000344
`Github Username Sonia-Raposo `

Steven Hall 22001753
`Github Username: bryanb619`


**Data de Completação do Projecto**

13.07.2021

 </p>
 

<h3>2. Sumário do Projecto <a name="sumario"></a></h3>

<p>
Este projecto consiste na construção de um ambiente "FPS-Like" 3D que consiste num mapa com paredes e objectos 3D onde é possivel controlar um jogador em primeira pessoa.

O jogador consegue movimentar-se para todas as direcções, rodar a câmara de visão e correr, utilizando as teclas respectivas:

**Controlos básicos**
* **Frente:** Tecla W
* **Trás:** Tecla S
* **Esquerda:** Tecla A
* **Direita:** Tecla D

**Controlos Câmara**
* **Rodar Câmara para esquerda:** Seta Esquerda
* **Rodar Câmara para direita:** Seta Direita

**Controlos avançados**
* **Sprint:** Tecla Shift + W

**Sair do Jogo**
* **Exit:** Tecla Esc

</p>


<p>

<h3>3. Movimentos & Rotação do Jogador <a name="movimentos"></a></h3>

Para a criação do jogador foi criado um ficheiro ***py: PlayerScript***. 
É neste ficheiro que foi criada uma classe onde foi definida a sua posição em x e y e o seu ângulo.

Foi então criada uma função movimento onde é utilizada a biblioteca **math** para definir o sin e cos do movimento do jogador.

Após isso, foram então definidas as Teclas do teclado que permitem controlar e movimentar o jogador, sendo:

**Controlos básicos**
* **Frente:** Tecla W
* **Trás:** Tecla S
* **Esquerda:** Tecla A
* **Direita:** Tecla D

**Controlos Câmara**
* **Rodar Câmara para esquerda:** Seta Esquerda
* **Rodar Câmara para esquerda:** Seta Direita

**Controlos avançados**
* **Sprint:** Tecla Shift + WS

Foram definidos também os controlos de rato para movimentar o jogador:

**Controlos básicos**
* **Direcções:** Movimento com o rato

 </p>

 <p>

<h3>4. Cenário e Implementação 3D <a name="cenario"></a></h3>


Para a criação do mapa foi criado um ficheiro ***py: Map***. O tipo de mapa criado é um **text_map** em 2D para a contrução do mesmo foi utilizada a letra **I**.

Para criar o mapa em si, são detectadas as letras **I** através de uma *função if* que transforma a letra numa parede.

Sendo assim, foram criados os limites do mapa, colocando **I** nos cantos superior, inferior e lateral no **text_map**, e colocadas paredes dentro do mapa, intercalando com "." que representa espaço vazio.

Para transformar este mapa 2D numa vista 3D, é utilizada a fórmula que se encontra no ficheiro ***py: AppSettings***:

Multiplicamos ainda distancia por 3, para optimizar a escala
Isso faz com que o escala do cenário seja "aumentada"

`proj_3d = 3 * dist * walls`

Sendo que a multiplicação por da distância por 3 serve para projectar e optimizar a escala tornando assim a vista e a navegação pelo mapa de forma mais agradável para o jogador devido à escala mais realista. 

</p>

<p>

<h3>5. Configurações do Jogo <a name="configuraçoes"></a></h3>

Para definir as configurações do jogo, foi criado um ficheiro ***py: AppSettings***.

É neste ficheiro que são definidas as configurações tais como:

**Configurações de ecrã**
* Largura e Altura da tela de jogo
* FPS (Valor Limite de Frames por Second)

**Configurações Ray Casting**
* Ponto de Vista
* Número de raios
* Dimensão
* Distância
* Projecção 3D
* Ângulo
* Escala

**Configurações de cores do jogo**
* Lista de cores em código RGB usadas no jogo

</p>


<h3>6.Contribuições individuais <a name="contribuiçoes"></a></h3>

**Rafaela Henriques**
* Organização e correções de código
* Criação do ficheiro ***Map***
* Criação do ficheiro ***AppSettings***
* Configurações de mapa
* Realização do ficheiro ***Postmortem***

**Sónia Raposo**
* Organização e correções de código
* Criação do ficheiro ***PlayScript***
* Criação do ficheiro ***Main***
* Configurações ecrã
* Movimentos básicos do jogador
* Realização do ficheiro ***readme***

**Steven Hall**
* Organização e correções de código
* Configurações Base
* Criação do ficheiro ***Ray***
* Configurações dos Visuais do Jogo em 3D
* Movimentos especiais do jogador (Sprint e Salto)
* Configurações de Cores no Mapa