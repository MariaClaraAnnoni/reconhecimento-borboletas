# Reconhecimento de Personagens com YOLO e Segmentação de Imagens

Projeto desenvolvido para a disciplina de **Inteligência Artificial Aplicada à Análise de Imagens e Reconhecimento de Padrões**.

## Visão Geral

Este projeto tem como objetivo desenvolver um sistema capaz de detectar automaticamente personagens em imagens utilizando o modelo **YOLO (You Only Look Once)** e, posteriormente, realizar a segmentação da região de interesse (ROI) empregando técnicas clássicas de Processamento Digital de Imagens.

O sistema deverá identificar automaticamente os personagens presentes na imagem, delimitar sua localização através do modelo treinado e aplicar algoritmos de segmentação para destacar o objeto detectado em relação ao fundo.

Ao final do processamento, a aplicação apresentará:

- Imagem original;
- Região detectada pelo YOLO;
- Máscara obtida pela segmentação;
- Sobreposição (overlay) da máscara sobre a imagem original.

O projeto integra conceitos de:

- Inteligência Artificial
- Visão Computacional
- Detecção de Objetos
- Processamento Digital de Imagens
- Reconhecimento de Padrões

---

## Dataset

O projeto utiliza o dataset:

**SpongeBob, PatrickStar and Squidward Detection**

Fonte:

https://www.kaggle.com/datasets/lara311/spongebob-patrickstar-and-squidward-detection

O dataset contém imagens anotadas para treinamento de modelos de detecção de objetos utilizando o formato YOLO, permitindo identificar automaticamente três personagens:

- SpongeBob
- Patrick Star
- Squidward

As anotações serão utilizadas exclusivamente para o treinamento do modelo de detecção. A segmentação das imagens será implementada durante o projeto utilizando técnicas desenvolvidas ao longo da disciplina. :contentReference[oaicite:0]{index=0}

---

## Estrutura do Projeto

```text
reconhecimento-borboletas/
│
├── data/
│   └── dataset/
│
├── src/
│   ├── train.py
│   ├── detect.py
│   ├── segmentation.py
│   ├── visualization.py
│   └── utils.py
│
├── interface/
│   └── app.py
│
├── outputs/
│   ├── detections/
│   ├── masks/
│   └── overlays/
│
├── download_dataset.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/ai-squarepants.git
cd ai-squarepants
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente.

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Configuração do Kaggle

O download do dataset é realizado automaticamente utilizando a CLI oficial do Kaggle.

Após instalar as dependências:

```bash
kaggle auth login
```

Depois de autenticar sua conta:

```bash
python download_dataset.py
```

O dataset será armazenado em:

```text
data/dataset/
```

---

## Pipeline do Projeto

O sistema seguirá as seguintes etapas:

```text
Imagem
      │
      ▼
YOLO
      │
      ▼
Detecção do personagem
      │
      ▼
Extração da ROI
      │
      ▼
Pré-processamento
      │
      ▼
Segmentação
      │
      ▼
Operações Morfológicas
      │
      ▼
Máscara
      │
      ▼
Overlay
```

---

## Segmentação

Após a detecção realizada pelo YOLO, serão aplicadas técnicas clássicas de processamento de imagens para segmentar o personagem detectado.

Entre as técnicas previstas estão:

- Conversão para escala de cinza;
- Filtragem Gaussiana;
- Limiarização automática (Método de Otsu);
- Operações morfológicas;
- Extração da região de interesse (ROI).

---

## Interface

A interface deverá apresentar:

```text
┌──────────────┬──────────────┬──────────────┐
│   Original   │  Segmentação │   Overlay    │
└──────────────┴──────────────┴──────────────┘
```

Permitindo visualizar todas as etapas do processamento.

---

## Objetivos

### Etapa 1

- [x] Escolha do dataset
- [ ] Download automatizado
- [ ] Treinamento do YOLO

### Etapa 2

- [ ] Implementação do pré-processamento
- [ ] Segmentação utilizando técnicas estudadas em aula
- [ ] Geração das máscaras

### Etapa 3

- [ ] Interface gráfica
- [ ] Visualização dos resultados
- [ ] Avaliação do sistema

---

## Tecnologias Utilizadas

- Python
- OpenCV
- Ultralytics YOLO
- NumPy
- Matplotlib
- Kaggle CLI

---

## Resultados Esperados

Ao final do projeto espera-se obter um sistema capaz de:

- Detectar automaticamente os personagens presentes na imagem;
- Delimitar corretamente a região de interesse;
- Segmentar o objeto detectado;
- Exibir a máscara gerada;
- Sobrepor a segmentação à imagem original;
- Demonstrar a integração entre técnicas de Inteligência Artificial e Processamento Digital de Imagens.

---

## Licença

Projeto desenvolvido exclusivamente para fins acadêmicos na disciplina de Inteligência Artificial Aplicada à Análise de Imagens e Reconhecimento de Padrões.
