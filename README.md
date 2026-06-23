# Reconhecimento de Borboletas 🦋

Segmentação semântica e reconhecimento de padrões em imagens de borboletas utilizando Visão Computacional e Deep Learning.

## Visão Geral

Este é um projeto de Machine Learning voltado para a extração de características e segmentação automática de borboletas em imagens complexas. O objetivo principal é treinar modelos capazes de gerar máscaras binárias precisas, separando o indivíduo do fundo da imagem (região de interesse), viabilizando o reconhecimento de padrões morfológicos.

Atualmente, o foco do projeto está no pré-processamento, treinamento e avaliação de modelos de segmentação semântica. Em versões futuras, o modelo treinado poderá ser integrado a uma aplicação visual interativa para inferência.

O projeto foi desenvolvido como estudo prático e rigoroso em:

* Computer Vision e Processamento Digital de Imagens
* Semantic Segmentation
* Extração de características e limiarização
* Organização de pipelines reproduzíveis de Machine Learning

## Dataset

O dataset utilizado para o treinamento e validação das máscaras é:

* Butterfly Dataset
* Fonte: Kaggle
* Contém imagens RGB de borboletas e suas respectivas máscaras binárias (*ground truth*)

Dataset:
https://www.kaggle.com/datasets/veeralakrishna/butterfly-dataset

## Estrutura do Projeto

```text
reconhecimento-borboleta/
│
├── data/
│   └── butterfly_dataset/
│
├── notebooks/
│
├── src/
│   ├── train.py
│   ├── predict.py
│   ├── evaluate.py
│   └── utils.py
│
├── models/
│
├── runs/
│
├── download_dataset.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/reconhecimento-borboleta.git
cd reconhecimento-borboleta
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

O projeto utiliza a CLI oficial do Kaggle para baixar automaticamente o dataset.

Após instalar as dependências, execute:

```bash
kaggle auth login
```

Um link será exibido no terminal.

1. Abra o link no navegador;
2. Faça login na sua conta Kaggle;
3. Autorize o acesso;
4. Retorne ao terminal.

As credenciais serão armazenadas automaticamente e não será necessário repetir esse processo.

Para verificar se a autenticação foi realizada corretamente:

```bash
kaggle datasets list -s butterfly
```

## Download do Dataset

Após autenticar sua conta:

```bash
python download_dataset.py
```

O script irá:

* Verificar se o dataset já existe localmente;
* Fazer o download apenas quando necessário;
* Organizar automaticamente os arquivos do projeto.

Os dados serão armazenados em:

```text
data/butterfly_dataset/
```

## Treinamento

Exemplo de treinamento:

```bash
python src/train.py
```

Durante o treinamento serão gerados:

* Pesos do modelo
* Métricas de validação
* Curvas de aprendizado
* Matrizes de confusão
* Relatórios de desempenho

Os resultados serão salvos em:

```text
runs/
```

## Inferência

Para classificar novas imagens:

```bash
python src/predict.py
```

Os resultados serão salvos no diretório:

```text
runs/
```

## Objetivos

### Fase Atual

* Classificar espécies de borboletas automaticamente;
* Explorar arquiteturas modernas de Deep Learning;
* Avaliar métricas de desempenho em classificação multiclasse;
* Desenvolver um pipeline reproduzível para classificação de imagens;
* Comparar diferentes modelos e hiperparâmetros.

### Fase Futura

* Desenvolver uma aplicação web para classificação em tempo real;
* Permitir upload de imagens pelo usuário;
* Exibir a espécie identificada e sua probabilidade;
* Disponibilizar o modelo treinado online;
* Criar uma interface amigável para demonstração dos resultados.

## Tecnologias Utilizadas

* Python
* TensorFlow / Keras
* PyTorch
* OpenCV
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Kaggle CLI

## Resultados Esperados

* Alta precisão na identificação das espécies de borboletas;
* Pipeline automatizado de treinamento e inferência;
* Comparação entre diferentes arquiteturas de classificação;
* Base para futuros projetos de visão computacional aplicados à biodiversidade;
* Integração futura com aplicações web.

## Licença

Este projeto é destinado a fins educacionais, como parte das exigências da disciplina de Inteligência Artificial Aplicada à Análise de Imagens e Reconhecimento de Padrões da Universidade Federal de Lavras.

