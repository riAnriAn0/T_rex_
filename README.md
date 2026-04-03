# T-Rex Game (Pygame)

Projeto simples em Python usando Pygame, inspirado no jogo do dinossauro do navegador.
O objetivo e controlar o Dino, desviar dos obstaculos e sobreviver o maior tempo possivel.

## Tecnologias

- Python 3
- Pygame

## Como clonar o projeto (GitHub)

1. Abra o terminal.
2. Execute:

```bash
git clone https://github.com/riAnriAn0/T_rex_.git
```

3. Entre na pasta do projeto:

```bash
cd T_rex_
```

## Como instalar e executar

1. Crie um ambiente virtual:

```bash
python -m venv venv
```

2. Ative o ambiente virtual:

Windows (PowerShell):

```bash
.\venv\Scripts\Activate.ps1
```

3. Instale as bibliotecas:

```bash
pip install -r requirements.txt
```

4. Execute o jogo:

```bash
python src/main.py
```

## Como o jogo funciona

- O Dino fica correndo automaticamente.
- Obstaculos (como cactos e aves) aparecem durante a partida.
- O jogador deve pular ou se abaixar para desviar.
- A dificuldade aumenta com o tempo.
- Quando ocorre colisao, aparece a tela de fim de jogo e voce pode reiniciar.

## Estrutura basica

- `src/main.py`: loop principal do jogo.
- `src/Class/`: classes dos elementos do jogo (Dino, Cacto, Aves, Chao, Nuvem, Over, Text).
- `src/img/`: sprites e imagens.
- `src/audio/`: efeitos sonoros.
- `src/fonts/`: fontes do projeto.

## Requisitos

- Python 3.10+ (recomendado)
- Dependencias listadas em `requirements.txt`
