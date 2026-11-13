# Webots — Robótica Inteligente

Projeto desenvolvido durante meus estudos de **Robótica Inteligente**, utilizando o simulador Webots da Cyberbotics.

O objetivo é aprender os fundamentos de simulação robótica, construção de ambientes, propriedades físicas, sensores e programação de robôs utilizando Python.

## 🛠️ Tecnologias utilizadas

- **Webots R2025a:** ambiente de simulação robótica.
- **Python:** desenvolvimento dos controladores dos robôs.
- **e-Puck:** robô móvel educacional utilizado nos experimentos.

## 📁 Estrutura do projeto

```text
Webots/
│
├── controllers/
│   └── epuck_go_forward/
│       └── epuck_go_forward.py
│
├── worlds/
│   ├── first_simulation.wbt
│   ├── obstacles.wbt
│   ├── appearance.wbt
│   └── red_brick_wall.jpg

```

## 🤖 Simulações desenvolvidas

### 1. First Simulation

Primeiro ambiente de simulação, contendo o robô e-Puck e objetos distribuídos pelo cenário.

- Inserção do robô e-Puck.
- Adição de caixas de madeira.
- Primeiro contato com a movimentação robótica.
- Implementação de um controlador em Python.

### 2. Obstacles

Construção de um ambiente com obstáculos e objetos físicos.

- Criação de esferas utilizando `Solid` e `Shape`.
- Configuração de propriedades físicas (`Physics`).
- Configuração de colisões (`boundingObject`).
- Construção de quatro paredes utilizando `Box`.
- Aplicação dos conceitos `DEF` e `USE` para reutilização de objetos.

### 3. Appearance

Personalização visual dos objetos da simulação.

- Configuração de materiais utilizando `PBRAppearance`.
- Alteração de cores e propriedades dos materiais.
- Aplicação de texturas utilizando `ImageTexture`.
- Reutilização de aparências através de `DEF` e `USE`.

## 🐍 Controlador Python

O projeto possui um controlador chamado `epuck_go_forward.py`, responsável por movimentar o robô e-Puck para frente.

O código utiliza a API de controladores do Webots para acessar os motores das rodas e definir suas velocidades.

Principais conceitos aplicados:
- Inicialização do robô.
- Acesso aos motores através de `getDevice()`.
- Configuração dos motores para controle de velocidade.
- Execução contínua da simulação utilizando `robot.step()`.

## ▶️ Como executar

1. Instale o [Webots](https://cyberbotics.com/).
2. Clone ou baixe este repositório.
3. Abra o Webots.
4. Abra um dos arquivos `.wbt` disponíveis na pasta `worlds`.
5. Clique em Play para iniciar a simulação.

Para executar o controlador Python, abra o mundo `first_simulation.wbt`, que já possui o controlador `epuck_go_forward` associado ao robô.

## 📚 Referência

Documentação oficial: [Cyberbotics — Webots](https://cyberbotics.com/doc/guide/index)

Projeto desenvolvido para fins educacionais e aprendizado de robótica, simulação física e programação de robôs.
