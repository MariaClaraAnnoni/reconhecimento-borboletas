# reconhecimento-borboletas
# Segmentação e Reconhecimento de Padrões em Borboletas

Repositório dedicado ao projeto da disciplina de **Inteligência Artificial Aplicada à Análise de Imagens e Reconhecimento de Padrões** da Universidade Federal de Lavras.

## 📌 Sobre o Projeto
O objetivo central deste trabalho é investigar e aplicar técnicas avançadas de Visão Computacional para a segmentação de imagens de borboletas. Através da extração de máscaras binárias (*ground truth*), o *pipeline* busca isolar a região de interesse anatômica, separando o indivíduo do fundo da imagem. Esta etapa de pré-processamento e segmentação é crucial para viabilizar a posterior extração de características e o reconhecimento de padrões morfológicos.

## 🛠️ Stack Tecnológico
O ambiente de desenvolvimento numérico e de experimentação foi estruturado em Python, empregando o seguinte ecossistema científico:

* **Visão Computacional e Processamento:** `opencv-python`, `scikit-image`, `rembg`
* **Deep Learning e Modelagem:** `torch`, `tensorflow`, `ultralytics`
* **MLOps e Rastreamento de Experimentos:** `mlflow`, `wandb`
* **Análise Numérica e Visualização:** `numpy`, `pandas`, `matplotlib`, `seaborn`

## ⚙️ Metodologia e Avaliação
A arquitetura do modelo será treinada para prever a máscara correspondente à silhueta da borboleta em imagens complexas. O rigor e a precisão do modelo serão avaliados primariamente por métricas de sobreposição espacial, em especial a Interseção sobre a União (IoU):

$$IoU = \frac{|A \cap B|}{|A \cup B|}$$

Onde $A$ representa a máscara prevista pelo modelo e $B$ a anotação real esperada (*ground truth*). Adicionalmente, outras métricas espaciais e funções de perda específicas para segmentação poderão ser monitoradas durante o treinamento.
