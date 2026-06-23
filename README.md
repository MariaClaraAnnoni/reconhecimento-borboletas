# Reconhecimento de Borboletas 🦋

Segmentação e identificação automática de regiões de interesse em imagens de borboletas utilizando técnicas de Processamento Digital de Imagens e Inteligência Artificial.

## Visão Geral

Este é um projeto desenvolvido para a disciplina de **Inteligência Artificial Aplicada à Análise de Imagens e Reconhecimento de Padrões**.

O objetivo do projeto é implementar um pipeline completo de análise de imagens capaz de identificar automaticamente a região de interesse (ROI) correspondente à borboleta presente em uma imagem.

Para isso, serão utilizadas técnicas clássicas de Processamento Digital de Imagens, incluindo pré-processamento, limiarização automática, segmentação, operações morfológicas e avaliação quantitativa dos resultados.

Ao final, o sistema deverá ser capaz de:

* Carregar imagens do dataset;
* Realizar pré-processamento;
* Segmentar automaticamente a borboleta;
* Gerar máscaras binárias da região de interesse;
* Sobrepor a segmentação à imagem original;
* Avaliar a qualidade da segmentação utilizando métricas apropriadas;
* Exibir os resultados por meio de uma interface gráfica.

O projeto foi desenvolvido como oportunidade prática de estudo em:

* Processamento Digital de Imagens
* Inteligência Artificial
* Reconhecimento de Padrões
* Segmentação de Imagens
* Extração de Região de Interesse (ROI)
* Avaliação de Algoritmos de Visão Computacional

## Dataset

O dataset utilizado é:

* Butterfly Dataset
* Fonte: Kaggle
* Imagens de diferentes espécies de borboletas em ambientes naturais

Dataset:

https://www.kaggle.com/datasets/veeralakrishna/butterfly-dataset

O dataset será utilizado para experimentação e validação das técnicas de segmentação implementadas ao longo do projeto.

## Estrutura do Projeto

```text
ButterflyROI/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── butterfly_dataset/
│
├── notebooks/
│   ├── dataset_analysis.ipynb
│   ├── preprocessing.ipynb
│   └── segmentation.ipynb
│
├── src/
│   ├── preprocessing/
│   │   ├── filters.py
│   │   └── enhancement.py
│   │
│   ├── segmentation/
│   │   ├── otsu.py
│   │   ├── morphology.py
│   │   └── roi_extraction.py
│   │
│   ├── evaluation/
│   │   ├── metrics.py
│   │   ├── iou.py
│   │   └── dice.py
│   │
│   ├── visualization/
│   │   ├── overlay.py
│   │   └── plots.py
│   │
│   └── utils.py
│
├── outputs/
│   ├── masks/
│   ├── overlays/
│   ├── reports/
│   └── figures/
│
├── interface/
│   └── app.py
│
├── download_dataset.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/ButterflyROI.git
cd ButterflyROI
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração do Kaggle

O projeto utiliza a CLI oficial do Kaggle para realizar o download automático do dataset.

Após instalar as dependências, execute:

```bash
kaggle auth login
```

Um link será exibido no terminal.

1. Abra o link no navegador;
2. Faça login na sua conta Kaggle;
3. Autorize o acesso;
4. Retorne ao terminal.

Para verificar se a autenticação foi realizada corretamente:

```bash
kaggle datasets list -s butterfly
```

## Download do Dataset

Após autenticar sua conta:

```bash
python download_dataset.py
```

O script será responsável por:

* Verificar se o dataset já existe localmente;
* Realizar o download automaticamente quando necessário;
* Extrair os arquivos;
* Organizar os dados na estrutura do projeto.

Os dados serão armazenados em:

```text
data/butterfly_dataset/
```

## Metodologia

### 1. Pré-processamento

As imagens poderão passar pelas seguintes etapas:

* Conversão para escala de cinza;
* Redução de ruído;
* Suavização com filtros Gaussianos;
* Equalização de histograma;
* Ajustes de contraste.

### 2. Segmentação

A segmentação inicial será realizada utilizando técnicas clássicas de limiarização.

#### Método de Otsu

O algoritmo de Otsu determina automaticamente um limiar capaz de separar objeto e fundo.

Fluxo esperado:

```text
Imagem RGB
      ↓
Escala de Cinza
      ↓
Gaussian Blur
      ↓
Threshold Otsu
      ↓
Máscara Binária
```

### 3. Pós-processamento

Após a segmentação poderão ser aplicadas operações morfológicas como:

* Erosão;
* Dilatação;
* Opening;
* Closing.

Objetivos:

* Remover ruídos;
* Corrigir falhas na segmentação;
* Melhorar os contornos da região de interesse.

### 4. Extração da Região de Interesse

A região segmentada será aplicada à imagem original para destacar apenas a borboleta.

Resultado esperado:

* Imagem Original;
* Máscara Binária;
* Sobreposição da Máscara (Overlay).

### 5. Avaliação

A qualidade da segmentação será analisada utilizando métricas quantitativas.

Métricas previstas:

* Intersection over Union (IoU);
* Dice Score;
* Precisão da segmentação;
* Comparação visual dos resultados.

## Execução

Executar o pipeline de segmentação:

```bash
python src/segmentation/otsu.py
```

Os resultados gerados serão armazenados em:

```text
outputs/
```

## Interface

A versão final do projeto contará com uma interface gráfica para visualização dos resultados.

A interface deverá exibir:

```text
┌─────────────┬─────────────┬─────────────┐
│  Original   │  Máscara    │   Overlay   │
└─────────────┴─────────────┴─────────────┘
```

Permitindo ao usuário comparar visualmente:

* Imagem original;
* Resultado da segmentação;
* Região de interesse destacada.

## Tecnologias Utilizadas

* Python
* OpenCV
* NumPy
* Matplotlib
* Scikit-image
* Scikit-learn
* Pandas
* Kaggle CLI

## Resultados Esperados

* Segmentação eficiente das regiões de interesse;
* Extração automática das borboletas presentes nas imagens;
* Avaliação quantitativa dos métodos utilizados;
* Visualização clara dos resultados obtidos;
* Aplicação prática de conceitos de Inteligência Artificial e Processamento Digital de Imagens.

## Licença

Este projeto possui finalidade exclusivamente acadêmica e educacional, sendo desenvolvido para a disciplina de Inteligência Artificial Aplicada à Análise de Imagens e Reconhecimento de Padrões.
